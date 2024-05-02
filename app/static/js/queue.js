document.addEventListener('DOMContentLoaded', function() {
    const queueTable = document.getElementById('queueTable');
    const statusFilter = document.getElementById('statusFilter');
    let jobs = [];

    function refreshQueue() {
        const status = statusFilter.value;
        const url = status ? `/jobs?status=${status}` : '/jobs';

        fetch(url)
        .then(response => response.json())
        .then(data => {
            jobs = data;
            renderQueue();
        });
    }

    function renderQueue() {
        const tbody = queueTable.querySelector('tbody');
        tbody.innerHTML = '';

        jobs.forEach(job => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${job.job_number}</td>
                <td>${job.nickname}</td>
                <td>${job.character}</td>
                <td>${job.fandom}</td>
                <td>${job.status}</td>
                <td>${new Date(job.created_at).toLocaleString()}</td>
                <td>${job.updated_at ? new Date(job.updated_at).toLocaleString() : ''}</td>
                <td>
                    <a href="/gallery.html?job_id=${job.id}">View Gallery</a>
                </td>
            `;
            tbody.appendChild(tr);
        });
    }

    function sortQueue(column) {
        jobs.sort((a, b) => {
            if (column === 'created_at' || column === 'updated_at') {
                return new Date(a[column]) - new Date(b[column]);
            } else {
                if (a[column] < b[column]) return -1;
                if (a[column] > b[column]) return 1;
                return 0;
            }
        });
        renderQueue();
    }

    queueTable.querySelectorAll('th').forEach(th => {
        th.addEventListener('click', () => {
            sortQueue(th.dataset.sort);
        });
    });

    statusFilter.addEventListener('change', refreshQueue);
    const refreshButton = document.getElementById('refreshButton');
    refreshButton.addEventListener('click', refreshQueue);
    refreshQueue();
});
