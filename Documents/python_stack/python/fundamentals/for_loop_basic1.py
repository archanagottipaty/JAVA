# Question1: Basic 
#for x in range(0,151,1):
#   print(x)

#Question2: Multiples of Five
#for x in range(5,1001,5):
#	print(x)

#Question3:Counting, the Dojo Way
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. 
#If divisible by 10, print "Coding Dojo".

#for x in range(1,101,1):
#    if ((x%5)==0):
#        print("Coding")
#    else:
#        print(x)
#    if ((x%10)==0):
#        print("Coding Dojo")
#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum. 

#sum = 0
#for x in range(1,500000,2):
#    sum = sum + x
#print(sum)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

#for x in range(2018, 0, -4):
#   print(x)

#Flexible Counter - Set three variables: lowNum, highNum, mult.
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
# For example, if lowNum=2, highNum=9, and mult=3,
# the loop should print 3, 6, 9 (on successive lines)

def flexible_counter(lowNum,highNum,mult):
    for i in range(lowNum,highNum,1):    
        if (i%mult==0):
            print(i)

flexible_counter(1,100,5)




