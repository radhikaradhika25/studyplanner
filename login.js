function login(){
let username=document.getElementById("username").value;
let password=document.getElementById("password").value;
let user=localStorage.getItem("username");
let pass=localStorage.getItem("password");
if(username===user && password===pass){
window.location.href="dashboard.html";
}
else
{
document.getElementById("msg").innerHTML="Invalid Username or Password";
}
}
