console.time('hola')
console.time('bucle')

setTimeout(() => {
    console.log('hola')
    console.timeEnd('hola')
}, 105)

let i = 0
setTimeout(() => {
    console.log('En bucle')
    console.timeEnd('bucle')
    while(true) {
        if (i > 1000000000) {
            break
        }
        i++
    }
}, 100)