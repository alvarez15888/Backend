const http = require('http')
const fs = require('fs')

const fetchPokedexData = async () => {
    return new Promise((resolve, reject) => {
        fs.readFile('./pokedex.json', 'utf-8', (err, data) => {
            if(err) {
                reject(err)
            }else{
                resolve(JSON.parse(data));
            }
        });
    });
};

const handleRequest = async( req, res ) => {
    const pokedexData = await fetchPokedexData()
    const pokeName = decodeURI(req.url.substring(1))

    const pokeData = pokedexData.find(
        pokemon => pokemon.name.english === pokeName || pokemon.id === parseInt(pokeName) || pokemon.name.japanese === pokeName || 
        pokemon.name.chinese === pokeName || pokemon.name.french === pokeName
    )
    

    if (pokeData) {
        const response = {
            'Name': pokeData.name.english,
            'Type': pokeData.type,
            'Base': pokeData.base
        }
        res.writeHead(200, {'Content-Type': 'application/json'})
        res.end(JSON.stringify(response, null, 4))
    }else{
        res.writeHead(404, {'Content-Type': 'text/plain'});
        res.end('Pokémon no encontrado');   
    }

server.listen(3000, () => {
    console.log('Servidor iniciado en el puerto 3000');
});

};

const server = http.createServer(handleRequest)
server.listen(3000, () => {
    console.log('Escuchando el 3000')
})