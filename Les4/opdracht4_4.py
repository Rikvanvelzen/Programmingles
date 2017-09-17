oldpassword = 'kanari'
newpassword = str(input("Wat is je nieuwe paswoord: "))
def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and newpassword >= 6:
        return print("True")
    else:
        return print("False")
new_password(oldpassword, newpassword)