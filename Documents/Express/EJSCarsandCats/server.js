const express = require("express");
const app = express();
app.set('view engine', 'ejs');
app.use(express.static(__dirname + "/static"));
app.get('/', (request, res) => {
res.render('index');
});
app.get('/cats', (request, res) => {
   res.render('cats');
});

app.get('/cuddles', (request,res) => {
 var cat_array = [
        {picture: "cat.jpg",favfood: "Tuna", age:3, sleepingspots:" under the bed"} 
    ];
	res.render('cuddles',{cuddles: cat_array});
});
app.get('/cuddles1', (request,res) => {
        res.render('cuddles');
});
app.get('/cuddles2', (request,res) => {
        res.render('cuddles');
});
app.listen(8000, () => console.log("listening on port 8000"));


