const {Router} = require('express')
const cookieParser = require('cookie-parser')
const session = require('express-session')
const router = Router()

// habilitar el cookieParser
router.use(cookieParser())
router.use(session({
    secret: 'secret_word',
    resave: false,
    saveUninitialized: false
}))

// I try anytimes install and run mongodb but nothing that's why I created a simple data model
// Define the data
const songs = [
    {
        id:1, title:'Million Dollar Baby', singer:'Tommy Richman', reproductions:82235497
    },
    {
        id:2, title:'Not Like Us', singer:'Kendrick Lamar', reproductions:73078518
    },
    {
        id:3,
        title:'Fortnight(ft. Post MAlone)',
        singer:'Taylor Swift',
        reproductions:46079957
    },
    {
        id:4,
        title:'Too Sweet',
        singer:'Hozier',
        reproductions:42925136
    },
]

// Create a route and a handler for GET
router.get('/', (req, res, next) => {
  console.log('Esto es antes del procesado')
  next()
}, (req, res, next) => {

  const { Top10 } = req.query
  res.cookie('visited', true,{
      maxAge: 50000
  })

  if (Top10 && !isNaN(Top10)){
      const filteredSongs = songs.filter((s) => s.reproductions >= Top10)
      res.status(200).send({
          filteredSongs
      })
  }else{

  res.status(200).send({
      songs
  })
}
  next()
},
() => {
  console.log('El preceso ha terminado')
}
)

// Create a route and a handler for POST
router.post('/:id', (req,res) => {
  console.log(req.cookies)
  const { id } = req.params
  const { title, singer, reproductions } = req.body
  const data = songs.map((song) => song.id)

  if (data.includes(id)) {
      res.status(418).send({
          message: 'Already have a song in this id'
      })
  }
  else{
      songs.push({
          id: id,
          title: title,
          singer: singer,
          reproductions: reproductions
      })
      res.send({
          message: `Song added ${id}`
      })
  }
})

// Create a route and a handler for PATCH
router.patch('/:id', (req,res) => {
  const { id } = req.params
  const { title, singer, reproductions } = req.body
  const data = songs.find((i) => i.id === id)

  if (title) {data.title = title}
  if (singer) {data.singer = singer}
  if (reproductions) {data.reproductions = reproductions}
  
  res.send(`Song with id ${id} has been updated`)
})


// Create a route and a handler for DELETE
router.delete('/:id', (req,res) => {

  const { id } = req.params
  const response = songs.delete(id)
  // songs = songs.filter((song) => song.id !== id)
  res.send(`Song with the id ${id} deleted from the database.`)

})




module.exports = router