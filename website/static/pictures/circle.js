const angletoradian = (angle) =>{
    return angle * (Math.PI / 180);
};

const radius = 100;
const diameter = radius*2;
const circle = document.querySelector('#rounded');
circle.style.width = `${diameter}px`;
circle.style.height = `${diameter}px`;

const text = circle.innerText;
const character = text.split('');
circle.innerText = null;

let angle = -90;

const deltaangle = 360/character.length;

character.forEach((char, index) =>{
    const charelement = document.createElement('span');
    charelement.innerText = char;
    const xpos = radius * Math.cos(angletoradian(angle));
    const ypos = radius * Math.sin(angletoradian(angle));

    const transform = `translate(${xpos}px, ${ypos}px)`;
    const rotate = `rotate(${index * deltaangle}deg)`;
    charelement.style.transform = `${transform} ${rotate}`;

    angle += deltaangle;
    circle.appendChild(charelement);


})