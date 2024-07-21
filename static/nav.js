document.querySelector("body").innerHTML += `<header class="header">
<div class="burgerBtn menuBtn">
    <div></div>
    <div></div>
    <div></div>
</div>

<h1 class="headerTitle"><p><img src="../assets/images/Have I Been Faked.png"></p> <p>Have I Been Faked</p></h1>

<img class="headerLogo" draggable="false" alt="" src="/shared../assets/toyfactory.png">
</header>

<section class="menuBackdrop">
<nav class="menu">
    <h2 class="menuTitle">Menu</h2>

    <ul class="menuLinks">
        <li><a href="/index.html">Home</a></li>
        <li><a href="/login.html">Login</a></li>
        <li><a href="/budget.html">Budget</a></li>
        <li><a href="/climate.html">Climate</a></li>
        <li><a href="/preferences.html">Modality</a></li>
        <li><a href="/chatbox.html">GOJA</a></li>
        <li><a href="/index.html">Log out</a></li>
        </li>
    </ul>

</nav>
</section>
`;

// Menu button
const menuBackdrop = document.querySelector(".menuBackdrop");
const burgerBtn = document.querySelector(".burgerBtn");
burgerBtn.onclick = () => {
    burgerBtn.classList.toggle("open");
    menuBackdrop.classList.toggle("open");
}

menuBackdrop.onclick = (e) => {
    if(e.target === menuBackdrop) {
        burgerBtn.classList.remove("open");
        menuBackdrop.classList.remove("open");
    }
}    

