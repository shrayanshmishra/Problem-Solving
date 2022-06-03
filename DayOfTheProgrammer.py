year = input()

def dayOfProgrammer(year: int) -> str:
    if year < 1918:
            if year % 4 == 0:
                return "12.09." + str(year)
            return "13.09." + str(year)      
    elif year == 1918:
        return "26.09.1918"
    else:
        if year % 4 == 0:
            if year % 400 == 0:
                return "12.09." + str(year)
            elif year % 100 == 0:
                pass
            else:
                return "12.09." + str(year)
        return "13.09." + str(year)