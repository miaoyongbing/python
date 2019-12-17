

name=input("请输入姓名:")
password=input("请输入密码:")

with open("blacklist.txt","r",encoding="utf-8") as f:
    for bname in f.readlines():
        bname=bname.strip("\n")
        if name == bname:
            print("该用户禁止登录")
            break
with open("userAndPassword.txt",encoding="utf-8") as f:
    list=f.readlines()
    for i in range(len(list)):
        line=list[i].strip("\n").split()
        uname=line[0]
        upassword=line[1]
        times=line[2]
        if uname==name and password == upassword:
            print("登录成功" )
            break
        elif uname == name and password !=password:
            print("密码不对")   
            times=times+1
            list[i]=uname+" "+upassword+" "+times
            if times == 3:
                
            break


