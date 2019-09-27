<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
    
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Languages</title>
</head>
<body> 

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Creator</th>
            <th>Version</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        <c:forEach items="${languages}" var="language">
        <tr>
            <td><a href ="/languages/${language.id}"><c:out value='${language.name}'/></a></td>
            <td><c:out value="${language.creator}"/></td>
            <td><c:out value="${language.version}"/></td>
            <td><a href="/languages/delete/${language.id}">Delete</a><a href="/languages/edit/${language.id}">Edit</a></td>
            
        </tr>
        </c:forEach>
    </tbody>
</table>
	<form action = "/createlanguage" method = "post">
		Name:
		<input type=text name = name >
		Creator:
		<input type = text name = creator >
		Version:
		<input type = version name=version >
		<input type = submit name = submit>
	</form>
</body>
</html>