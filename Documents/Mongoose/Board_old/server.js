const express = require("express");
const app = express();
app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');
app.use(express.static(__dirname + "/static"));
const bodyparser = require("body-parser");
app.use(bodyparser.urlencoded());
const mongoose = require("mongoose");
//mongoose.connect('mongodb://localhost/name_of_your_DB', {useNewUrlParser: true});

mongoose.connect('mongodb://localhost/dash', {useNewUrlParser: true});
// const RabbitSchema = new mongoose.Schema({
// name: String});
// const Rabbit = mongoose.model('Rabbit', RabbitSchema);

const CommentSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Posts must have a title"]},
         message: {type: mongoose.Schema.Types.ObjectId, required: [true, "Posts must have content"]},
    comment:{type: String, required: [true, "Posts must have content"]}
  }, {timestamps: true})

const MessageSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Posts must have a title"]},
     message: {type: String, required: [true, "Posts must have content"]},
     comments: [CommentSchema]
   }, {timestamps: true})
  
  const Message = mongoose.model('Message', MessageSchema);
  const Comment = mongoose.model('Comment', CommentSchema);

  


// app.get('/rabbits/new', (req,res) => {
//     res.render('new');
// });
// app.get('/rabbits/:id', (req, res) =>{
//     // ...retrieve an array of documents matching the query object criteria
//     Rabbit.findOne({_id:req.params.id}) 
//     .then(data => res.render("one", {rabbits: data}))
//     .catch(err => res.json(err));
//     console.log(req.params.id)
//         // logic with usersNamedJessica results 
// });
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
    console.log('Message created: ', newMessageData)
})   
    .catch(err => console.log(err));
});
 


app.get('/', (req,res) => {
    console.log("inside app.get");
    res.render('dash');
});


message.create(req.body, function(err, data){
     if(err){
          // handle the error from creating a blog
     }
     else {
          Message.findOneAndUpdate({_id: req.params.id}, {$push: {blogs: data}}, function(err, data){
               if(err){
                    // handle the error from trying to update the user
               }
               else {
                    // it worked! How shall we celebrate?
               }
          })
      }
})    


// app.get('/rabbits/edit/:id', (req,res) => {

//     res.render('edit',{rabbit_id:req.params.id});

// });

// app.post('/rabbits/:id', (req,res) => {
// // ...update 1 document that matches the query object criteria
// Rabbit.updateOne({_id:req.params.id}, {
//         name: req.body.name
//     })
//         .then(result => {
//         res.redirect('/rabbits/'+req.params.id)
//             // logic with result -- note this will be the original object by default!
//         })
//         .catch(err => res.json(err));
    
// });
// app.get('/rabbits/destroy/:id', (req,res) => {
// // ...delete 1 document that matches the query object criteria
// Rabbit.deleteOne({_id:req.params.id})
//     .then(deletedUser => {
//     res.redirect('/')
//         // logic (if any) with successfully removed deletedUser object
//     })
//     .catch(err => res.json(err));
// });

app.listen(8000, () => console.log("listening on port 8000"));