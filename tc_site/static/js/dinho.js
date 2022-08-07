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


sidebar.addEventListener('click', () => {
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
})



//Chart.Js

const ctx = document.getElementById("myChart").getContext("2d");
const newGen = document.getElementById("newGen").getContext("2d");

//*********Trying to parse data with array**********//

// const clingeTotal = document.querySelector(".clinge-total");

// const genFile = [3,1];
// const percentageValue = genFile[1]/genFile[0] * 100;

// clingeTotal.innerHTML = Math.floor(percentageValue) + "%"
//*********Trying to parse data with array**********//


const myChart = new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: ["2 Privacy policy", "1 Terms and Condition"],
    datasets: [
      {
        label: "# of Votes",
        // data: [genFile[0], genFile[1]],
        data: [2, 1],
        backgroundColor: ["#BCB612", "#C53F3F"],
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
  },
});

const myChart2 = new Chart(newGen, {
  type: "doughnut",
  data: {
    labels: ["1 Privacy policy", "1 Terms and Condition"],
    datasets: [
      {
        label: "# of Votes",
        data: [50, 50],
        backgroundColor: ["#BCB612", "#C53F3F"],
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
  },
});

//progress bar

const progress = document.querySelector(".progress");
const loading = document.querySelector(".loading");
const progressTwo = document.querySelector(".progress2");
const loadingTwo = document.querySelector(".loading2");

//Terms and condition generate function
let i = 0;

const dummyData = [0, 30, 45, 50, 72, 79];

const interval = setInterval(() => {
  progress.style.width = `${dummyData[i]}%`;
  loading.innerHTML = dummyData[i] + "%";
  i++;
  if (i == dummyData.length) {
    clearInterval(interval);
    // loading.innerHTML = dummyData.findIndex(i);
  }
}, 1000);

//Privacy Policy generate function
let x = 0;

const newDataAdd = [0, 15, 21, 25, 29];

const dummyDataTwo = newDataAdd;

const interval2 = setInterval(() => {
  progressTwo.style.width = `${dummyDataTwo[x]}%`;
  loadingTwo.innerHTML = dummyDataTwo[x] + "%";
  x++;
  if (x == dummyDataTwo.length) {
    clearInterval(interval2);
    // loadingTwo.innerHTML = dummyDataTwo.findIndex();
  }
}, 1000);
