
//Animation function
document.querySelector('.project').style.display='none'
document.querySelector('.loader').classList.add('loader')

setTimeout(() => {
    document.querySelector('.project').style.display='block'
    document.querySelector('.loader').style.display='none'
},1000)


//Navbar Toggler function

const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.querySelectorAll('.nav-item')


navbarLinks.forEach((navbarLink)=>{
    navbarLink.addEventListener('click', ()=> {
        const activeNavbarLinks = document.querySelectorAll('.active')

        activeNavbarLinks.forEach((activeNavbarLink)=>{
            activeNavbarLink.classList.remove("active");
        })
        
        navbarLink.classList.add('active')
    })

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



// Animation

// Auto Typing Effect
var typed = new Typed('#auto-type', {
    strings: ["Creator","Generator","Builder"], typeSpeed: 200,
    backSpeed: 250,
    loop: true,
    smartBackspace: true
})


//Fades Animations
AOS.init();