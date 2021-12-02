'use strict'

import Modal from '../script/classes/Modal.js';

function createModalWindow(event) {
    event.preventDefault();

    const modalWindow = new Modal();
    modalWindow.beforeMount();
}

const btnSingUp = document.querySelector('.btn-signUp');
if (btnSingUp) {
    btnSingUp.addEventListener('click', createModalWindow);
}

const btnSingUpIndex = document.querySelector('.btn.btn-primary.link');
if (btnSingUpIndex) {
    btnSingUpIndex.addEventListener('click', createModalWindow);
}

