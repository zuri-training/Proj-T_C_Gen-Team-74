/* Setting the navbar*/

// get dashboard menu button
const header = document.getElementById('header');
header.style.width = "220px";
smallSidebarWidth = '100px'
const sidebar = document.getElementById('mySidenav');

let toggler = false;
const spanList = header.querySelectorAll('span');
const logo = header.querySelector('.logo');


const positionTopNav = () => {
    // Position top nav bar
    const vpWidth = window.innerWidth;
    const sidebarWidth = header.getBoundingClientRect().width;

    // target the main section
    const main = document.getElementById('main');

    const topNav = document.querySelector('main').querySelector('.dash-nav');
    main.style.width = `${vpWidth - sidebarWidth}px`;
    topNav.style.width = `${vpWidth - sidebarWidth}px`;
}
const closedSidebarStyles = () => {
    header.style.width = smallSidebarWidth;
    spanList.forEach((span) => {
        span.style.textAlign = "center";
        span.style.marginLeft = "0";
        span.style.fontSize = ".8rem";
        span.style.paddingTop = "3px";
        span.style.lineHeight = ".8rem";
        span.parentElement.querySelector('img').style.display = "block";
        span.parentElement.querySelector('img').style.margin = "auto";
        span.parentElement.style.display = "flex";
        span.parentElement.style.flexDirection = "column";
        span.parentElement.style.alignItems = "center";
    })
    // switch to smaller logo
    logo.querySelector('.full-logo').style.display = 'none';
    logo.querySelector('.half-logo').style.display = 'block';
    logo.querySelector('.half-logo').style.width = '80%';
    logo.querySelector('.half-logo').style.margin = '0 auto';
}
const openSidebarStyles = () => {
    header.style.width = "220px";
        spanList.forEach((span) => {
            // span.style.display = "inline";
            span.style.textAlign = "left";
            span.style.marginLeft = "0.3rem";
            span.style.fontSize = "1rem";
            span.style.paddingTop = "0px";
            span.style.lineHeight = "1rem";
            span.parentElement.querySelector('img').style.display = "inline";
            span.parentElement.querySelector('img').style.margin = "auto";
            span.parentElement.style.display = "block";
        })
        logo.querySelector('.full-logo').style.display = 'block';
        logo.querySelector('.half-logo').style.display = 'none';
}
positionTopNav();

window.addEventListener('resize', positionTopNav)
function styleLayout() {
    positionTopNav()
    if (toggler) {
        // Adjust styles when sidebar is closed

        closedSidebarStyles();
        toggler = !toggler;
    } else {
        // Adjust styles when sidebar is open
        
        openSidebarStyles();
        toggler = !toggler;
    }
    // Position top nav bar
    positionTopNav();
}
// styleLayout()
sidebar.addEventListener('click', styleLayout)
toggler = true;

// Mobile styles 

const mobileStyles = () => {

    if (document.documentElement.scrollWidth < 900) {
        // Adjust styles when sidebar is closed
        closedSidebarStyles()
        sidebar.removeEventListener('click', styleLayout);
    } else {
        toggler ? openSidebarStyles() : closedSidebarStyles()
        sidebar.addEventListener('click', styleLayout);
    }
    positionTopNav();
}

mobileStyles();

window.addEventListener('resize', mobileStyles)