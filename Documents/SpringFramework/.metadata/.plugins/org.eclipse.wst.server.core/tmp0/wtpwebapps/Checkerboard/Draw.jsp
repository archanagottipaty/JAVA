<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Checkerboard</title>
<link rel="stylesheet" href="mycss.css">
</head>
<body>
	
<!-- getting the value for the name parameter -->
    <% String height = request.getParameter("height");
	String width = request.getParameter("width");
		%>
    <!-- displaying the value -->
    <h1><%= height %></h1>
    <h1><%= width %></h1>
    <h1><%= Integer.parseInt(width) %></h1>
    
    
    <!-- for loops work as well! -->
    
  	
    <% for(int index1 = 0; index1 < Integer.parseInt(height); index1++) { %>
    <% for(int index = 0; index < Integer.parseInt(width); index++) { %>
    	<% if((index+index1)%2==0){ %>
   		<div id="index"> </div>
        	<%} else {%> 
        <div id="index2"></div>
        <% } %>
        
    <% } %>  
    <br>
    <% } %> 
   
 <p> Hello There </p>
 
 
</body>
</html>