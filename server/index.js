const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

//middleware
app.use(cors());
app.use(bodyParser.json());
const posts = require('./routes/posts');
app.use('/', posts);

//port
const port = process.env.PORT || 8000;

//Make the app listen through the selected port
app.listen(port, () =>{
    console.log('server started on port ' + port);
});


