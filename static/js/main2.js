const readMoreBtn = document.querySelector('.education');
const text = document.querySelector('.text');

readMoreBtn.addEventListener('click',(e)=>{
  text.classList.toggle('show-more');
  if(readMoreBtn.innerText === 'Read More'){
    readMoreBtn.innerText = 'Read Less';
  }else{
    readMoreBtn.innerText = 'Read More';
  }
})
