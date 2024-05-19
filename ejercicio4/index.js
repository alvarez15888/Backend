// inicializar 
const express = require('express')
const userRoute = require('./routes/users')

const app = express()

const PORT = 8000


// require('./database')
app.use(express.json())

app.use('/api/users',userRoute)

app.listen(
    PORT,
    () => console.log(`Estoy en http://localhost:${PORT}`)
)