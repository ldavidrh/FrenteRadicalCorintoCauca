const { Pool } = require('pg')

//Creating a new client and passing the URI

const pool = new Pool({
    connectionString : 'postgres://chifuavyjdteuw:da94215e492472b304f57fc7d63c2c06fe2d8fc3f2d4b53c048e745d3fe5c559@ec2-107-20-230-70.compute-1.amazonaws.com:5432/d5j8frme84avk6',
    ssl : true,
});


//Exporting the client as a module so it can be used in another file
module.exports = pool;