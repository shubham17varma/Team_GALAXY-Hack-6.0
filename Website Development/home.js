const express = require("express");
const app = express();

app.listen(3000, function(){
  console.log("Server running on port 3000!");
});

app.use(express.static("public"))
app.set('view engine', 'ejs');

app.get("/", function (req, res) {
  res.render("home.ejs");
})
