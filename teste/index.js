const express = require('express')
const app = express()
const mongoose = require('mongoose')

require('./database')

app.use(express.json())

const tareasSchema = new mongoose.Schema({
    titulo: {type: String, required: true},
    description: {type: String},
    status: {type: String, required: true, default: 'to-do'},


})

const Tarea = mongoose.model('Tarea', tareasSchema)

app.post('/tareas', async (req, res) => {
    try {
        const tarea = new Tarea(req.body)
        await tarea.save()
        res.status(201).json(tarea);
    } catch(error) {
        res.status(400).json({error: error.message})
    }
});

app.get('/tarea', async (req,res) => {
    try {
        const tareas = await Tarea.find()
        res.json(tareas)
    }catch (error){
        res.status(500).send({error: error.message})
    }
});

app.listen(3001, () => {
    console.log('Servidor Escuchando')
})