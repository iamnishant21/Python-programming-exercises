KPH=[]
MPH=[]
count=0
while True :
    count+=1
    s=input("Enter the speed:")
    if s=="":
        break
    speed=float(s[1:])
    if s[0]=="U":
        MPH.append(speed)
        speed*=1.60934
        KPH.append(speed)
    else:
        KPH.append(speed)
        speed*=0.621371
        MPH.append(speed)
        print("max:{:.2f}KPH,{:.2f}MPH".format(max(KPH),max(MPH)))
        print("min:{:.2f}KPH,{:.2f}MPH".format(min(KPH),min(MPH)))
        print("average:{:.2f}KPH,{:.2f}MPH".format(sum(KPH)/len(KPH),sum(MPH)/len(MPH)))
        print(count)