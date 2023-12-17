print(3<5 and 7<5)
print(3<5 and not(7<5))
print(2+2==5 or 2+2==4)

def foo():
    print("Foo!")
    return True


if 2+2==5 and foo():
    print("True")
else:
    print("False")

# if ~((x<=5) & y>=7):
# if ((x>5) | (y<7)):
# if ~((x>9) | (y>3)):


a1=[6,2,4]
print(all((i%2==0) for i in a1))
a2=[2,7,6]
print(all((i%2==0) for i in a2))

a3=[1,7,9]
print(any((i%2==0) for i in a3))
a4=[9,2,3]
print(any((i%2==0) for i in a4))


def is_divisible_by_3(x):
    return x%3==0

lst=[5,17,6,10]
print(not any([is_divisible_by_3(x) for x in lst]))
print(all([not is_divisible_by_3(x) for x in lst]))
