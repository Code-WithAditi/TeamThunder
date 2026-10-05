#arguments arbitrary positional arguments.
def add(a,b,*remaining):
    print (a+b+sum(remaining))
add(1,2,3,4,5)

def sub(a,b,*remaining):
    print(a - b - sum(remaining))
sub(10,2,5,8)  

def mul(a,b,*remaining):
    print(a*b *sum(remaining))   
mul(10,2)

#arbitrary keyword arguments 
def student (**details):
    print(details)
student(name="aditi",age =21, city="hamirpur")    

def student (**data):
    print(data)
student(name="aditi",age=21)

def add(*numbers):
    print(sum(numbers))
add(10,20,30)





    