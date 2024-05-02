document.addEventListener('DOMContentLoaded', function() {
    const rawImagesContainer = document.getElementById('rawImagesContainer');
    const controlnetAssetsContainer = document.getElementById('controlnetAssetsContainer');
    const ipadapterContainer = document.getElementById('ipadapterContainer');
    const masksContainer = document.getElementById('masksContainer');
    const generatedImagesContainer = document.getElementById('generatedImagesContainer');
    const finalImagesContainer = document.getElementById('finalImagesContainer');

    const urlParams = new URLSearchParams(window.location.search);
    const jobId = urlParams.get('job_id');
    const folder = urlParams.get('folder');

    function refreshGallery(container, folderName) {
        if (folder && folder !== folderName) {
            container.innerHTML = '';
            return;
        }

        fetch(`/jobs/${jobId}/images?folder=${folderName}`)
        .then(response => response.json())
        .then(images => {
            container.innerHTML = '';
            images.forEach(image => {
                const img = document.createElement('img');
                img.src = image.url;
                img.alt = image.filename;
                container.appendChild(img);
            });
        });
    }

    setInterval(() => {
        refreshGallery(rawImagesContainer, 'raw');
        refreshGallery(controlnetAssetsContainer, 'controlnet_assets');
        refreshGallery(ipadapterContainer, 'ipadapter');
        refreshGallery(masksContainer, 'masks');
        refreshGallery(generatedImagesContainer, 'generated_images');
        refreshGallery(finalImagesContainer, 'final_images');
    }, 1500);
});
