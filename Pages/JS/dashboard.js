// The Nav Bar
function openNav() {
  document.getElementById("menu").style.width = "371px";
}

function closeNav() {
  document.getElementById("menu").style.width = "0";
}

// Submit form
function submitform()
{
  document.myform.submit();
}

// Upload Button 
function uploadButton() {
  let fileInput = document.getElementById('fileInput');
  fileInput.click();
}

// function uploadFile(){
//     let fileInput = document.querySelector("#fileInput");
//     let file = fileInput.files[0];
    
//     let formData = new FormData();
//     formData.append("file", file);
    
//     let xhr = new XMLHttpRequest();
//     xhr.open("POST", "upload.php");
//     xhr.send(formData);
// }

// uploadFile();



