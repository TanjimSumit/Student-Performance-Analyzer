marks = []

while True:
    print("1.Add Marks 2.Analyze 3.Exit")
    ch = input("Choice: ")
    if ch == '1':
        m = float(input("Marks: "))
        marks.append(m)
    elif ch == '2':
        if marks:
            print("Average:", sum(marks)/len(marks))
            print("Highest:", max(marks))
        else:
            print("No data")
    elif ch == '3':
        break
