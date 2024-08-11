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

## Yolov8s training Stats
### Model Trained in Colab (T4 GPU) on 5493 Images for 25 epochs in 1.63 hours, Validated on 1698 Images. 

![Screenshot (329)](https://github.com/user-attachments/assets/43b7be87-c06e-452d-849f-76d068e308bd)  

### Training Results

1. Results
- ![results](https://github.com/user-attachments/assets/bbda69d0-b001-4f3a-8cdc-17929de3a3c0)

2. Confusion matrix (
- ![confusion_matrix](https://github.com/user-attachments/assets/1917b6d5-c2b1-4c15-9bde-13a3e9f32a70)

3. Val Batch 0
- ![validation](https://github.com/user-attachments/assets/61ac0a9d-77df-4c83-83f1-c27a4099e49f)



## StreetSpecter Application Snaps

![Screenshot (331)](https://github.com/user-attachments/assets/28d46fd6-aaf6-4f70-96c1-478990986c70)

![Screenshot (333)](https://github.com/user-attachments/assets/f904f9a0-1989-4147-a3ab-98aa2a49dd4d)

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
