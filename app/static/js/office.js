document.addEventListener('DOMContentLoaded', function() {
    const processingCompleteJobsList = document.getElementById('processingCompleteJobsList');

    function refreshProcessingCompleteJobsList() {
        fetch('/jobs?status=processing-complete')
        .then(response => response.json())
        .then(jobs => {
            processingCompleteJobsList.innerHTML = '';
            jobs.forEach(job => {
                const listItem = document.createElement('li');
                listItem.textContent = `Job ${job.job_number} - ${job.character} (${job.fandom})`;

                const outputReadyButton = document.createElement('button');
                outputReadyButton.textContent = 'Finished';
                outputReadyButton.addEventListener('click', () => {
                    updateJobStatus(job.id, 'finished');
                });

                listItem.appendChild(finalizingButton);
                listItem.appendChild(outputReadyButton);
                processingCompleteJobsList.appendChild(listItem);
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
            refreshProcessingCompleteJobsList();
        })
        .catch(error => console.error('Error updating job status:', error));
    }

    refreshProcessingCompleteJobsList();
});
