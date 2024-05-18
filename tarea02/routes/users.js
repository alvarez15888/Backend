// Validate the data
if (data.title && data.singer && data.reproductions) {
    // If the data is valid, find the song with the given id in the songs array
    const song = songs.find((p) => p.id == id)

    // If the song exists, update its properties with the data
    if (song) {
      song.title = data.title
      song.singer = data.singer
      song.reproductions = data.reproductions

      // Send a 200 status code and the updated song as a JSON response
      res.status(200).json(song)
    } else {
      // If the song does not exist, send a 404 status code and a message
      res.status(404).send('Post not found')
    }
  } else {
     res.status(400).send('Invalid data')
}})