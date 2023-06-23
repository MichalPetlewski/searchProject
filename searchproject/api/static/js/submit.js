const barWrapper = document.querySelectorAll('.bar-wrapper');
console.log('hello')




function autoSubmit(){
    const categoryForm = document.querySelector('.category-form')
    for(const bar of barWrapper){
        bar.addEventListener('click', function(){
            console.log('it worked!')
            categoryForm.submit()
        });
    };
};


autoSubmit();