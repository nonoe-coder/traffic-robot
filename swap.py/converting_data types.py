a="1"
b="2"           #addition of strings to have integious numbers

c=int(a)
d=int(b)
sum=(c+d)
print(sum)


a="1.2"       # casting
b="2.5"
c=float(a)            #addition of float numbers to have integious numbers
d=float(b)
sum=(c+d)
print(int(sum)) 



a="hello,world"    # print w
print(a[6])

a="hello,world"   #print last  character
print(a[-1])



a="hello,world!" #changing to capital letters
print(a.upper())


a="hello,world!"
print(len(a))   # checking length 


#slicing
b="hello,world!"
print(b[2:5])


a="juice"
b="water"

print(a[2:5])    #print ice and water

c=a[2:5]
print(c.capitalize()+" "+b.capitalize()) #  capitalizing fierst letters