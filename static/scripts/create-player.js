import {getCookie} from './token.js'

const imgInput = document.querySelector('#id_img')
const image = document.querySelector('#new-player-pic');
imgInput.addEventListener('change', (event)=>{
    if(event.target.files[0])
	    image.src = URL.createObjectURL(event.target.files[0]);
    else
        image.src = "/static/img/default_pfp.webp"
})
image.addEventListener('click', ()=>{
    imgInput.click()
})

function toggle_edit(el){
    const id = el.getAttribute('data-id')
    const parent = document.querySelector(`li#player-${id}`)
    const div_array = parent.querySelectorAll('div.player-info, div.player-icons')
    div_array.forEach(element => {
        element.classList.toggle('d-none')
    });
    const edit_section = parent.querySelector('section')
    edit_section.classList.toggle('d-none')
}

async function update_jogador(e, url, el){
    e.preventDefault();
    const id = el.getAttribute('data-id')
    const nome = document.querySelector(`section.player-edit[data-id="${id}"] > input.edit-player-name`).value
    const image = document.querySelector(`section.player-edit[data-id="${id}"] > input.edit-player-img`).files[0]
    const time = document.querySelector(`section.player-edit[data-id="${id}"] select.edit-player-time`).value
    const nacionalidade = document.querySelector(`section.player-edit[data-id="${id}"] select.edit-player-nationality`).value

    const formData = new FormData()
    formData.append('id', id)
    formData.append('nome', nome)
    formData.append('time', time)
    formData.append('nacionalidade', nacionalidade)
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
        const parent = document.querySelector(`li#player-${id}`)
        toggle_edit(parent)
        const new_img = parent.querySelector('div.player-info > img')
        if(image)
           new_img.src = URL.createObjectURL(image);
        const new_name = parent.querySelector('div.player-info > span')
        new_name.innerHTML = nome

        const nationality_img = parent.querySelector('div.player-icons > img.player-nationality')
        nationality_img.src = `../${data.nacionalidade_img.replace(/['"]+/g, '')}`

        const time_img = parent.querySelector('div.player-icons > img.player-club')
        time_img.src = `../${data.time_img.replace(/['"]+/g, '')}`
      //Perform actions with the response data from the view
     });
}

function update_edit_img(el){
    const image = el.parentNode.querySelector('img.player-edit-pic')
    if(el.files[0])
	    image.src = URL.createObjectURL(el.files[0]);
    else
        image.src = "/static/img/default_pfp.webp"
}

async function search_player(){
    const term = document.querySelector('input#search-player').value
    const url = `search/${term}/`
    if(!term)
        return
    const options = {
        method: 'GET',
        headers: {
            "X-CSRFToken": getCookie("csrftoken")},
    }
    const response = await fetch(url, options).then((response) => {
        return response.json(); //converts response to json
     })
     .then((data) => {
        console.log(data)
        
     });
}

window.update_jogador = update_jogador
window.toggle_edit = toggle_edit
window.update_edit_img = update_edit_img
window.search_player = search_player