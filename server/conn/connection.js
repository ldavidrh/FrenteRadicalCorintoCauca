const { Client } = require('pg')

//Data necessary to connect to de database
const connectionData = {
    user : 'luis',
    host : 'localhost',
    database : 'madlab',
    password : 'ldavidrh',
    port : 5432
};

//Creating a new client and passing the connection data
const client = new Client(connectionData);


//Exporting the client as a module so it can be used in another file
module.exports = client;