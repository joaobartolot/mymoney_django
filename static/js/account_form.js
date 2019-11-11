// Balance input auto-format
var balance = document.getElementById('id_balance')
new Cleave(balance, {
	numeral: true,
	prefix: 'R$ ',
	numeralDecimalMark: ',',
	delimiter: '.',
})


// Account types and card names or bank names
let accountTypes = document.getElementById('id_account_type')
let bankNames = document.getElementById('id_bank_name')
let cardNames = document.getElementById('id_card_name')

let divBankNames = document.getElementById('div_id_bank_name')
let divCardNames = document.getElementById('div_id_card_name')

function checkType(selectedType) {
	if (selectedType === '') {
		divCardNames.style.display = 'none'
		divBankNames.style.display = 'none'

	}

	if (selectedType === 'MV') {
		divCardNames.style.display = 'block'
		divBankNames.style.display = 'none'

		for (element of cardNames.options) {
			if (element.value.slice(-1) !== 'R') {
				element.style.display = 'none'
			} else {
				element.style.display = 'block'
			}
		}

	} else if (selectedType === 'FV') {
		divCardNames.style.display = 'block'
		divBankNames.style.display = 'none'

		for (element of cardNames.options) {
			if (element.value.slice(-1) !== 'A') {
				element.style.display = 'none'
			} else {
				element.style.display = 'block'
			}
		}

	} else if (selectedType === 'W') {
		divCardNames.style.display = 'none'
		divBankNames.style.display = 'none'

	} else if (selectedType === 'SL' || selectedType === 'SA' || selectedType === 'CA') {
		divCardNames.style.display = 'none'
		divBankNames.style.display = 'block'

	}
}

accountTypes.addEventListener('change', () => {
	let currentType = accountTypes.options[accountTypes.selectedIndex].value

	checkType(currentType)
})


// Form error messages
let nameInput = document.getElementById('id_name')
let submitButton = document.getElementById('submit_button')

nameInput.addEventListener('change', () => {
	nameInput.classList.remove('border-danger')

})

submitButton.addEventListener('click', () => {
	if (!nameInput.value) {
		nameInput.classList.add('border-danger')
	}
})