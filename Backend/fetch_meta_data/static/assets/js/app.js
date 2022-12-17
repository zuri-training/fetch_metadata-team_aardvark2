function submitform()
{
  document.myform.submit();
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

function uploadButton() {
    let fileInput = document.getElementById('fileInput');
    fileInput.click();
}


