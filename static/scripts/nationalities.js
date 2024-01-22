import {getCookie} from './token.js'

const imgInput = document.querySelector('input#id_img')
const image = document.querySelector('img#nationality-pic');
imgInput.addEventListener('change', (event)=>{
    if(event.target.files[0])
	    image.src = URL.createObjectURL(event.target.files[0]);
    else
        image.src = "/static/img/default-nationality.webp"
})
image.addEventListener('click', ()=>{
    imgInput.click()
})

async function update_nationality(e, url, el){
    e.preventDefault();
    const id = el.getAttribute('data-id')
    const nome = document.querySelector(`form#nationality-edit-${id} > input.edit-nationality-name`).value
    const image = document.querySelector(`form#nationality-edit-${id} > input.edit-nationality-img`).files[0]
    const formData = new FormData()
    formData.append('nome', nome)
    formData.append('id', id)
    if(image)
        formData.append('img', image)
    const options = {
        method: 'POST',
        headers: {
            "X-CSRFToken": getCookie("csrftoken")},
        body: formData
    }
    const response = await fetch(url, options).then((response) => {
        return response.json(); //converts response to json
     })
     .then((data) => {
         console.log(data)
         const parent = document.querySelector(`li#nationality-${id}`)
         toggle_edit(parent)
         const new_img = parent.querySelector('div.nationality-info > img')
         if(image)
            new_img.src = URL.createObjectURL(image);
         const new_name = parent.querySelector('div.nationality-info > span')
         new_name.innerHTML = nome
      //Perform actions with the response data from the view
     });
}

function update_edit_img(parent, el){
    const image = parent.querySelector('img.edit_img')
    if(el.files[0])
	    image.src = URL.createObjectURL(el.files[0]);
    else
        image.src = "/static/img/default-nationality.webp"
}

function toggle_edit(parent){
    const div_array = parent.querySelectorAll('div')
    div_array.forEach(element => {
        element.classList.toggle('d-none')
    });
    const edit_section = parent.querySelector('section')
    edit_section.classList.toggle('d-none')
}

window.update_nationality = update_nationality;
window.update_edit_img = update_edit_img;
window.toggle_edit = toggle_edit;