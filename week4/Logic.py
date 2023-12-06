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