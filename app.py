from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv
import os
from datetime import datetime, timezone

load_dotenv()

app = Flask(__name__)
CORS(app)

supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    response = supabase.table('pothole_reports').select('*').order('timestamp', desc=True).execute()
    reports = response.data
    return render_template('dashboard.html', reports=reports)

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        severity = request.form.get('severity')
        timestamp = datetime.now(timezone.utc).astimezone().isoformat()

        new_report = {
            'latitude': float(latitude),
            'longitude': float(longitude),
            'severity': severity,
            'timestamp': timestamp
        }

        response = supabase.table('pothole_reports').insert(new_report).execute()

        if response.data:
            return jsonify({'message': 'Report submitted successfully'}), 201
        else:
            return jsonify({'message': 'Error submitting report'}), 500

    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=False)