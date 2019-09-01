var balance = document.getElementById('id_balance')
new Cleave(balance, {
    numeral: true,
    prefix: 'R$ ',
    numeralDecimalMark: ',',
    delimiter: '.',
})

let accountTypes = document.getElementById('id_account_type')
let bankNames = document.getElementById('id_bank_name')

function checkType(selectedType) {
    if (selectedType === 'MV') {
        for (let element of bankNames.options) {
            if (element.value !== '' && element.value !== 'MV') {
                element.style.display = 'none'
            } else {

                element.style.display = 'block'
            }
        }
    } else if (selectedType === 'FV') {
        for (let element of bankNames.options) {
            if (element.value !== '' && element.value !== 'FV') {
                element.style.display = 'none'
            } else {

                element.style.display = 'block'
            }
        }
    } else if (selectedType === 'W') {
        for (let element of bankNames.options) {
            element.style.display = 'none'
        }
    } else if (selectedType === 'CA') {
        for (let element of bankNames.options) {
            if (element.value !== '' && element.value === 'MV' || element.value === 'FV' || element.value === 'NU') {
                element.style.display = 'none'
            } else {

                element.style.display = 'block'
            }
        }
    } else if (selectedType === 'SL' || selectedType === 'SA') {
        for (let element of bankNames.options) {
            if (element.value !== '' && element.value === 'MV' || element.value === 'FV') {
                element.style.display = 'none'
            } else {

                element.style.display = 'block'
            }
        }
    }
}

accountTypes.addEventListener('change', () => {
    let currentType = accountTypes.options[accountTypes.selectedIndex].value

    if (currentType !== 'W') {
        if (bankNames.disabled) {
            bankNames.disabled = false
        }
        bankNames.selectedIndex = 0
        checkType(currentType)
    }
    else {
        bankNames.selectedIndex = 0
        bankNames.disabled = true
    }
})

console.log(balance.value.length)
console.log(balance.value.slice(2, -2).length)
// balance.value = 'R$ '
// check the size of the splice until the last two digits
// if it is greater than 3:
// shift the "." to the left by 2
// else:
// delete the "."


function adjustingDots(balance) {
	let balanceArray = []

	for (letter of balance.value.slice(3, -2)) {
		balanceArray.push(letter)
	}

	for (let i = 0; i < balanceArray.length; i++) {
		if (balanceArray[i] == '.') {
			let temp = balanceArray[i]
			balanceArray[i] = balanceArray[i-1]

		}
	}

}
