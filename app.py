from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv
import os, requests, pytz
from datetime import datetime
import base64

load_dotenv()

app = Flask(__name__)
CORS(app)

supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# result = supabase.table("pothole_reports").delete().neq('Id', -1).execute()

#LANDING PAGE
@app.route('/')
def index():
    return render_template('index.html')

#DASHBOARD
@app.route('/dashboard')
def dashboard():
    response = supabase.table('pothole_reports').select('Id, latitude, longitude, severity, timestamp, location').order('timestamp', desc=False).execute()
    reports = response.data
    return render_template('dashboard.html', reports=reports)

@app.route('/coordinates')
def coordinates():
    response = supabase.table('pothole_reports').select('Id, latitude, longitude').execute()
    reports = response.data
    return jsonify(reports)


#REPORT PAGE
@app.route('/report', methods=['GET', 'POST'])
def report():
    #This function converts Longitude and Latitude to Place Name
    def get_place_name(latitude, longitude):
        url = "https://nominatim.openstreetmap.org/reverse"
        headers = {
            'User-Agent': 'StreetSpecter' 
        }
        params = {
            'format': 'json',
            'lat': latitude,
            'lon': longitude,
            'zoom': 20,  
            'addressdetails': 1
        }
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if 'display_name' in data:
                place_name_parts = data['display_name'].split(', ')[:-2]
                return ', '.join(place_name_parts)
            else:
                return "Unknown place"
        else:
            return f"Error: {response.status_code}"
        
    if request.method == 'POST':
        location = request.form.get('location')
        latitude, longitude = map(float, location.split(','))
        severity = request.form.get('severity')
        timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d-%m-%Y  %H:%M:%S' )
        photo = request.files.get('photo')

        new_report = {
            'latitude': latitude,
            'longitude': longitude,
            'severity': severity,
            'timestamp': timestamp,
            'location': get_place_name(latitude, longitude)
        }

        if photo:
            photo_data = base64.b64encode(photo.read()).decode('utf-8')
            new_report['photo'] = photo_data

        response = supabase.table('pothole_reports').insert(new_report).execute()

        if response.data:
            return jsonify({'message': 'Report submitted successfully'}), 201
        else:
            return jsonify({'message': 'Error submitting report'}), 500

    return render_template('des.html')



if __name__ == '__main__':
    app.run(debug=True)