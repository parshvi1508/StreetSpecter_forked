document.addEventListener('DOMContentLoaded', function() {
    const reportForm = document.getElementById('reportForm');
    const message = document.getElementById('message');

    if (reportForm) {
        reportForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(reportForm);
            
            fetch('/report', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                message.textContent = data.message;
                message.style.color = 'green';
                reportForm.reset();
            })
            .catch(error => {
                message.textContent = 'An error occurred. Please try again.';
                message.style.color = 'red';
            });
        });
    }

    // Simple map initialization (replace with a proper map library like Leaflet or Google Maps)
    const map = document.getElementById('map');
    if (map) {
        
    }
});