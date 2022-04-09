
var password = document.getElementById("password")
  , confirmpassword = document.getElementById("confirmpassword");

function validatePassword(){
  if(password.value != confirmpassword.value) {
    confirmpassword.setCustomValidity("Please enter the same password");
  } else {
    confirmpassword.setCustomValidity('');
  }
}

password.onchange = validatePassword;
confirmpassword.onkeyup = validatePassword;