import sys

print("Hello, World!")
# To find the version of the editor
print(sys.version)
print(sys.api_version)
if 5>2:
    print("Five is the greatest number")
# variable name starts with alphabets and underscore  no number
# A variable number can only contains aplha-numeric characters and underscored(A-z, 0-9, and ....)
# A varable name are  case sensitive
# Variable name cannot be any of the python keywords
_x=int(3)
y=str("sita")
z=s=f="asdsad"
w,r,t="orange",5,"yellow"
print(_x)
print(y)
print(z)
print(s)
print(f)
print(w)
print(r)
print(t)
print(type(_x))
print(type(y))
#unpacking a collection-if you have a collection of value in a list.
#Python allows  you to extract the values into variables
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)
x="python is awesome"
print(x)
print(x+y+z)
