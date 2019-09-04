function bracesValid(x){
  var myarray= [];
  var i;
  var dict = {"{":"}","[" :"]", "(":")"};
  var opening = ["{","[","("];
  var closing = ["}","]",")"];
  
    if ((x.length%2)===1){console.log("false");return false;}
    if (closing.includes(x[0])){console.log("false");return false;}
  
    myarray[0] = x[0];
   for (i = 1; i<x.length; i++){
     if (closing.includes(x[i])){
       console.log(myarray[myarray.length-1]);
       console.log(dict[myarray[myarray.length-1]]);
       if (dict[myarray[myarray.length-1]]==x[i])
         console.log("Found a matching brace");
         myarray.pop();
     }
     if (opening.includes(x[i])){
     myarray[i] = x[i];
   }
   }
  if (myarray.length === 0) {console.log("true");return true;}
 }

bracesValid("{}");


 
 bracesValid("");