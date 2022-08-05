const embedElement = document.getElementById('embed');
const text = embedElement?.dataset.embedHtml;


function copyToClipboard(text) {
    if (!navigator.clipboard){
        anotherCopyToClipboard(text)
        console.log('copied')
    }
    navigator.clipboard.writeText(text).then(function() {
        console.log('Async: Copying to clipboard was successful!');
      }, function(err) {
        console.error('Async: Could not copy text: ', err);
      });
}
function anotherCopyToClipboard(text) {
    console.log('click')
    var input = document.createElement('textarea');
    input.innerHTML = text;
    document.body.appendChild(input);
    input.select();
    var result = document.execCommand('copy');
    document.body.removeChild(input);

    console.log(result)
    return result;
}

// Get embed button
const embedBtn = document.getElementById('embed-btn');

embedBtn.addEventListener('click', (text)=>copyToClipboard(text));

