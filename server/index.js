const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

//middleware
app.use(cors());
app.use(bodyParser.json());
const posts = require('./routes/posts');
app.use('/', posts);
//middleware


const port = process.env.PORT || 4000;

app.listen(port, () =>{
    console.log('server started on port ' + port);
});


