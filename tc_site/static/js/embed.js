
function copyToClipboard(text, copyBtn) {
  if (!navigator.clipboard) {
    anotherCopyToClipboard(text)
  }
  navigator.clipboard.writeText(text).then(function () {
    console.log('Async: Copying to clipboard was successful!');
  }, function (err) {
    console.error('Async: Could not copy text: ', err);
  });
  
  copyBtn.classList.add('active');
  setTimeout(() => {
    copyBtn.classList.remove('active');
  }, 2000)
}
function anotherCopyToClipboard(text) {

  var input = document.createElement('textarea');
  input.innerHTML = text;
  document.body.appendChild(input);
  input.focus();
  input.select();
  var result = document.execCommand('copy');

  document.body.removeChild(input);

  return result;
}

// Get embed button
const copyBtns = document.querySelectorAll('.copy-btn');

copyBtns.forEach((copyBtn) => {
  const copyElement = copyBtn.parentNode;

  const text = copyElement?.dataset.copyHtml;
  copyBtn.addEventListener('click', () => copyToClipboard(text, copyBtn));
})

