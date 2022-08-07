/* Setting the navbar*/

// get dashboard menu button
const header = document.getElementById('header');
const sidebar = document.getElementById('mySidenav');

let toggler = true;
const spanList = header.querySelectorAll('span');
const logo = header.querySelector('.logo');


const positionTopNav = () => {
  // Position top nav bar
  const vpWidth = document.documentElement.scrollWidth;
  const sidebarWidth = header.getBoundingClientRect().width;
  // target the main section
  const main = document.querySelector('main');
  const topNav = document.querySelector('main').querySelector('.dash-nav');
  main.style.width = `${vpWidth - sidebarWidth}`;
  topNav.style.width = `${vpWidth - sidebarWidth}px`;
}
positionTopNav();

window.addEventListener('resize', positionTopNav)
function styleLayout() {
  if (toggler) {
    // Adjust styles when sidebar is closed
    // header.style.gridColumn = "1 / span 1";
    header.style.width = "80px";
    spanList.forEach((span) => {
      span.style.display = "none";
    })
    // switch to smaller logo
    logo.querySelector('.full-logo').style.display = 'none';
    logo.querySelector('.half-logo').style.display = 'block';
    logo.querySelector('.half-logo').style.width = '80%';
    logo.querySelector('.half-logo').style.margin = '0 auto';

    // document.getElementById("main").style.gridColumn = "2 / 13";

    // Position top nav bar
    positionTopNav();


    toggler = !toggler;
  } else {
    // Adjust styles when sidebar is open
    header.style.gridColumn = "1 / span 3";
    header.style.width = "220px";
    spanList.forEach((span) => {
      span.style.display = "inline";
    })
    logo.querySelector('.full-logo').style.display = 'block';
    logo.querySelector('.half-logo').style.display = 'none';
    document.getElementById("main").style.gridColumn = "4 / 13";


    // Position top nav bar
    positionTopNav();

    toggler = !toggler;
  }
}
sidebar.addEventListener('click', styleLayout)

// Mobile styles 
window.addEventListener('resize', () => {

  if (document.documentElement.scrollWidth < 900) {
    // Adjust styles when sidebar is closed
    header.style.width = "80px";
    spanList.forEach((span) => {
      span.style.display = "none";
    })
    // switch to smaller logo
    logo.querySelector('.full-logo').style.display = 'none';
    logo.querySelector('.half-logo').style.display = 'block';
    logo.querySelector('.half-logo').style.width = '80%';
    logo.querySelector('.half-logo').style.margin = '0 auto';

    // document.getElementById("main").style.gridColumn = "2 / 13";

    // Position top nav bar
    positionTopNav();

    sidebar.removeEventListener('click', styleLayout);
  } else {
    sidebar.addEventListener('click', styleLayout);
  }
})