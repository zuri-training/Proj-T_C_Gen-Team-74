const review = document.getElementById('review-body');
review.style.display = 'none';

setTimeout(()=>{
    review.style.display = 'flex';
}, 10000)

// apply initial rate of 4
let activeRateBtn = document.querySelector('.rate.active');

const rateInput = document.getElementById('rate-input');
console.dir(rateInput)
rateInput.value = activeRateBtn.dataset.value;

// select rate
const rateList = document.querySelectorAll('.rate');


rateList.forEach((rateBtn)=>{
    rateBtn.addEventListener('click', ()=>{
        let activeRateBtn = document.querySelector('.rate.active');
        activeRateBtn.classList.remove('active');
        rateBtn.classList.add('active');
        
        // connect rates to form
        activeRateBtn = document.querySelector('.rate.active');
        const rateInput = document.getElementById('rate-input');
        console.dir(rateInput)
        rateInput.value = activeRateBtn.dataset.value;
        rateInput.addEventListener('change', (e)=>{
            console.log(e)
            e.target.value = activeRateBtn.dataset.value;
            console.log(e.target.value)
        })
    })
})

