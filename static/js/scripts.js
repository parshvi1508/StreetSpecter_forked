document.getElementById('start-btn').addEventListener('click', function() {
    // Request location permission
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
});

function successCallback(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);

    // Request camera permission and start video
    const cameraContainer = document.getElementById('camera-container');
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const captureBtn = document.getElementById('capture-btn');

    cameraContainer.style.display = 'block';

    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            video.srcObject = stream;

            captureBtn.addEventListener('click', function() {
                // Capture the image from the video stream
                const context = canvas.getContext('2d');
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                context.drawImage(video, 0, 0, canvas.width, canvas.height);

                // Convert the canvas image to base64 format
                const imageData = canvas.toDataURL('image/png');

                // Send image and location data to the server
                sendDataToServer(imageData, latitude, longitude);
            });
        })
        .catch((err) => {
            console.error('Error accessing the camera: ', err);
        });
}

function errorCallback(error) {
    console.error('Error obtaining location: ', error);
    alert('Location access is required to report a pothole.');
}

function sendDataToServer(imageData, latitude, longitude) {
    fetch('/report', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            image: imageData,
            latitude: latitude,
            longitude: longitude
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Pothole report submitted successfully!');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Error submitting the pothole report.');
    });
}
