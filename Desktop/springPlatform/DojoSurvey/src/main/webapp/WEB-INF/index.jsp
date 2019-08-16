<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
    <%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Dojo Survey Index</title>
</head>
<body>

<form method="POST" action="/">
Your Name: <input type = text name = name>
Dojo Location: <select name = location>
  <option value="san jose">San Jose</option>
  <option value="seattle">Seattle</option>
  <option value="dallas">Dallas</option>
  <option value="nyc">NYC</option>
</select>
Favorite Language: <select name= language>
  <option value="python">Python</option>
  <option value="javascript">Javascript</option>
  <option value="java">Java</option>
  <option value="JQuery">JQuery</option>
</select>

Comment(Optional):
<textarea name = comment></textarea>

<input type="submit" name=Button>



</form>

</body>
</html>