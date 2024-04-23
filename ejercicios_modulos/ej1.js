const {readFile} = require('fs')

readFile('./ejemplo.txt', 'utf-8', (err, texto) => {
    console.log(texto)
})



console.log('haz esto primero')