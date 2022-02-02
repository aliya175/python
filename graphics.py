from packagegraphics.cirfunction import *
from packagegraphics.sphearfunction import *
from packagegraphics.rectfunction import *
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
print("Area:",rectarea(l,b))
print("Perimeter:",rectperimeter(l,b))
r=int(input("Enter radius:"))
print("Area:",circle(r))
print("Perimeter:",cirperimeter(r))
