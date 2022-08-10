const togglePasswordBtns = document.querySelectorAll('.togglePassword'); // I changed the id to a class so I could target multiple buttons at once
const passwords = document.querySelectorAll('.password');

passwords.forEach((password, id) => {

  togglePasswordBtns[id]?.addEventListener('click', function () {
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

// Get the show-sign-up-cheker from the landing block
signupChecker = document.getElementById('sign-up-modal-checker');
signinChecker = document.getElementById('sign-in-modal-checker');
previewChecker = document.getElementById('blank-preview-modal-checker');
forgotPasswordChecker = document.getElementById('forgot-password-modal-checker');


// Create a toggle by checking if the route was redirected to 'signup' or 'signin'
let signupModalActive = signupChecker?.dataset?.showSignUpModal == 'true' ? true : false;
let signinModalActive = signinChecker?.dataset?.showSignInModal == 'true' ? true : false;
let previewModalActive = previewChecker?.dataset?.showBlankPreviewModal == 'true' ? true : false;
let forgotPasswordModalActive = forgotPasswordChecker?.dataset?.showBlankforgotPasswordModal == 'true' ? true : false;

// Toggle signup modal
const signupBtns = document.querySelectorAll('.sign-up')
const signupModal = document.getElementById('sign-up-modal');
signupModal.style.display = signupModalActive ? 'grid' : 'none';


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
signinModal.style.display = signinModalActive ? 'grid' : 'none';

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


// Toggle forgot password modal
const forgotPasswordBtn = document.getElementById('forgot');
const forgotPasswordModal = document.getElementById('forgot-password-modal');
forgotPasswordModal.style.display = forgotPasswordModalActive ? 'grid' : 'none';


  forgotPasswordBtn.addEventListener('click', () => {
    if (forgotPasswordActive) {
      forgotPasswordModal.style.display = 'none';
      forgotPasswordModalActive = !forgotPasswordModalActive
    } else {
      // remove signin modal if active
      if (signinModalActive) {
        signinModal.style.display = 'none';
        signinModalActive = !signinModalActive
      }
      forgotPasswordModal.style.display = 'grid';
      forgotPasswordModalActive = !signinModalActive
    }
  })



// Add onclick handler to backdrop to remove modal
const backdrops = document.querySelectorAll('.backdrop')
backdrops.forEach((backdrop) => {
  backdrop.addEventListener('click', () => removeBackdrop(backdrop))
})
const removeBackdrop = (backdrop) => {
  backdrop.parentElement.style.display = 'none';
  signinModalActive = false
  signupModalActive = false
  forgotPasswordActive = false
  previewModalActive = false
}
const cancelBackdrops = document.querySelectorAll('.cancel-backdrop')
cancelBackdrops.forEach((btn) => {
  btn.addEventListener('click', () => {
    backdrops.forEach((backdrop)=>{
      backdrop.click()
    })
  })
})

// Toggle template Preview modal

const previewModalButton = document.querySelector('.preview-modal-btn')
const previewModal = document.getElementById('preview-modal');
previewModal.style.display = previewModalActive ? 'grid' : 'none';


previewModalButton.addEventListener('click', () => {
  if (previewModalActive) {
    previewModal.style.display = 'none';
    previewModalActive = !previewModalActive
  } else {
    // remove signin modal if active
    // remove signup modal if active
    if (signinModalActive) {
      signinModal.style.display = 'none';
      signinModalActive = !signinModalActive
    }
    if (signupModalActive) {
      signupModal.style.display = 'none';
      signupModalActive = !signupModalActive
    }
    previewModal.style.display = 'grid';
    previewModalActive = !previewModalActive
  }
})
