const togglePassword = document.querySelector('#togglePassword');
  const password = document.querySelector('#password');

  togglePassword.addEventListener('click', function () {
    // toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('bi-eye');
});

function enableBtn() {
  var checkBox = document.getElementById('terms_agreement');
  var buTn = document.getElementById('sign-up_btn');

  if (checkBox.checked == true) {
    buTn.removeAttribute('disabled');
} else {
  buTn.setAttribute('disabled', '');
}
}