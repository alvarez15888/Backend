// Import the express module
const express=require('express')
const userRoute = require('./routes/users_')

// Create an instance of the express application
const app = express()

// MongoDB - doesn't work
//require('./database')

// response format
app.use(express.json())
// use Routes
app.use('/api/songs', userRoute)

// Specify a port number for the server
const port=8080


// Start the server and listen to the port
app.listen(port, 
    () => { console.log(`Server is running on http://localhost:${port}`);
})

