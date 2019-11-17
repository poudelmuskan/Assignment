class CustomDataset:

    # this is iterable
    numList = range(1, 101)

    for num in numList:
        print(num)

    print(type(numList))
    print("Extracting iterator form iterable-----------------------------")

    numiter = iter(numList)

    for num in numiter:
        print(num)

    #checking if iterator is used up
    print("Checking iterator after using----------------------------------")

    for num in numiter:
        print(num)