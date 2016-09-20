def main():
    print("  1    ---")
    print("6 7 2 | / |")
    print("  8    ---")
    print("5 9 3 | / |")
    print("  4    ---")
    print("Введите номера палок:")
    string=input()
    lines=[int(x) for x in  string.split(' ')]
    check=[1,2,8,9]
    mass=[]
    mask=[[1,1,0,0],#0
          [0,1,0,0],#1
          [1,1,0,1],#2
          [1,0,1,1],#3
          [0,1,1,0],#4
          [1,0,1,0],#5
          [0,0,1,0],#6
          [1,0,0,0],#7
          [1,1,1,0],#8
          [1,1,1,1]]#9
    for i in range(0,4):
        if check[i] in lines:
            mass.append(1)
        else:
            mass.append(0)
    print(mass)
    k=0
    m=[1,1,0,0]
    for i in range(0,10):
        for j in range(0,4):
            if mass[j] == mask[i][j]:
                k+=1
        if k==4:
            print(i)
        k=0
if __name__=="__main__":
    main()
