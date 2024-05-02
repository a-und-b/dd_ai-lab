document.addEventListener('DOMContentLoaded', function() {
    const newJobsList = document.getElementById('newJobsList');

    function refreshNewJobsList() {
        fetch('/jobs?status=new')
        .then(response => response.json())
        .then(jobs => {
            newJobsList.innerHTML = '';
            jobs.forEach(job => {
                const listItem = document.createElement('li');
                listItem.textContent = `Job ${job.job_number} - ${job.character} (${job.fandom})`;

                const shootingButton = document.createElement('button');
                shootingButton.textContent = 'Start Shooting';
                shootingButton.addEventListener('click', () => {
                    updateJobStatus(job.id, 'shooting');
                });

                const assetsReadyButton = document.createElement('button');
                assetsReadyButton.textContent = 'Assets Ready';
                assetsReadyButton.addEventListener('click', () => {
                    updateJobStatus(job.id, 'assets-ready');
                });

                listItem.appendChild(shootingButton);
                listItem.appendChild(assetsReadyButton);
                newJobsList.appendChild(listItem);
            });
        });
    }

    function updateJobStatus(jobId, newStatus) {
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
            refreshNewJobsList();
        })
        .catch(error => console.error('Error updating job status:', error));
    }

    refreshNewJobsList();
});
