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

const users = [
    {username: 'Antonio',
        age:34
    },
    {username: 'Jose',
        age:7
    },
    {username: 'Maria',
        age:89
    },
]

router.get('/', (req, res, next) => {
    console.log('Esto es antes del procesado')
    next()
}, (req, res, next) => {

    const { minAge } = req.query
    res.cookie('visited', true,{
        maxAge: 50000
    })

    if (minAge && !isNaN(minAge)){
        const filteredUsers = users.filter((u) => u.age >= minAge)
        res.status(200).send({
            filteredUsers
        })
    }else{

    res.status(200).send({
        users
    })
}
    next()
},
() => {
    console.log('El preceso ha terminado')
}
)

router.post('/:username', (req,res) => {
    console.log(req.cookies)
    const {username} = req.params
    const {age} = req.body
    const usernames = users.map((user) => user.username)

    if (usernames.includes(username)) {
        res.status(418).send({
            message: 'Este nombre ya existe'
        })
    }
    else{
        users.push({
            username: username,
            age: age
        })
        res.send({
            message: `Añadido el usuario ${username}`
        })
    }
})

router.post('/friends/user', (req, res) => {
    const { username } = req.body
    const { friends } = req.session
    if(friends){
        req.session.friends.users.push(username)
    }else{
        req.session.friends = {
            users:[username]
        }
    }
    res.send(201)
})

router.get('/friends', (req, res) => {
    const {friends} = req.session
    if(!friends){
        res.send('No tienes amigos')
    }else{
        res.send(friends)
    }
})

module.exports = router