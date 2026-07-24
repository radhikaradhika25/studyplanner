let tasks=JSON.parse(localStorage.getItem("tasks")) || [];

let output="";

tasks.forEach(task=>{

if(task.status=="Completed"){

output+=`
<tr>

<td>${task.subject}</td>

<td>${task.topic}</td>

<td>${new Date().toLocaleDateString()}</td>

</tr>
`;

}

});

document.getElementById("completedList").innerHTML=output;
