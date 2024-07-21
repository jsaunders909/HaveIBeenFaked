const slider = document.querySelector("#budgetSlider");
const display = document.getElementById("budgetDisplay");

slider.oninput = function() {
  display.innerText = `Budget: $${slider.value}`;
}

const btn = document.querySelector(".button");

btn.onclick = () => {
  window.location.href = "/climate.html";
}
