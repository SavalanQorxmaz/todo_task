

export async function getScreenSize(){
    const screen = document.documentElement.offsetWidth
    switch(true){
        case 0 < screen && screen <= 600:{
            document.querySelector('input[name="screen"]').value = 'mobile'
        }
        break
        case 600 < screen && screen <= 992:{
            document.querySelector('input[name="screen"]').value = 'tablet'
        }
        break
        // case 992 < screen: {
        //     document.querySelector('input[name="screen"]').value = 'desktop'
        // }
        // break
        default: document.querySelector('input[name="screen"]').value = 'desktop'

    }
    return document.querySelector('input[name="screen"]').value
}

export async function  checkContainer(getScreen){
    if (document.querySelector('#container')){
        const container = document.querySelector('#container')
        const screen = await getScreen()
        switch(screen){
            case 'mobile':{
                container.classList = ''
                container.classList.add('container-mobile')
            }
            break
            case 'tablet':{
                container.classList = ''
                container.classList.add('container-tablet')
            }
            break
            default: {
                container.classList = ''
                container.classList.add('container-desktop')
            }
        }
        return screen

    }

}

addEventListener('load', () => {
    const screen = checkContainer(getScreenSize)
})

addEventListener('resize', ()=>{
    const screen = checkContainer(getScreenSize)
})


