require('./server/config/routes.js')(app);
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





app.listen(8000, () => console.log("listening on port 8000"));