# Logical operator "and", "or", "not"
# when using logical operator "and" both sttaements should be true to be True
print("logical operator and")      
x = 10
print(x>5 and x < 15) # True
print (x> 5 or x < 5) # false
print(x<5 and x>40) # false
print()
#logical operator "or" 
#when using logoical operator "or" at lewstvone statement or both statements should be true to be true
print(x>5 or x < 15) # True
print (x> 5 or x < 5) # true
print(x<5 or x>40) # True
print(x>2 or x<30) #True
print(x<5 or x>40) #false

#logical operator 'not"
#if you nagate truth it becomes false, if you nagete false statement, the output becomes true
print()
print("logical operator not")

print(not(x>5 and x < 15))
print(not(x<5 or x>40))
y= 15
print(not y>3) #false
print(not y<3) #True
print(not(not y>45)) # false
      


