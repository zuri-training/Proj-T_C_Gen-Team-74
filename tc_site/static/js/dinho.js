//Chart.Js

const ctx = document.getElementById("myChart").getContext("2d");
const newGen = document.getElementById("newGen").getContext("2d");

//*********Trying to parse data with array**********//

const clingeTotal = document.querySelector(".clinge-total");

// const genFile = [3,1];
//const percentageValue = genFile[1]/genFile[0] * 100;

//clingeTotal.innerHTML = Math.floor(percentageValue) + "%"
//*********Trying to parse data with array**********//

const refEl = document.getElementById("myChart");
const pp_count = refEl.dataset.ppCount
const tc_count = refEl.dataset.tcCount
const draft_pp_count = refEl.dataset.draftPpCount
const draft_tc_count = refEl.dataset.draftTcCount

const myChart = new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: [`${pp_count} Privacy policy`, `${tc_count} Terms and Condition`],
    datasets: [
      {
        label: "# of Votes",
        data: [pp_count, tc_count],
        backgroundColor: ["#BCB612", "#C53F3F"],
        borderWidth: .5,
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
    labels: [`${draft_pp_count} Privacy policy`, `${draft_tc_count} Terms and Condition`],
    datasets: [

      {
        label: "# of Votes",
        data: [draft_pp_count, draft_tc_count],
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
  loading.innerHTML = `  ${dummyData[i]}%`;
  i++;
  if (i == dummyData.length) {
    clearInterval(interval);
    loading.innerHTML = dummyData.findIndex();
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
  if (i == dummyDataTwo.length) {
    clearInterval(interval2);
    loadingTwo.innerHTML = dummyDataTwo.findIndex();
  }
}, 1000);

