p = "j*L3f&"
c = 5
print("*You only have 5 chances")
a = input("Please enter password:")
if a != p:
    c = c - 1
    print("Password incorrect, you still have", c, "chances left")
while a != p:
    c = c - 1
    a = input("Please re-enter password:")
    if c > 1:
        print("Password incorrect, you still have", c, "chances left")
    if c == 1:
        print("Password incorrect, you still have", c, "chance left")
    if c == 0:
        if a != p:
            print(
                "Account locked due to mutiple unsucessful attempt, please contect support for more infomation."
            )
            break
if a == p:
    print("Login sucessful!")