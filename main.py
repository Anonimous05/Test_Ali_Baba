while True:
    colPredmet = input("Введите количество предметов: ").split(" ")
    fourPredmet = input("Введите стоимость предметов (4): ").split(" ")

    if len(fourPredmet) > int(colPredmet[0]):
        print(f"Максимальное количество предметов {colPredmet[0]}")
    else:
        numMass = []
        for i in fourPredmet:
            numMass.append(int(i))
        numMass.sort()
        total = 0
        for i in numMass[len(numMass)-int(colPredmet[1]):len(numMass)]:
            total += i
        print(total)