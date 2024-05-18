const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/ejercicio2')
.then(() => console.log('Conectado a la base'))
.catch(err => console.error('MongoDB connection error:', err));