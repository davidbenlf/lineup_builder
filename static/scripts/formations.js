import {getCookie} from './token.js'

function onDrag(event, element){
    const movementX = event.movementX
    const movementY = event.movementY
    const getStyle = window.getComputedStyle(element);
    console.log(getStyle.left)
    let leftVal = parseInt(getStyle.left);
    let topVal = parseInt(getStyle.top);
    element.style.left = `${leftVal + movementX}px`;
    element.style.top = `${topVal + movementY}px`;
}

const all_player_icon = document.querySelectorAll('div.player-icon')

// Make the DIV element draggable:
all_player_icon.forEach((element)=>{
    dragElement(element);
})


function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (elmnt) {
    // if present, the header is where you move the DIV from:
    elmnt.onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
}

function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    const y = elmnt.offsetTop - pos2
    const x = elmnt.offsetLeft - pos1

    const campo_el = document.querySelector('#campo')

    const style = getComputedStyle(campo_el)
    const campo_dimensions = {
        width: parseInt(style.width.replace('px', '')),
        height: parseInt(style.height.replace('px', ''))
    }

    const position = {
        y: [campo_el.getBoundingClientRect().top, (campo_el.getBoundingClientRect().top + campo_dimensions.height)],
        x: [campo_el.getBoundingClientRect().left, (campo_el.getBoundingClientRect().left + campo_dimensions.width)]
    }
    if(y > position['y'][0] && y < position['y'][1] - 60)
        elmnt.style.top = `${y}px`;
    if(x > position['x'][0] && x < position['x'][1] - 60)
        elmnt.style.left = `${x}px`;
}

function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
}
}



window.dragElement = dragElement