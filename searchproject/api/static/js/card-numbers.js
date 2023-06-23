const CVV = document.querySelector('#CVV');
const CVVWrapper = document.querySelector('.cvv-wrapper');
const CVVLabel = document.querySelector('#cvv-label');
const cardNumbers = document.querySelector('#card-numbers');
const numbersWrapper = document.querySelector('.numbers');
const numbersLabel = document.querySelector('#numbers-label');
const submit = document.querySelector('#submit')
const link = document.querySelector('.link')
let validcvv = false;
let validnumer = false;



CVV.addEventListener('keyup', handleEnteringCVV)

cardNumbers.addEventListener('keyup', handleEnteringNumbers)

submit.addEventListener('keyup', isAllValid)



function handleEnteringCVV(){
    if(CVV.value.length == 3 && !isNaN(CVV) && parseInt(CVV)){
        CVV.classList.remove('border-highlight');
        CVVLabel.classList.remove('label-highlight');
        validcvv = true;
    }

    else if(CVV.value.length != 3 && !isNaN(CVV) == false && parseInt(CVV) == false){
        CVV.classList.add('border-highlight');
        CVVLabel.classList.add('label-highlight');
        validcvv = false;
    }
}


function handleEnteringNumbers(){
    if(cardNumbers.value.length == 16 && !isNaN(Number) && parseInt(Number)){
        cardNumbers.classList.remove('border-highlight');
        numbersLabel.classList.remove('label-highlight');
        validnumer = true;
    }

    else if(cardNumbers.value.length != 16  && !isNaN(Number) == false && parseInt(Number) == false){
        cardNumbers.classList.add('border-highlight');
        numbersLabel.classList.add('label-highlight');
        validnumer = false;
    }
}

function isAllValid() {
    if (validcvv && validnumer) {
      submit.removeAttribute('disabled');
      link.removeAttribute('href'); 
    } else {
      submit.setAttribute('disabled', '');
      link.setAttribute('href', '../thank-you');
    }
  }