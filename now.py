ki ={
 'username':'Rajdip34',
 'Age':'21',
 'password':'1610'
}
def log (u,p):
    if ki['username'] is 'Rajdip34'in u:
        print("your user name is right")
        if ki['password'] is '1610' in p:
            print("wellcome "+ str(ki['username']))
        else:
            print("type agin the password")
    else:
        print("worng usr and password")
u = input("enter your username: ")
p = input("enter your password: ")
print(log(u,p))
print("your age is " + str(ki['Age']))
