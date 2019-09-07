const http = require('http');
const fs = require('fs');
const server = http.createServer((request, response) => {
    if(request.url === '/') {
        fs.readFile('index.html', 'utf8', (errors, contents) => {
            response.writeHead(200, {'Content-Type': 'text/html'});
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
    else if (request.url === "/dojo.html") {
         fs.readFile('dojo.html', 'utf8', (errors, contents) => {
             response.writeHead(200, {'Content-type': 'text/html'});
             response.write(contents); 
             response.end();
         });
    }
    else {
        response.end('File not found!!!');
    }
});
server.listen(6789);
console.log("listening on port 6789");
