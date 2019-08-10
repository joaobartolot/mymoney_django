// Begin of the glider part
var myGlide = new Glide('.glide', {
    focusAt: 'center',
    startAt: 0,
    perView: 3,
    rewind: false,
    breakpoints: {
        1024: {
            focusAt: 'center',
            perView: 2
        },
        800: {
            focusAt: 'center',
            perView: 2
        },
        700: {
            focusAt: 'center',
            perView: 1
        },
        600: {
            focusAt: 'center',
            perView: 1
        }
    }
})

myGlide.on('move.after', function () {
    var btnLeft = document.getElementById('leftArrow')
    var btnRight = document.getElementById('rightArrow')

    var currentSlide = document.getElementsByClassName('glide__slide')[myGlide.index]
    var currentImg = currentSlide.getElementsByTagName('img')[0]




    var accountInfo = document.getElementsByClassName('account_info')
    for (var item of accountInfo) {
        var sectionPk = item.getAttribute('data-pk')

        if (sectionPk === currentImg.getAttribute('data-pk')) {
            item.style.display = 'block'
        } else {
            item.style.display = 'none'
        }

    }



    // if (currentImg.alt === 'nuCard') {
    //     document.getElementById('card-names').innerHTML = 'Nu Bank Card Selected'
    // }
    // if (currentImg.alt === 'ticketCard') {
    //     document.getElementById('card-names').innerHTML = 'Ticket Card Selected'
    // }
    // if (currentImg.alt === 'santanderCard') {
    //     document.getElementById('card-names').innerHTML = 'Santander Card Selected'
    // }

    // console.log();


})

document.getElementById('rightArrow').addEventListener('click', function () {
    myGlide.go('>')
})
document.getElementById('leftArrow').addEventListener('click', function () {
    myGlide.go('<')
})


myGlide.mount()

// End of the glide part

// Info toggle

var toggleBtn = document.getElementById('toggler')
var collapseDiv = document.getElementById('infoCollapse')
var infoCaret = document.getElementById('caretIcon')

toggleBtn.addEventListener('click', function () {
    collapseDiv.classList.toggle('show')
    if (infoCaret.classList[infoCaret.classList.length - 1] === 'down') {
        infoCaret.classList.remove('down')
        infoCaret.classList.add('up')
    }
    else if (infoCaret.classList[infoCaret.classList.length - 1] === 'up') {
        infoCaret.classList.remove('up')
        infoCaret.classList.add('down')

    }
    else {
        infoCaret.classList.add('up')
    }
})