document.addEventListener('DOMContentLoaded', function() {
    const galleryContainer = document.getElementById('galleryContainer');
    const urlParams = new URLSearchParams(window.location.search);
    const jobId = urlParams.get('job_id');
    const folder = urlParams.get('folder') || '';

    function refreshGallery() {
        fetch(`/jobs/${jobId}/images?folder=${folder}`)
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

    setInterval(refreshGallery, 2500);
});
