const express = require("express");
const app = express();
app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');
app.use(express.static(__dirname + "/static"));
const bodyparser = require("body-parser");
app.use(bodyparser.urlencoded());
const mongoose = require("mongoose");

mongoose.connect('mongodb://localhost/dash', {useNewUrlParser: true});

const CommentSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Posts must have a title"]},
        // message: {type: mongoose.Schema.Types.ObjectId, required: [true, "Posts must have content"]},
    comment:{type: String, required: [true, "Posts must have content"]}
  }, {timestamps: true})

const MessageSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Posts must have a title"]},
     message: {type: String, required: [true, "Posts must have content"]},
     comments: [CommentSchema]
   }, {timestamps: true})
  const Message = mongoose.model('Message', MessageSchema);
  const Comment = mongoose.model('Comment', CommentSchema);

app.listen(8000, () => console.log("listening on port 8000"));