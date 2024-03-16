// // Login Page Start
let login = document.querySelector(".login");
let create = document.querySelector(".create");
let container = document.querySelector(".container");
let Uname = document.querySelector("#Uname");
let pass = document.querySelector("#pass");
let goBack = document.querySelector(".BackBtn");

// function OpenImageUpload(){
//     if(Uname.value != "" && pass.value != ""){
//         location.href = "ImageUpload.html";
//     }
//     else{
//         alert("Username or Password are Empty!");
//     }
// }

// login.onclick = function() {
//   // container.classList.add("signinForm");
//   container.children[0].style = "display:none";
//   container.children[1].style = "display:flex";
// };

// create.onclick = function() {
//   container.children[1].style = "display:none";
//   container.children[0].style = "display:flex";
//   // container.classList.remove("signinForm");
// };
// // Login Page End

function moveToPage() {
  location.href = "LoginPage.html";
}
// Upload image script Start
function uploadImage() {
  const fileInput = document.getElementById("imageUpload");
  const uploadedImage = document.getElementById("uploadedImage");
  const resultSection = document.querySelector(".resultSection");

  const file = fileInput.files[0];
  if (file) {
    const reader = new FileReader();

    reader.onload = function (event) {
      uploadedImage.src = event.target.result;
      resultSection.style.display = "flex";
    };
    reader.readAsDataURL(file);
  }
}
// Upload image script End

goBack.onclick = function(){
  location.href = "Index.html";
}

function redirectToImageUpload() {
  window.location.href = "{% url 'image_upload_page' %}";
}
