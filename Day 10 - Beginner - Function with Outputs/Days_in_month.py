def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap Year")
        else:
            print("Leap year")
    else:
        print("Not leap year")

# todo: add more code here
year = int