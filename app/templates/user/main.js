const backgrounds = [
    "../assets/grass-luxury-beach-resort-travel.jpg", 
    "../assets/edit.jpg",
    "../assets/hotelbuild.jpg"
];

const texts = ["luxury", "Hotel", "luxury"];
const texts2 = ["HOTELS & RESORTS", "MASTER'S ROOMS", "LUXURY HOTELS"];

let currentIndex = 0;
// const background = document.querySelector(".hero-sect");
const background = document.querySelector("back-img");
const backgroundImg = document.getElementById("background-img");
const head = document.querySelector(".head");
const intro = document.querySelector(".intro");
const tagline = document.querySelector(".tagline");
const button = document.querySelector(".buton");

function changeBackground() {
           currentIndex = (currentIndex + 1) % backgrounds.length;
           backgroundImg.src = backgrounds[currentIndex];
           head.textContent = texts[currentIndex];
           intro.textContent = texts2[currentIndex];

            const animationClass = "head";
            head.classList.remove(animationClass);
            void head.offsetWidth; 
            head.classList.add(animationClass);

            const classname = "intro";
            intro.classList.remove(classname);
            void intro.offsetWidth; 
            intro.classList.add(classname);

            const tag = "tagline";
            tagline.classList.remove(tag);
            void tagline.offsetWidth; 
            tagline.classList.add(tag);
            
            const btn = "buton";
            button.classList.remove(btn);
            void button.offsetWidth; 
            button.classList.add(btn);

           
};

setInterval(changeBackground, 8000);


changeBackground();
console.log("hello")
