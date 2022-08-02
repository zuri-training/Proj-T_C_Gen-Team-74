// You can create your own js files for your pages as need arises and link them to the relevant pages

//Dinho 

//Animation function
document.querySelector('.project').style.display='none'
document.querySelector('.loader').classList.add('loader')

setTimeout(() => {
    document.querySelector('.project').style.display='block'
    document.querySelector('.loader').style.display='none'
},2000)


//Navbar Toggler function

const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('nav-links')[0]


toggleButton.addEventListener('click', ()=> {
    navbarLinks.classList.toggle('active')
})


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



