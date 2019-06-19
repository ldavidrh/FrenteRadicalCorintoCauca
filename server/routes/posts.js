const express = require('express');
const client = require('../conn/connection.js')

//Connecting with the imported client
client.connect();

//Router
const router = express.Router()

//Get
router.get('/products', (req, res) => {
   let data;
    client.query('SELECT * FROM products;', (err, response)=>{
        res.send(response.rows);
        client.end();
    });
});

//Post
router.post('/', (req, res) => {
    res.send('Post request');
});

//Put
router.put('/', (req, res) => {
    res.send('Put request');
})

//Delete
router.delete('/', (req, res) => {
    res.send('Delete request');
});

module.exports = router;