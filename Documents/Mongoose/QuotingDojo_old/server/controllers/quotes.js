// All necessary requires, such as the Quote model.
module.exports = {
    index: function(req, res) {
    	// code...
    },
    create: function(req, res) {
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
      //res.render('users', {users: users_array});
        res.redirect('/quotes');
    },
    destroy: function(req, res) {
    	// code...
    },

    update: function(req,res){


    },

    show: function(req,res){

        
    }
};



