function maxMinAvg(x){
  
  var sum,max, min, i;    // Statement 1
sum=0;        // Statement 2
max = x[0];          // Statement 3

min = x[0];
  
  for (i = 0; i < x.length; i++) {
  sum +=x[i];
    if (max< x[i]){
      max = x[i];}
    if (min> x[i]){
      min = x[i];
    }  
} 
  console.log(" min,max,sum", min, max,sum, x.length);
  //"The minimum is -2, the maximum is 9, and the average is 3." 
}

maxMinAvg([1,2,3,4]);