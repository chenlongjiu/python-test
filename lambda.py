def add(x,y):return x+y
add2 = lambda x,y:x+y
print add2(1,2)     #3

def sum(x,y=10):return x+y
sum2 = lambda x,y=10:x+y
print sum     
print sum2(1,100)   