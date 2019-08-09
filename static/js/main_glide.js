document.getElementById('glide')
var myGlide = new Glide('.glide', {
    focusAt: 'center',
    startAt: 1,
    perView: 3,
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
    console.log($('.glide__slides')[myGlide.index])
})

document.getElementById('rightArrow').addEventListener('click', function () {
    myGlide.go('>')
})
document.getElementById('leftArrow').addEventListener('click', function () {
    myGlide.go('<')
})


myGlide.mount()