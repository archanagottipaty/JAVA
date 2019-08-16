<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
 <link rel="stylesheet" type="text/css" href="css/welcome.css">
    
    <%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Ninja Gold Game</title>
</head>
<body>
<div>Your Gold: <%= session.getAttribute("gold")%></div>
<div>
<form method="POST" action="/farm">
Farm
<input type=submit value="Find Gold">
<input type="hidden" id="cave" name="location" value="farm">
</form>
 <form method="POST" action="/farm">
Cave
<input type=submit value="Find Gold" >
<input type="hidden" id="cave" name="location" value = "cave">
</form>
<form method="POST" action="/farm">
House
<input type=submit value="Find Gold" >
<input type="hidden" id="house" name="location" value= "house">
</form>
<form method="POST" action="/farm">
Casino!
<input type=submit value="Find Gold">
<input type="hidden"  id="casino" name="location" value="casino">
</form>

</div>

<div>

Activities:
<textarea name =activities>
<%= session.getAttribute("activities")%>
</textarea>
</div>


</body>
</html>