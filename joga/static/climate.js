const buttons = document.querySelectorAll(".climate-button");
const selection = document.getElementById("selection");

buttons.forEach(button => {
  button.addEventListener("click", function() {
    const climate = this.dataset.climate;
    selection.textContent = `You selected ${climate} climate.`;
  });
});

const cold = document.querySelector(".cold");
const warm = document.querySelector(".warm");
const lukewarm = document.querySelector(".lukewarm");

cold.onclick = () => submit("cold");
warm.onclick = () => submit("warm");
lukewarm.onclick = () => submit("lukewarm");

function submit(temp) {
  if(temp == "warm") {
    localStorage.setItem("template", JSON.stringify({
      location: "RINCÓN, PUERTO RICO",
      budget: 100,
      activities: [
          { aname: "Getting ice, drinks, and snacks", cost: 24, date: Date.now() },
          { aname: "Getting gas", cost: 30, date: Date.now() },
          { aname: "Car toll payments", cost: 2, date: Date.now() },
          { aname: "Going to the beach", cost: 0, date: Date.now() },
          { aname: "Dinner after beach", cost: 19, date: Date.now() },
      ]
  }))
  }

  else {
    localStorage.setItem("template", JSON.stringify({
      location: "MIAMI, FLORIDA",
      budget: 3000,
      activities: [
          { aname: "Jet Blue tickets", cost: 700, date: Date.now() },
          { aname: "4-day Stay at Elser Hotel", cost: 660, date: Date.now() },
          { aname: "Car rental", cost: 600, date: Date.now() },
          { aname: "Disney tickets", cost: 300, date: Date.now() },
          { aname: "Food and souveniers", cost: 200, date: Date.now() },
      ]
    }))
  }

  window.location.href = "/preferences.html";
}