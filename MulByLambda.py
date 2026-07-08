Multiplication = lambda No1, No2 : No1 * No2

def main():
    Data = input("Input : ").split()

    value1 = int(Data[0])
    value2 = int(Data[1])

    Ret = Multiplication(value1,value2)

    print("Output : ",Ret)

if __name__ == "__main__":
    main()