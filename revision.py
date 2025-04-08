a=5
b=2.5
c=a+b        #casting
print(c)


thisdict={
    'Brand':'Ford',         # dictionary
    'Car'  :'Mustang',
    'year':2022
}
print(thisdict)



a='Hello,World' 
print(a[ :5])    #the fifth letter is not counted in slicing

txt='abdef' 
print(txt[-2:-5])


x=('banana','mango','grape')
# uncharngable,orderly,allows duplicates,can be indexed
print(x[0])

#allows mixing of all data types
# it can be converted to any data type for example

x=('banana',"mango")
a=list(x)
a[1]='maheu'
print




two_digit_number=input('enter any 2 numbers')
a=two_digit_number=[0]
b=two_digit_number=[1]
sum=int(a)+int(b)
print('sum')
if len(two_digit_number)==2:
    print('invalid input')

username=input('username?')
    
password=input("whats your password?")

if 'username' =="nonoe" and' password'=="myself":
 print('good')
else:
   print('wrongpassword')
