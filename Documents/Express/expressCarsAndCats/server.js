const express = require("express");
const app = express();
app.set('views', __dirname + '/views');
app.get("/users", (req, res) => {
})

app.get('/', (request, response) => {
   response.send("index.html");
});
app.listen(8000, () => console.log("listening on port 8000"));

app.use(express.static(__dirname + "/static"));

