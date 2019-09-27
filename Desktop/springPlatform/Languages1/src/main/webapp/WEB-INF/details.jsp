<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page isErrorPage="true" %>    
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>     
    
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Java</title>
</head>
<body> 
<a href = "/languages">Dashboard</a>
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Creator</th>
            <th>Version</th>
        </tr>
    </thead>
    <tbody>
       
        <tr> <td><c:out value='${language.name}'/></td>
            <td><c:out value="${language.creator}"/></td>
            <td><c:out value="${language.version}"/></td>  
        </tr>
       
    </tbody>
    <a href = "/languages/edit/${language.id}">Edit</a><br>
    <a href = "/languages/delete/${language.id}">Delete</a>
</body>
</html>