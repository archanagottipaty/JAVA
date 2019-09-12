const express = require("express");
const app = express();
app.set('view engine', 'ejs');
app.use(express.static(__dirname + "/static"));
app.get('/', (request, response) => {
res.render('index');
});

app.get('/cars', (request, res) => {
 res.render('cars');
});

app.get('/cats', (request, res) => {
   res.render('cats');
});

app.get('/cars/new', (request, res) => {
  res.render('form'); 
});
app.listen(8000, () => console.log("listening on port 8000"));


