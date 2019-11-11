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
    var currentSlide = document.getElementsByClassName('glide__slide')[myGlide.index]
    var currentImg = currentSlide.getElementsByTagName('img')[0]


    var accountInfo = document.getElementsByClassName('account_info')

	// Display current account selected information
    for (var item of accountInfo) {
        var sectionPk = item.getAttribute('data-pk')

        if (sectionPk == currentImg.getAttribute('data-pk')) {
            item.style.display = 'block'
        } else {
            item.style.display = 'none'
        }
    }

	let dot = document.querySelectorAll('.dot')

	dot.forEach((element, index) => {
		console.log(myGlide.index)
		if (index === myGlide.index) {
			dot[index].classList.add('active')
		} else {
			dot[index].classList.remove('active')
		}

	})


})

document.getElementById('rightArrow').addEventListener('click', function () {
    myGlide.go('>')
})
document.getElementById('leftArrow').addEventListener('click', function () {
    myGlide.go('<')
})


let dots = document.querySelectorAll('.dot')
let activeButton = document.querySelector('.active')

dots.forEach((element, index) => {
  
  element.addEventListener('click', () => {
    console.log(activeButton)
    if (activeButton) {
      activeButton.classList.remove('active')
    }
    
    element.classList.add('active')
    activeButton = element

		myGlide.go('=' + index)
  })
})

myGlide.mount()

// End of the glide part
