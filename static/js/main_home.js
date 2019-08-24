// Begin of the glider part
var myGlide = new Glide('.glide', {
    focusAt: 'center',
    startAt: 0,
    perView: 3,
    rewind: false,
    breakpoints: {
        1200: {
            perView: 2
        },
        700: {
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

        if (sectionPk == currentImg.getAttribute('data-pk')) {
            item.style.display = 'block'
        } else {
            item.style.display = 'none'
        }

    }

})

document.getElementById('rightArrow').addEventListener('click', function () {
    myGlide.go('>')
})
document.getElementById('leftArrow').addEventListener('click', function () {
    myGlide.go('<')
})


myGlide.mount()

// End of the glide part
