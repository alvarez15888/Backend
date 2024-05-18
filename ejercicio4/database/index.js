const mongoose = require('mongoose')

mongoose.connect('mongodb://127.0.0.1:27017/mydb')
.then(() => console.log('La conexion ha sido exitosa'))
.catch((err) => console.log(err))