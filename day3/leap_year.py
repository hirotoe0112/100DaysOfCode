year = int(input())

leap_year_result = "Leap year"
not_leap_year_resul = "Not leap year"

if year % 4 != 0:
    print(not_leap_year_resul)
else:
    if year % 100 != 0:
        print(leap_year_result)
    else:
        if year % 400 == 0:
            print(leap_year_result)
        else:
            print(not_leap_year_resul)
