classUN = ['Welma','Tapiwa','Fellan']
print(classUN[1])                           # listing
print(len(classUN))
classUN[1]='Simba' # replacing a name on the list
print(classUN)

print(classUN[1:])
print(classUN[:-1])


#
special  =classUN[:1]
print(special)
special.append('prince')#adding a name on the list after the last nmae
print(special)






password=("input your passord")
c=int(password)
if c==1345:      # a program tht assks matches username and password
    print("password is correct")
else:
    print("wrong password")

x=5
y=0   # making numbers more readable
z=x/y
print(z)


name=input('whats your name')
age='inputspecial'.insert(0,'mike')  #Insert a name to a specific position on the list
print(special)

classUN.extend(special)     #joining 2 lists
print(classUN)('your age')
score=input('youre score')

print("name"+" "+'age'+" "+'score')