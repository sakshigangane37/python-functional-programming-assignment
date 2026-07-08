from functools import reduce

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True


Multiply = lambda No: No * 2

Maximum = lambda No1, No2: No1 if No1 > No2 else No2


def main():
    numbers = []

    Data = input("Enter Numbers : ").split()

    for i in Data:
        numbers.append(int(i))

    FilterData = list(filter(ChkPrime, numbers))

    MapData = list(map(Multiply, FilterData))

    Ret = reduce(Maximum, MapData)

    print("List after filter :", FilterData)
    print("List after map :", MapData)
    print("Output of reduce :", Ret)


if __name__ == "__main__":
    main()