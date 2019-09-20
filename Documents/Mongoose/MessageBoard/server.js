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


app.post('/messages', (req,res) => {
    console.log("Got this far", req.body);
  
  const message = new Message();
  message.name = req.body.name;
  message.message = req.body.message;
  console.log("This is printing message name console :", message.name);
  console.log("This is printing message name console :", message.message);


  message.save()
    .then(newMessageData => {
          res.redirect('/');
          //console.log('Message saved: ', newMessageData)
})   
    .catch(err => console.log(err));
});


app.post('/comments/:id', (req,res) => {
const comment = new Comment();
  comment.name = req.body.name;
  comment.comment = req.body.comment;

  Message.findOne({_id:req.params.id})
         .then(result => {
           console.log("I am printing the result:", result);
           result.comments.push(comment);
           result.save()
               .then(()=> {
                    res.redirect('/');
               })
             // logic with result -- note this will be the original object by default!
         })
         .catch(err => res.json(err));   
 
  console.log("This is printing comment name console :", comment.name);
  console.log("This is printing comment name console :", comment.comment);
//   comment.save()
//     .then(newCommentData => {
//           res.redirect('/');
//           console.log('Comment saved: ', newCommentData)
// })   
//     .catch(err => console.log(err));
});

app.get('/', (req,res) => {
    Message.find()
     .then (allMessages =>{
           
          res.render('dash', { allmessages: allMessages});
})
.catch( err => console.log(err));
});
app.listen(8000, () => console.log("listening on port 8000"));