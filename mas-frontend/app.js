let express = require('express');
let path = require('path');
let request = require('request')
let port = 3000;

let indexRouter = require('./public/index');

let app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);

app.listen(port, ()=>{
  console.log(`frontend server on port ${port}`)
})

module.exports = app;