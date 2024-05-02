document.addEventListener('DOMContentLoaded', function() {
    const galleryContainer = document.getElementById('galleryContainer');
    const jobId = new URLSearchParams(window.location.search).get('job_id');

    function refreshGallery() {
        fetch(`/jobs/${jobId}/images`)
        .then(response => response.json())
        .then(images => {
            galleryContainer.innerHTML = '';
            images.forEach(image => {
                const img = document.createElement('img');
                img.src = image.url;
                img.alt = image.filename;
                galleryContainer.appendChild(img);
            });
        });
    }

    setInterval(refreshGallery, 2500); // Aktualisiere die Galerie alle 5 Sekunden
});
