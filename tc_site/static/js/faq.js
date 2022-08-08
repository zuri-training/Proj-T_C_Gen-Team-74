const descList = [
    'There are no requirements. You can change it as how you want.',
    "You can get it under a minute. It's fast and easy.",
    "No, there is no payment required.",
    "There is no limit to the number of templates. You can generate as long as you want.",
];

const faqList = document.querySelectorAll(".faq-item");

let show = false;
const toggle = (faqItem, id) => {
    const descDiv = document.createElement("div");
    descDiv.classList.add("faq-item-desc");

    const desc = document.createElement("p");

    desc.innerText = descList[id];
    descDiv.appendChild(desc);

    const shownItem = document.querySelector(".show");
    const shownDiv = shownItem?.querySelector(".faq-item-desc");

    if (faqItem.classList.contains("show")) {
        const shownDiv = shownItem?.querySelector(".faq-item-desc");
        console.dir(shownDiv);
        faqItem.classList.remove("show");
        faqItem.removeChild(shownDiv);
    } else {
        shownItem?.classList.remove("show");
        shownItem?.removeChild(shownDiv);
        faqItem.classList.add("show");
        faqItem.appendChild(descDiv);
    }
};

faqList.forEach((faqItem, id) => {
    faqItem.addEventListener("click", () => {
        toggle(faqItem, id);
    });
});
