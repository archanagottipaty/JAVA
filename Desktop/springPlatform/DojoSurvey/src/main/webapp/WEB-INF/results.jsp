<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
     <%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Dojo Survey Index</title>
</head>
<body>

<p>Submitted Info:</p>

<p>Name: <c:out value ="${name}" />
<p>Location: <c:out value ="${location}" />
<p>Language: <c:out value ="${language}" />
<p>Comment: <c:out value ="${comment}" />


</body>
</html>