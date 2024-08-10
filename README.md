# StreetSpecter
StreetSpecter is an innovative AI-driven solution designed to detect potholes and facilitate road maintenance. Leveraging advanced technologies, StreetSpecter aims to ensure efficient and proactive road safety measures, making streets safer for everyone.

## Features
* **Pothole Detection**: Automatically identifies potholes using AI and machine learning.
* **Real-time Monitoring**: Provides up-to-date information on road conditions.
* **User-friendly Interface**: Easy-to-use interface for monitoring and reporting.
* **Custom Alerts**: Set up alerts for specific areas or severity levels.
* 
## Prerequisites
Ensure you have the following installed:
* Python 3
* pip
* virtualenv
  
## Instructions to use

1. Clone the repository:
    ```bash
    git clone https://github.com/Spyrosigma/StreetSpecter
    ```
2. Create Virtual Environment
    ```bash
    pip install virtualenv  #If Virtual Env Module is not installed
    virtualenv envname
    envname\Scripts\activate
    ```
3. Install Libraries
    ```bash
    pip install -r requirements.txt
    ```
    
4. Create a .env file and add your own 'Supabase URL & Supabase Key'. For Example:
   ```bash
   SUPABASE_URL='https://xyzcompany.supabase.co'
   SUPABASE_KEY='uhvki565$55d'
   ``` 
  
5. Run the app!
    ```bash
    python app.py
    ```
