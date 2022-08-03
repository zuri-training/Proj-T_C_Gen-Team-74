            // Javascript Functions for Form Page
/**
 * Define a function to navigate betweens form steps.
 * It accepts one parameter. That is - step number.
 */
 const navigateToFormStep = (stepNumber) => {
    /**
     * Hide all form steps.
     */
    document.querySelectorAll(".form-step").forEach((formStepElement) => {
        formStepElement.classList.add("d-none");
    });
    /**
     * Mark all form steps as unfinished.
     */
    document.querySelectorAll(".form-stepper-list").forEach((formStepHeader) => {
        formStepHeader.classList.add("form-stepper-unfinished");
        formStepHeader.classList.remove("form-stepper-active", "form-stepper-completed");
    });
    /**
     * Show the current form step (as passed to the function).
     */
    document.querySelector("#step-" + stepNumber).classList.remove("d-none");
    /**
     * Select the form step box (progress bar).
     */
    const formStepBox = document.querySelector('li[step="' + stepNumber + '"]');
    /**
     * Mark the current form step as active.
     */
    formStepBox.classList.remove("form-stepper-unfinished", "form-stepper-completed");
    formStepBox.classList.add("form-stepper-active");
    /**
     * Loop through each form step circles.
     * This loop will continue up to the current step number.
     * Example: If the current step is 3,
     * then the loop will perform operations for step 1 and 2.
     */
    for (let index = 0; index < stepNumber; index++) {
        /**
         * Select the form step circle (progress bar).
         */
        const formStepBox = document.querySelector('li[step="' + index + '"]');
        /**
         * Check if the element exist. If yes, then proceed.
         */
        if (formStepBox) {
            /**
             * Mark the form step as completed.
             */
            formStepBox.classList.remove("form-stepper-unfinished", "form-stepper-active");
            formStepBox.classList.add("form-stepper-completed");
        }
    }
};
/**
 * Select all form navigation buttons, and loop through them.
 */
document.querySelectorAll(".btn-navigate-form-step").forEach((formNavigationBtn) => {
    /**
     * Add a click event listener to the button.
     */
    formNavigationBtn.addEventListener("click", () => {
        /**
         * Get the value of the step.
         */
        const stepNumber = parseInt(formNavigationBtn.getAttribute("step_number"));
        /**
         * Call the function to navigate to the target form step.
         */
        navigateToFormStep(stepNumber);
    });
});
/**
         * DropDown Functions
         */
//  function showHideAltUrl () {
//     if(document.getElementById('alturl').value == "yes")
//     {document.getElementById('secondurl').style.display = 'block';
//     } else {
//         document.getElementById('secondurl').style.display = 'none';
//             }
// }

function show1(){
    document.getElementById('secondurl').style.display ='none';
  }
  function show2(){
    document.getElementById('secondurl').style.display = 'block';
  }

//   Add style to the country input

const countryInput = document.getElementById('country')

countryInput.children[1].classList.add('form-select')

//   Add style to the company_type input

const companyTypeInput = document.getElementById('company_type')

companyTypeInput.children[1].classList.add('form-select')