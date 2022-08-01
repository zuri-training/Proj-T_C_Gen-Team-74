const togglePasswordBtn = document.querySelector('#togglePassword');
const passwords = document.querySelectorAll('.password');

passwords.forEach((password) => {

  togglePasswordBtn.addEventListener('click', function () {
    // toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('bi-eye');
  })

})

function enableBtn() {
  var checkBox = document.getElementById('terms_agreement');
  var buTn = document.getElementById('sign-up_btn');

  if (checkBox.checked == true) {
    buTn.removeAttribute('disabled');
  } else {
    buTn.setAttribute('disabled', '');
  }
}


let signupModalActive = false;
let signinModalActive = false;

// Toggle signup modal
const signupBtns = document.querySelectorAll('.sign-up')
const signupModal = document.getElementById('sign-up-modal');
signupModal.style.display = 'none';


signupBtns.forEach((signupBtn) => {
  signupBtn.addEventListener('click', () => {
    if (signupModalActive) {
      signupModal.style.display = 'none';
      signupModalActive = !signupModalActive
    } else {
      // remove signin modal if active
      if (signinModalActive) {
        signinModal.style.display = 'none';
        signinModalActive = !signinModalActive
      }
      signupModal.style.display = 'grid';
      signupModalActive = !signupModalActive
    }
  })
})

// Toggle signin modal
const signinBtns = document.querySelectorAll('.sign-in');
const signinModal = document.getElementById('sign-in-modal');
signinModal.style.display = 'none';

signinBtns.forEach((signinBtn) => {

  signinBtn.addEventListener('click', () => {
    if (signinModalActive) {
      signinModal.style.display = 'none';
      signinModalActive = !signinModalActive
    } else {
      // remove signup modal if active
      if (signupModalActive) {
        signupModal.style.display = 'none';
        signupModalActive = !signupModalActive
      }
      signinModal.style.display = 'grid';
      signinModalActive = !signinModalActive
    }
  })

})

// Add onclick handler to backdrop to remove modal
const backdrops = document.querySelectorAll('.backdrop')
backdrops.forEach((backdrop) => {
  backdrop.addEventListener('click', () => {
    backdrop.parentElement.style.display = 'none';
    signinModalActive = false
    signupModalActive = false
  })
})

// switch from signin to signup and vice versa

