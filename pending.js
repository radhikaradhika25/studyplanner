let tasks=JSON.parse(localStorage.getItem("tasks")) || [];

let output="";

tasks.forEach((task,index)=>{

if(task.status=="Pending"){

output+=`
<tr>

<td>${task.subject}</td>

<td>${task.topic}</td>

<td>${task.deadline}</td>

<td>

<button onclick="completeTask(${index})">Complete</button>

</td>

</tr>
`;

}

});

document.getElementById("pendingList").innerHTML=output;

function completeTask(i){

tasks[i].status="Completed";

localStorage.setItem("tasks",JSON.stringify(tasks));

location.reload();

}
