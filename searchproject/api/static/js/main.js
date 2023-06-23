//add to fav
const heart = document.querySelector('.heart');
let heartUnactive = true;

//counter
const minus = document.querySelector('.minus');
const plus = document.querySelector('.plus');
const display = document.querySelector('.display');
const digit = document.querySelector('.digit')

let currentvalue = 1;


function handlePlusClick(){
    minus.classList.remove('gray');
    currentvalue++;
    digit.innerText = currentvalue;

}

function handleMinusClick(){
    if(currentvalue <= 1){
        minus.classList.add('gray');
    }

    else if(currentvalue > 1){
        minus.classList.remove('gray');
        currentvalue--;
        digit.innerText = currentvalue;
    }
}








function handleHeartClick(){
    if(heartUnactive){
        heart.style.backgroundImage = 'url("../static/images/hearUnactive.svg")';
        heart.style.transform = 'scale(1)';
        heartUnactive = false;
    }

    else if(heartUnactive === false){
        heart.style.backgroundImage = 'url("../static/images/heartActive.png")';
        heart.style.transform = 'scale(1.08)';
        heartUnactive = true;
    }

}

heart.addEventListener('click', handleHeartClick);

plus.addEventListener('click', handlePlusClick);
minus.addEventListener('click', handleMinusClick);