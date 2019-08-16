<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
    <%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Secret Code</title>
</head>
<body>

<c:out value ="${error}" />
<h1>What is the code?</h1>
<!-- ... -->
<form method="POST" action="/">
    <label>Try Code: <input type="text" name="trycode"></label>
 
    <button>Login</button>
</form>


</body>
</html>