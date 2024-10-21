document.getElementById('task-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const taskInput = document.getElementById('task-input');
    const newTask = taskInput.value;


    const response = await fetch('/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title: newTask })
    });

    if (response.ok) {
        taskInput.value = ''; // Limpa o campo de entrada
        loadTasks(); // Recarrega a lista de tarefas
    } else {
        alert('Erro ao adicionar a tarefa');
    }
});

// Função para carregar as tarefas da API
async function loadTasks() {
    const response = await fetch('/tasks');
    const tasks = await response.json();

    const taskList = document.getElementById('task-list');
    taskList.innerHTML = '';

    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.title;
        taskList.appendChild(li);
    });
}

// Carregar as tarefas quando a página é aberta
loadTasks();
