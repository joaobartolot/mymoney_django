var balance = document.getElementById('id_balance')
new Cleave(balance, {
    numeral: true,
    prefix: 'R$ ',
    numeralDecimalMark: ',',
    delimiter: '.',
})