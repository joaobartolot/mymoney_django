window.addEventListener('load', function () {
    function hideLoad() {
        const loader = this.document.querySelector('.loader')
        loader.classList.add('hide')
    }

    setTimeout(hideLoad, 300)
})