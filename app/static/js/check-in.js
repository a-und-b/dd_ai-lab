document.addEventListener('DOMContentLoaded', function() {
    const checkInForm = document.getElementById('checkInForm');
    const jobList = document.getElementById('jobList');

    // Function to refresh the job list
    function refreshJobList() {
        fetch('/jobs')
        .then(response => response.json())
        .then(data => {
            jobList.innerHTML = '';
            data.forEach(job => {
                const item = document.createElement('li');
                const jobInfo = `
                    <strong>Job Number:</strong> ${job.job_number} <br>
                    <strong>Nickname:</strong> ${job.nickname} <br>
                    <strong>Character:</strong> ${job.character} <br>
                    <strong>Fandom:</strong> ${job.fandom} <br>
                    <strong>Background:</strong> ${job.background} <br>
                    <strong>Mood:</strong> ${job.mood} <br>
                    <strong>Style:</strong> ${job.style} <br>
                    <strong>Status:</strong> ${job.status} <br>
                    <strong>Created At:</strong> ${new Date(job.created_at).toLocaleString()} <br>
                    <strong>Updated At:</strong> ${job.updated_at ? new Date(job.updated_at).toLocaleString() : 'N/A'} <br>
                    <img src="${job.qr_code_url}" alt="QR Code" width="100" height="100"> <br>
                    <a href="/gallery.html?job_id=${job.id}">View Gallery</a>
                    <a href="/gallery.html?job_id=${job.id}&folder=raw">Raw Images</a> |
                    <a href="/gallery.html?job_id=${job.id}&folder=generated_images">Generated Images</a>
                    <a href="/gallery.html?job_id=${job.id}&folder=ipadapter">Generated Images</a>
                    <a href="/gallery.html?job_id=${job.id}&folder=masks">Generated Images</a>
                    <a href="/gallery.html?job_id=${job.id}&folder=controlnet_assets">Generated Images</a>
                `;
                item.innerHTML = jobInfo;
                const statuses = ['new', 'shooting', 'assets-ready', 'processing', 'output-ready', 'finished'];
                statuses.forEach(status => {
                    const statusBtn = document.createElement('button');
                    statusBtn.textContent = status;
                    statusBtn.onclick = () => updateStatus(job.id, status);
                    item.appendChild(statusBtn);
                });
                jobList.appendChild(item);
            });
        });
    }

    // Function to update job status
    function updateStatus(jobId, newStatus) {
        fetch(`/jobs/${jobId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ status: newStatus })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            refreshJobList();
        })
        .catch(error => console.error('Error updating job status:', error));
    }

    // Submit check-in form via AJAX
    checkInForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(this);

        fetch('/jobs', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            alert('Check-in successful. Job ID: ' + data.job_id);
            refreshJobList();
            this.reset();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred during check-in.');
        });
    });

    // Function to refresh the gallery
    function refreshGallery(jobId) {
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

    // Initial job list refresh
    refreshJobList();
});

