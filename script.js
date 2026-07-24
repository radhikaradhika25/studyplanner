function addTask() {

    let subject = document.getElementById("subject").value;
    let topic = document.getElementById("topic").value;
    let deadline = document.getElementById("deadline").value;

    if (subject === "" || topic === "" || deadline === "") {
        alert("Please fill all fields.");
        return;
    }

    let deadlineList = document.getElementById("deadlineList");

    // Remove the default message
    if (deadlineList.innerHTML.includes("No Tasks")) {
        deadlineList.innerHTML = "";
    }

    let li = document.createElement("li");
    li.innerHTML = "<strong>" + subject + "</strong><br>" +
                   topic + "<br>" +
                   deadline;

    deadlineList.appendChild(li);

    // Clear inputs
    document.getElementById("subject").value = "";
    document.getElementById("topic").value = "";
    document.getElementById("deadline").value = "";

    alert("Task Added Successfully!");
}
