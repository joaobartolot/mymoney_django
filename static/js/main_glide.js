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