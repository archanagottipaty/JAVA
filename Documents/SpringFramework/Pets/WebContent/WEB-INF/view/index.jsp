<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Make a Pet!</title>
</head>
<body>

<div>
<p>Make a Dog!</p>
<form action="/Pets/dog"> 
Name:
 <input name="name">
<label for="name">
Breed:</label>
 <input name="breed">
 <label for="breed"></label>
Weight:
 <input name="weight" >
 <input type="submit">
 <label for="submit"></label>
 </form>
</div>

<div>
<p>Make a Cat!</p>
<form action="/Pets/Cats">
 <input name="name">
<label for="name">
Breed:</label>
 <input name="breed">
 <label for="breed"></label>
Weight:
 <input name="weight" >
 <input type="submit">
 <label for="submit"></label>
 </form>
</div>
</body>
</html>