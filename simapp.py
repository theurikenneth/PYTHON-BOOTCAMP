"""
CREATE A CONSOLE APPLICATION THAT DOES THE FOLLOWING:
- ask the user to set their pin
- the user has 3 attempts to login
- if the user enters a wrong pin, (s)he can reenter it again and
display the numbers of attempts left
- if attempts are exhausted, display sim blocked

"""

set_pin = int(input("Enter your pin\n:"))
i = 3
while i>0:
    pin = int(input("Enter your pin\n:"))

    if pin==set_pin:
        print("Login Successful")
        break
    elif pin!=set_pin:
        i-=1
        if i==0:
            print("Sim Blocked!!")
        else:
             print("You have",i,"attempts left")


"""
IMPROVEMENTS INCLUDE:
- the user has two pins when setting
"""

first_pin = int(input("Enter your pin:\n"))
repeat_pin = int(input("Re-enter the pin:\n"))

if first_pin == repeat_pin:
    i = 3
    while i > 0:
        pin = int(input("Enter your pin:\n"))

        if pin == first_pin:
            print("Login Successful")
            break
        elif pin != first_pin:
            i -= 1
            if i == 0:
                print("Sim Blocked!!")
            else:
                print("You have", i, "attempts left")
else:
    print("The pin entries do not match")