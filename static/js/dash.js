const map = L.map('map').setView([0, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
}).addTo(map);

fetch('/coordinates')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        data.forEach(coord => {
            // Create a marker with the default icon
            const marker = L.marker([coord.latitude, coord.longitude]).addTo(map);

            // Create a custom label with the ID
            const idLabel = L.divIcon({
                className: 'marker-id',
                html: coord.Id,
                iconSize: null,
                iconAnchor: [15, 0], // Offset the label to the right of the icon
            });

            // Add the ID label
            L.marker([coord.latitude, coord.longitude], {
                icon: idLabel,
                zIndexOffset: 1000,
                interactive: false // Make the label non-interactive
            }).addTo(map);

            // Set up the popup on the main marker
            marker.bindPopup(`ID: ${coord.Id}<br>Latitude: ${coord.latitude}<br>Longitude: ${coord.longitude}`);
        });

        const bounds = L.latLngBounds(data.map(coord => [coord.latitude, coord.longitude]));
        map.fitBounds(bounds);
    })
    .catch(error => console.error('Error fetching coordinates:', error));