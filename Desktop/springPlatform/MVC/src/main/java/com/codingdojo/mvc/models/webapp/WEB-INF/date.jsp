<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
    <%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
    <script type="text/javascript" src="js/date.js"></script>
    
    <link rel="stylesheet" type="text/css" href="css/date.css">
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Date</title>
</head>
<body>
<p>This is the date jsp. </p>
<c:out value="${dojoName}"/>
<c:out value="${date}"/>

</body>
</html>