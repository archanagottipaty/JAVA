const http = require('http');
const fs = require('fs');
const server = http.createServer((request, response) => {
    if(request.url === '/cars') {
        fs.readFile('cars.html', 'utf8', (errors, contents) => {
            response.writeHead(200, {'Content-Type': 'text/html'});
            console.log(contents);
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/images/cars2.jpg') {
        fs.readFile('./images/cars2.jpg', function(errors, contents){
            response.writeHead(200, {'Content-Type': 'image/jpg'});
            console.log("Iam printing images:");
            console.log(contents);
            response.write(contents);
            response.end();
        }); 
    }

    
    else if(request.url === '/images/cars3.jpg') {
        fs.readFile('./images/cars3.jpg', function(errors, contents) {
            response.writeHead(200, {'Content-Type': 'image/jpg'});
            response.write(contents); 
            response.end();
        }); 
    }
    else if(request.url === '/images/tesla.jpg') {
        fs.readFile('./images/tesla.jpg', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'image/jpg'});
            response.write(contents); 
            response.end();
        }); 
    }
    else if (request.url === "/stylesheets/style.css"){
        fs.readFile('stylesheets/style.css', 'utf8', (errors, contents) =>{
            response.writeHead(200, {'Content-Type': 'text/css'});
            response.write(contents + "p{background-color: black};"); 
            console.log(contents);
            response.end();
        });
    }
    else if (request.url === "/cats") {
         fs.readFile('ninjas.html', 'utf8', (errors, contents) => {
             response.writeHead(200, {'Content-type': 'text/html'});
             response.write(contents); 
             response.end();
         });
    }
    else if (request.url === "/cars/new") {
        fs.readFile('newcar.html', 'utf8', (errors, contents) => {
            response.writeHead(200, {'Content-type': 'text/html'});
            response.write(contents); 
            response.end();
        });
   }
   
    else {
        response.end("URL requested is not available.");
    }
});
server.listen(7077);
console.log("listening on port 7077");

// localhost:6789/    This route should serve a view file called index.html
//  and display a greeting.
// localhost:6789/ninjas    This route should serve a view file called
//  ninjas.html and display information about ninjas.
// localhost:6789/dojos/new    This route should serve a view file called dojos.html and have a form (don't worry about where the form should be sent to).
