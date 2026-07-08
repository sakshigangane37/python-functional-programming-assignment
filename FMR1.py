from functools import reduce

ChkEven = lambda No : No % 2 == 0

CalSquare = lambda No : No * No

Addition = lambda No1,No2 : No1 + No2

def main():
    Numbers = []

    Data = input("Enter Numbers : ").split()

    for i in Data:
        Numbers.append(int(i))

    FilterData = list(filter(ChkEven,Numbers))

    MapData = list(map(CalSquare,FilterData))

    Ret = reduce(Addition,MapData)

    print("List after filter : ",FilterData)
    print("List after map :",MapData)
    print("Output of reduce : ",Ret)

if __name__ == "__main__":
    main()  