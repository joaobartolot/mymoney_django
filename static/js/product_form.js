var balance = document.getElementById('id_price')
new Cleave(balance, {
    numeral: true,
    prefix: 'R$ ',
    numeralDecimalMark: ',',
    delimiter: '.',
})