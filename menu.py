def readfile():
    try:
        with open("sample.txt",'r') as f:
            L=f.readlines()
            for i in L:
                print(i,end="")
    except FileNotFoundError:
        print("File not found")

def Addtofile():
  with open("sample.txt","a") as f:
    while True:
      L=input("append :")
      f.write(L+"\n")
      choice=input("Press 'Y' or 'y' to continue ")
      if choice not in ['Y','y']:
        break

def Writetofile():
  with open("sample.txt","w") as f:
    while True:
      L=input("Write :")
      f.write(L+"\n")
      choice=input("Press 'Y' or 'y' to continue ")
      if choice not in ['Y','y']:
        break

while True:
    print("*********M A I N    M E N U***********")
    print("1. Read a Text File")
    print("2. Write into a Text File")
    print("3. Append a Text File")
    print("4. Exit")
    ch=input("\n\nEnter Choice :")
    if ch=='1':
        readfile()
    elif ch=='2':
        Writetofile()
    elif ch=='3':
        Addtofile()
    else:
        break
