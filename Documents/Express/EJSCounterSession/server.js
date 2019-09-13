const express = require("express");
const app = express();
const session = require('express-session');
app.use(session({
  secret: 'keyboardkitteh',
  resave: false,
  saveUninitialized: true,
  cookie: { maxAge: 60000 }
}))

app.set('view engine', 'ejs');

app.set('views', __dirname + '/views');
app.use(express.static(__dirname + "/static"));

app.get('/', (request, response) => {
   if (request.session.counter){ 
	
   	request.session.counter += 1;}
   else 
{	request.session.counter = 1;}
//   res.render('cuddles',{cuddles: cat_array});
   response.render('index', {counter: request.session.counter});
});

app.post('/plustwo', (request,response) => {
 if (request.session.counter){

        request.session.counter += 2;}
   else
{       request.session.counter =2;}
response.render('index', {counter: request.session.counter});
});

app.post('/reset', (request,response) => {
 if (!request.session.counter) {
	request.session.counter = 0; }
else request.session.counter = 0;
response.render('index', {counter: request.session.counter});
});
app.listen(8000, () => console.log("listening on port 8000"));

