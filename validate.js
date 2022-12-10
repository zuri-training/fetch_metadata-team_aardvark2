const form = document.querySelector("#form");
const username = document.querySelector("#username");
const email = document.querySelector("#email");
const password = document.querySelector("#password");
const password2 = document.querySelector("#password2");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  checkInputs();
});

function checkInputs() {
  // get value from input
  //trim to remove the whitespaces
  const usernameValue = username.value.trim();
  const emailValue = email.value.trim();
  const passwordValue = password.value.trim();
  const password2Value = password2.value.trim();

  if (usernameValue === "") {
    //show error
    //add error class
    setErrorFor(username, " Oops! Username cannot be blank");
  }

  if (emailValue === "") {
    setErrorFor(email, " Oops! Email cannot be blank");
  } else if (!isEmail(emailValue)) {
    setErrorFor(email, "Please enter a valid email address");
  }

  if (passwordValue === "") {
    setErrorFor(password, "Oops! password cannot be blank");
  }

  if (password2Value === "") {
    setErrorFor(password2, "Oops! confirm password cannot be blank");
  } else if (passwordValue !== password2Value) {
    setErrorFor(password2, "Passwords does not match");
  }
}

function setErrorFor(input, message) {
  const formControl = input.parentElement; // .from-control
  const small = formControl.querySelector("small");

  // add error message inside small
  small.innerText = message;
  //add error class
  formControl.className = "form-control error";
}

function isEmail(email) {
  return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
    email
  );
}

function successMessage(form) {
  const showSuccessMessage = form.parentElement;
  showSuccessMessage.className = "success-message";
}

// OTP Input
function clickEvent(first, last) {
  if (first.value.length) {
    document.getElementById(last).focus();
  }
}
