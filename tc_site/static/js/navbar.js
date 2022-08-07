const navbar = document.getElementById('landing-navbar');
navbar.style.setProperty('--light-color', 'transparent');

// console.dir(navbar);

// Set Hero nav styles
const aList = navbar.querySelector('.nav-lg').querySelectorAll('a')

aList.forEach((a) => {
    a.style.color = 'var(--white-color)';

    console.log(a)

    span = a.querySelector('span');
    console.log(span);
    if (span) {
        span.style.color = 'var(--white-color)';
    }
    
    // on hover styles for nav items
    a.addEventListener('mouseover', () => {
        a.style.color = 'var(--primary-yellow-light)';
        a.style.background = 'transparent';
    })
    
    // reset after hover is done
    a.addEventListener('mouseleave', () => {
        a.style.color = 'var(--white-color)';
    })
})

// Nav auth buttons conditional styles

const priBtn = navbar.querySelector('.nav-lg').querySelector('.pri-btn');
const secBtn = navbar.querySelector('.nav-lg').querySelector('.sec-btn');



// Get hero height

const hero = document.getElementById('hero');

document.addEventListener('scroll', () => {
    // console.log(hero.scrollHeight)
    const heroHeight = hero.getBoundingClientRect().height === 0 ? document.documentElement.scrollHeight : hero.getBoundingClientRect().height;
    const pageOffset = hero.getBoundingClientRect().top;

    console.log(hero.getBoundingClientRect());
    console.log(-1 * +pageOffset);
    console.log(heroHeight);


    if (+heroHeight <= (-1 * +pageOffset)) {
        // reset white nav styles
        navbar.style.position = 'fixed';
        navbar.style.setProperty('--light-color', 'white'); // '#E3DFE5' looks iffy


        // reset anchor tag colors
        const aList = navbar.querySelector('.nav-lg').querySelectorAll('a')

        aList.forEach((a) => {
            a.style.color = 'var(--primary-blue)';

            span = a.querySelector('span');
            if (span) {
                span.style.color = 'var(--primary-blue)';
            }

            // on hover styles for nav items
            a.addEventListener('mouseover', () => {
                a.style.color = 'var(--white-color)';
                a.style.background = 'var(--primary-yellow)';
            })
    
            // reset after hover is done
            a.addEventListener('mouseleave', () => {
                a.style.color = 'var(--primary-blue)';
                a.style.background = 'transparent';
            })
        })

        // Reset auth button colors for large nav bar
        const priBtn = navbar.querySelector('.nav-lg').querySelector('.pri-btn');
        const secBtn = navbar.querySelector('.nav-lg').querySelector('.sec-btn');
        priBtn.style.color = 'var(--primary-blue)';
        secBtn.style.color = 'var(--primary-yellow)';

        // on hover styles for auth buttons
        priBtn.addEventListener('mouseover', () => {
            priBtn.style.color = 'var(--white-color)';
            priBtn.style.background = 'var(--primary-blue)'
        })
        secBtn.addEventListener('mouseover', () => {
            secBtn.style.color = 'var(--white-color)';
            secBtn.style.background = 'var(--primary-yellow)';
        })

        // reset after hover is done
        priBtn.addEventListener('mouseleave', () => {
            priBtn.style.color = 'var(--primary-blue)';
            priBtn.style.background = 'transparent';
        })
        secBtn.addEventListener('mouseleave', () => {
            secBtn.style.color = 'var(--primary-yellow)';
            secBtn.style.background = 'transparent';
        })

        // reset display of the logo.
        navbar.querySelector('.logo').querySelector('.white-navbar-logo').style.display = 'block'
        navbar.querySelector('.logo').querySelector('.transparent-navbar-logo').style.display = 'none'

        navbar.style.boxShadow = '0 0 .5rem #555';

        // Reset menu button styles
        const menubtnLine = navbar.querySelector('.menu-line');

        const primaryBlue = window.getComputedStyle(navbar).getPropertyValue("--primary-blue");
        console.log('blue: ', primaryBlue)

        menubtnLine.style.setProperty('--menu-line-color', primaryBlue)

    } else {
        // Transparent navbar styles
        navbar.style.position = 'absolute';
        navbar.style.setProperty('--light-color', 'transparent');

        const aList = navbar.querySelector('.nav-lg').querySelectorAll('a')

        aList.forEach((a) => {
            a.style.color = 'var(--white-color)';
            span = a.querySelector('span');

            if (span) {
                span.style.color = 'var(--white-color)';
            }

            // on hover styles for nav items
            a.addEventListener('mouseover', () => {
                a.style.color = 'var(--primary-yellow-light)';
                a.style.background = 'transparent';
            })
            
            // reset after hover is done
            a.addEventListener('mouseleave', () => {
                a.style.color = 'var(--white-color)';
            })
        })

        const priBtn = navbar.querySelector('.nav-lg').querySelector('.pri-btn');
        const secBtn = navbar.querySelector('.nav-lg').querySelector('.sec-btn');

        priBtn.style.color = 'var(--white-color)'
        secBtn.style.color = 'var(--white-color)'
        
        priBtn.addEventListener('mouseleave', () => {
            priBtn.style.color = 'var(--white-color)'
        })
        secBtn.addEventListener('mouseleave', () => {
            secBtn.style.color = 'var(--white-color)'
        })

        navbar.querySelector('.logo').querySelector('.white-navbar-logo').style.display = 'none'
        navbar.querySelector('.logo').querySelector('.transparent-navbar-logo').style.display = 'block'
        navbar.style.boxShadow = 'none'

        // Reset menu button styles
        const menubtnLine = navbar.querySelector('.menu-line');

        const whiteColor = window.getComputedStyle(navbar).getPropertyValue("--white-color");
        console.log('whiteColor: ', whiteColor)
        menubtnLine.style.setProperty('--menu-line-color', whiteColor)

    }
})




