


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
