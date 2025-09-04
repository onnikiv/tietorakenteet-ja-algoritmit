sum = 0.0

while True:
    try:
        luku = input()
        num = float(luku)
        if num == 0:
            print(f"The grand total is {sum}")
            break
        else:
            sum += num
            print(f"The total is now {sum}")
    except ValueError:
        print("That wasn’t a number.")
