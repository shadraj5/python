#list -- List is mutable means it's value can change
#tuple -- Tupple is immutable means it's value can't change,object.

tp = (2,4,6)
print(tp)
#tp[1] = 1 can't change value

tp1= (1) #not tuple
tp2 = (1,) #is tuple
print(tp1)
print(tp2)

a=111
b=222
a,b =b,a #changing value
print(a,b)