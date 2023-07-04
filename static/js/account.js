const loginElement = document.querySelector("#login");
const registerElement = document.querySelector("#register");

document.querySelector("#register > a").addEventListener("click", (event) => {
    event.preventDefault();
    loginElement.style.display = "block";
    registerElement.style.display = "none";
})

document.querySelector("#login > a").addEventListener("click", (event) => {
    event.preventDefault();
    registerElement.style.display = "block";
    loginElement.style.display = "none";
})
