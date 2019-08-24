var balance = document.getElementById('id_balance')
new Cleave(balance, {
    numeral: true,
    prefix: 'R$ ',
    numeralDecimalMark: ',',
    delimiter: '.',
})

let accountTypes = document.getElementById('id_account_type')
for (elements in accountTypes) {
	console.log(elements)
}
