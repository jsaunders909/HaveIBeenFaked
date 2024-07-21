setInterval(() => {
    document.querySelector(".loadScreen").classList.add("hidden");
    
}, 0)


data = JSON.parse(localStorage.getItem("template"));
place = document.querySelector(".place");
actElem = document.querySelector(".activities");
activityAmt = document.querySelector(".activityAmt");

totalSpent = 0

data.activities.forEach(activity => {
    totalSpent += activity.cost

    actElem.innerHTML +=
    `
    <div class="activity">
        <div class="name">${activity.aname}</div>
        <div class="date">${new Date(activity.date).toLocaleDateString()} - ${new Date(activity.date).toLocaleTimeString()}</div>
        <div class="cost">${activity.cost}</div>
    </div>
    `
});


rinconImg = document.querySelector(".rincon");
disneyImg = document.querySelector(".disney");

rinconImg.classList.add("hidden")
disneyImg.classList.add("hidden")

if(data.location == "RINCÓN, PUERTO RICO") {
    rinconImg.classList.remove("hidden")
}else {
    disneyImg.classList.remove("hidden")
}


money = document.querySelector(".money");
left = document.querySelector(".left");
spent = document.querySelector(".spent");

place.innerText = data.location;
money.innerText = data.budget;
spent.innerText = totalSpent;
left.innerText = data.budget - totalSpent;
activityAmt.innerText = data.activities.length