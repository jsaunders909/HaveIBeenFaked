const chill = document.querySelector(".chill");
const adventure = document.querySelector(".adventure");
const both = document.querySelector(".both");

chill.onclick = () => submit('chill');
adventure.onclick = () => submit('adventure');
both.onclick = () => submit('both');

function submit(value) {
    window.location.href = "/match.html";
}