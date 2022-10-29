




a = input("input your email adress")

for x in a:
    if x == '@':
        b = a.index("@")
        print("this is your domain")
        print(a[b:])
        
        print("this is your name")
        print(a[:b])


