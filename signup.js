function signup(){
let username=document.getElementById("newUsername").value;
let email=document.getElementById("email").value;
let password=document.getElementById("newPassword").value;
let confirm=document.getElementById("confirmPassword").value;
if(username=="" || email=="" || password==""){
alert("Please fill all fields");
return;
}
if(password!==confirm){
alert("Passwords do not match");
return;
}
localStorage.setItem("username",username);
localStorage.setItem("password",password);
alert("Account Created Successfully");
window.location.href="index.html";
}
