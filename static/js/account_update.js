var balance = document.getElementById('id_balance')
new Cleave(balance, {
    numeral: true,
    prefix: 'R$ ',
    numeralDecimalMark: ',',
    delimiter: '.',
})

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

function adjustingDots(balance) {
    let balanceArray = []

    for (letter of balance.value.slice(3, -2)) {
        balanceArray.push(letter)
    }

    for (let i = 0; i < balanceArray.length; i++) {
        if (balanceArray[i] == '.') {
            let tempDot = balanceArray[i]
            let temp2 = balanceArray[i - 2]

            balanceArray[i] = balanceArray[i - 1]
            balanceArray[i - 1] = temp2
            balanceArray[i - 2] = tempDot
        }
    }

    if (balanceArray[0] == '.') {
        balanceArray.shift()
    }

    if (balanceArray.length != 0) {
        return `R$ ${balanceArray.join('')},${balance.value.slice(-2)}`
    } else {
        return 'R$ 0,00'
    }
}

balance.value = adjustingDots(balance)


if (bankNames.value !== '') {
    divBankNames.style.display = 'block'
}

if (cardNames.value !== '') {
    divCardNames.style.display = 'block'
}
