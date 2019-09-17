const express = require("express");
const app = express();
app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');
app.use(express.static(__dirname + "/static"));
const bodyparser = require("body-parser");
app.use(bodyparser.urlencoded());
const mongoose = require("mongoose");
//mongoose.connect('mongodb://localhost/name_of_your_DB', {useNewUrlParser: true});

mongoose.connect('mongodb://localhost/mongoquote', {useNewUrlParser: true});
const UserSchema = new mongoose.Schema({
name: String, quote: String});
const User = mongoose.model('User', UserSchema);



app.post('/quotes', (req, res)=> {
  console.log("Got this far", req.body);
  
  const user = new User();
  user.name = req.body.name;
  user.quote= req.body.quote;
  console.log("Got this far");
  console.log("This is a console message:", user.name);
  console.log("This is a console message:", user.age);
  user.save()
    .then(newUserData => console.log('user created: ', newUserData))
    .catch(err => console.log(err));
   
  res.redirect('/quotes');
});

app.get('/quotes', (req,res) => {

    User.find()
            .then(data => res.render("quotes", {users: data}))
            .catch(err => res.json(err));
});

app.get('/', (req, res) => {  
    
    res.render('index');
});

app.listen(8000, () => console.log("listening on port 8000"));