console.time('hola')
console.time('adios')

setTimeout(() => {
    console.log('hola')
    console.timeEnd('hola')
}, 100)

console.log('Yo no bloqueo')

setTimeout(() => {
    console.log('adios')
    console.timeEnd('adios')
}, 100)