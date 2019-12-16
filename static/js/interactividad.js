const ipad = window.matchMedia('screen and (max-width: 767px)')
const menu = document.querySelector('.menu')
const burgerButton = document.querySelector('#burger-menu')
burgerButton.addEventListener('click', showHideMenu)

ipad.addListener(validation)

function validation(event) 
{
    if (event.matches) 
    {
        burgerButton.addEventListener('click', showHideMenu)
    }
    else
    {
        burgerButton.removeEventListener('click', showHideMenu)
    }
}

validation(ipad)

function showHideMenu()
{
    if (menu.classList.contains('is-active')) 
    {
        menu.classList.remove('is-active')
    } 
    else 
    {
        menu.classList.add('is-active')
    }
}