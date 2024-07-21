const submitBtn = document.querySelector(".submit");
const username = document.querySelector(".username");
const password = document.querySelector(".password");

submitBtn.onclick = (e) => {
    e.preventDefault();
    if(!username.value || !password.value) return
    window.location.href = "/budget.html";
}