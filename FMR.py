from functools import reduce

ChkRange = lambda No : No >= 70 and No <= 90 

Increment = lambda No : No+10

Product = lambda No1, No2 : No1 * No2

def main():
    Numbers = []

    Data = input("Enter Numbers : ").split()

    for i in Data:
        Numbers.append(int(i))

    FilterData = list(filter(ChkRange,Numbers))

    MapData = list(map(Increment,FilterData))

    Ret = reduce(Product,MapData)

    print("List after filter : ",FilterData)
    print("List after map :",MapData)
    print("Output of reduce : ",Ret)

if __name__ == "__main__":
    main()    