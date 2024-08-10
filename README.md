# StreetSpecter
__StreetSpecter__ is an innovative AI-driven solution designed to detect potholes and facilitate road maintenance. Leveraging advanced technologies, StreetSpecter aims to ensure efficient and proactive road safety measures, making streets safer for everyone.

## Features
* Pothole Detection
* Automatically identifies potholes using Computer-Vision.
* Reports severity levels and location.
* Real-time Monitoring
* Continuously monitors road conditions.
* Sends alerts for dangerous areas.
* User-friendly Interface.
* Easy navigation and reporting.
* Set up alerts for specific areas or severity levels.

## Instructions to use

### Prerequisites
Ensure you have the following installed:
* Python 3.x
* pip
* virtualenv

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Spyrosigma/StreetSpecter
    ```
2. Create Virtual Environment
    ```bash
    pip install virtualenv  #If Virtual Env Module is not installed
    virtualenv envname      # Replace 'envname' with your preferred environment name
    envname\scripts\activate
    ```
3. Install Libraries
    ```bash
    pip install -r requirements.txt
    ```
    
4. Create a .env file and add your own Supabase Keys. 
   ```bash
   SUPABASE_KEY='YOUR_API_KEY'
   SUPABASE_URL='YOUR_URL_KEY'
   ```

5. Run the app!
    ```bash
    python app.py
    ```
