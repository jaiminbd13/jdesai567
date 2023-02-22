def my_brand():
     print ("=*=*=*= Jaiminkumar Bhupeshkumar Desai =*=*=*=")
     print ("=*=*=*= Course 2023S-SSW567-A Software Testing,Quality Assurance and Maintanence =*=*=*= ")
     print("=*=*=*= HW 00 - Tools Setup =*=*=*= ")
     print ("=*=*=*= Date - 1/24/2023  =*=*=*= ")
my_brand()

def classifyTriangle(a,b,c):

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
         return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c and a == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2) :
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'
