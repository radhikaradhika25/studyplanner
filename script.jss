function addTask() {
    let subject = document.getElementById("subject").value;
    let topic = document.getElementById("topic").value;
    let deadline = document.getElementById("deadline").value;

    if (subject === "" || topic === "" || deadline === "") {
        alert("Please fill all fields");
        return;
    }

    let taskList = document.getElementById("taskList");

    let li = document.createElement("li");

    li.innerHTML = `
        <strong>Subject:</strong> ${subject}<br>
        <strong>Topic:</strong> ${topic}<br>
        <strong>Deadline:</strong> ${deadline}
        <br><br>
        <button class="btn complete-btn" onclick="completeTask(this)">
            Complete
        </button>
        <button class="btn delete-btn" onclick="deleteTask(this)">
            Delete
        </button>
    `;

    taskList.appendChild(li);

    document.getElementById("subject").value = "";
    document.getElementById("topic").value = "";
    document.getElementById("deadline").value = "";
}

function completeTask(button) {
    let task = button.parentElement;
    task.classList.toggle("completed");
}

function deleteTask(button) {
    let task = button.parentElement;
    task.remove();
}
