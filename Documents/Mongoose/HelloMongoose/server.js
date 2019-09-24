
const express = require("express");
const app = express();
app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');
app.use(express.static(__dirname + "/static"));
const mongoose = require("mongoose");
//mongoose.connect('mongodb://localhost/name_of_your_DB', {useNewUrlParser: true});

mongoose.connect('mongodb://localhost/mongotest', {useNewUrlParser: true});
const UserSchema = new mongoose.Schema({
name: String, age: Number});
const User = mongoose.model('User', UserSchema);



app.post('/users', (req, res)=> {
  console.log("Got this far");
  const user = new User();
  user.name = req.body.name;
  user.age = req.body.age;
  console.log("Got this far");
  console.log("This is a console message:", user.name);
  console.log("This is a console message:", user.age);
  user.save()
    .then(newUserData => console.log('user created: ', newUserData))
    .catch(err => console.log(err));
   
  res.redirect('/');
});
app.get('/', (req, res) => {  
    User.find()
        .then(data => res.render("index", {users: data}))
        .catch(err => res.json(err));
    //res.render('index');
});

app.listen(8000, () => console.log("listening on port 8000"));
