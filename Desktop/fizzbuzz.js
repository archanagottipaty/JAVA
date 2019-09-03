function fizzbuzz(n){
  var  i;    // Statement 1
  for (i = 0; i <= n; i++) { 
//If the number is divisible by both 3 and 5, log "FizzBuzz" instead of the number
//If the number is divisible by 3 but not by 5, log "Fizz" instead of the number
//If the number is divisible by 5 but not by 3, log "Buzz" instead of the number
  if ((i%3)===0 &&(i%5)===0){
//     console.log("*********i:", i);
   console.log("FizzBuzz");}
  else if ((i%3)===0)
    console.log("Fizz");
  else if ((i%5) ===0)
    console.log("Buzz");
  else
    console.log(i);
  }}
fizzbuzz(5);
