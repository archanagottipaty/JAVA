<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Button ClickerM</title>
</head>
<body>
<form action = '/ButtonClickerM/Home' method='post'>
<input type="submit" value = 'Click Me!' name ="submit">
</form>
<%! int i = 0; %> 

<p>You have clicked this item <%= i %> <%= session.getAttribute("count") %> times <p>

</body>
</html>