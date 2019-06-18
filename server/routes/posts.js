const express = require('express');
const pg = require('pg');
//Connection to database
const { Pool, Client } = require('pg');

const router = express.Router()

//Get
router.get('/', (req, res) =>{
    res.send('Get request');
});

//Post
router.post('/', (req, res) =>{
    res.send('Post request');
});

//Put
router.put('/', (req, res)=>{
    res.send('Put request');
})

//Delete
router.delete('/', (req, res)=>{
    res.send('Delete request');
});


module.exports = router;