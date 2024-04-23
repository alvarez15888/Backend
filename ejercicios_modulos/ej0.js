const {readFileSync} = require('fs')

const texto = readFileSync('./ejemplo.txt', 'utf-8')

console.log(texto)

console.log('"haz esto primero')