
//Animation function
document.querySelector('.project').style.display='none'
document.querySelector('.loader').classList.add('loader')

setTimeout(() => {
    document.querySelector('.project').style.display='block'
    document.querySelector('.loader').style.display='none'
},2000)


//Counter Function

const valueDisplay = document.querySelectorAll('.num');
let interval = 1000;

valueDisplay.forEach((valueDisplays) => {
    let startValue = 100;
    let endValue = parseInt(valueDisplays.getAttribute('data-val'));
    let duration = Math.floor(interval / endValue);
    let counter = setInterval(function () {
        startValue += 10;
        valueDisplays.textContent = startValue;
        if(startValue == endValue) {
            clearInterval(counter)
        }
    }, duration)
})



