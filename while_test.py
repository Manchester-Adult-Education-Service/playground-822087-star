# nesteted loop=Aloop inside another loop (outer inner)
#outer loop:
#       inner loop:

#for x in range (1,10):
   # print (x) this will print one after one 

# if you need nto print all in one line 

#    print(x, end=" ")

# this will print like that "123455678"

# if need to print this in time ex 5 time 
# do like this way 
count=1
for x in range (5):
    count=count+1
    for y in range (1,11):
        print (y,end="  ")
    print ()
    print(count)
    



