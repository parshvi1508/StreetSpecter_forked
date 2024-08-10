from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv
import os, requests, pytz, tempfile, time, shutil
from datetime import datetime
import uuid

load_dotenv()

app = Flask(__name__)
CORS(app)

supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# result = supabase.table("pothole_reports").delete().neq('Id', -1).execute()


# LANDING PAGE
@app.route("/")
def index():
    return render_template("index.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():
    response = (
        supabase.table("pothole_reports")
        .select("Id, latitude, longitude, severity, timestamp, location, media_url")
        .order("timestamp", desc=False)
        .execute()
    )
    reports = response.data
    return render_template("dashboard.html", reports=reports)


@app.route("/coordinates")
def coordinates():
    response = (
        supabase.table("pothole_reports").select("Id, latitude, longitude").execute()
    )
    reports = response.data
    return jsonify(reports)


# REPORT PAGE
@app.route("/report", methods=["GET", "POST"])
def report():
    # This function converts Longitude and Latitude to Place Name
    def get_place_name(latitude, longitude):
        url = "https://nominatim.openstreetmap.org/reverse"
        headers = {"User-Agent": "StreetSpecter"}
        params = {
            "format": "json",
            "lat": latitude,
            "lon": longitude,
            "zoom": 20,
            "addressdetails": 1,
        }
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            if "display_name" in data:
                place_name_parts = data["display_name"].split(", ")[:-2]
                return ", ".join(place_name_parts)
            else:
                return "Unknown place"
        else:
            return f"Error: {response.status_code}"

    if request.method == "POST":
        location = request.form.get("location")
        latitude, longitude = map(float, location.split(","))
        severity = request.form.get("severity")
        timestamp = datetime.now(pytz.timezone("Asia/Kolkata")).strftime(
            "%d-%m-%Y  %H:%M:%S"
        )
        media = request.files.get("media")

        new_report = {
            "latitude": latitude,
            "longitude": longitude,
            "severity": severity,
            "timestamp": timestamp,
            "location": get_place_name(latitude, longitude),
        }

        if media:
            temp_dir = tempfile.mkdtemp()
            temp_path = os.path.join(temp_dir, media.filename)
            try:
                media.save(temp_path)
                unique_filename = f"{uuid.uuid4()}{os.path.splitext(media.filename)[1]}"
                
                # Determine the correct content type
                content_type = media.content_type
                if content_type.startswith('image/'):
                    bucket_folder = "images"
                elif content_type.startswith('video/'):
                    bucket_folder = "videos"
                else:
                    raise ValueError(f"Unsupported media type: {content_type}")
                
                def process_media(temp_path, unique_filename):
                    pass
                    #Computer-Vision applies here!


                # Upload file to Supabase Storage
                with open(temp_path, 'rb') as f:
                    supabase.storage.from_("potholesmedia").upload(
                        file=f,
                        path=f"{bucket_folder}/{unique_filename}", 
                        file_options={"content-type": content_type}
                    )

                # Get public URL for the uploaded file
                file_url = supabase.storage.from_("potholesmedia").get_public_url(
                    f"{bucket_folder}/{unique_filename}"
                )
                print(f"File uploaded successfully. Public URL: {file_url}")

                new_report["media_url"] = file_url

            except Exception as e:
                print(f"Error processing media: {str(e)}")
                return jsonify({"message": f"Error processing media: {str(e)}"}), 500
            finally:
                # Clean up the temporary directory
                retry_count = 5
                while retry_count > 0:
                    try:
                        shutil.rmtree(temp_dir, ignore_errors=True)
                        break
                    except Exception as e:
                        print(f"Failed to remove temp directory, retrying... Error: {str(e)}")
                        time.sleep(1)
                        retry_count -= 1

        response = supabase.table("pothole_reports").insert(new_report).execute()
        print('Executed !!')

        if response.data:
            return jsonify({"message": "Report submitted successfully"}), 201
        else:
            return jsonify({"message": "Error submitting report"}), 500

    return render_template("report.html")


if __name__ == "__main__":
    app.run(debug=True)
