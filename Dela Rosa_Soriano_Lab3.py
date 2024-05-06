# Laboratory Exercise 3: DELA ROSA, SORIANO
# Exception Handling in Laboratory Activity 1 

def convert_to_MDY_format(date): 
       
    # Representation of Months     
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    
    # Remove the unnecessary whitespaces
    date = ''.join(date.split())

    try:        
        # USA Format (MM/DD/YYYY) 
        if "/" in date: 
            split_date = date.split("/", 2)
            month = int(split_date[0])
            day = split_date[1]
            year = split_date[2]
            if not (1 <= int(day) <= 31) or len(year) != 4 or not year.isdigit():
                raise ValueError("Invalid Date Components")
            return "{} {}, {}".format(months[month], day, year)
        
        # EUR Format (DD.MM.YYYY) 
        elif "." in date:
            split_date = date.split(".", 2)
            day = split_date[0]
            month = int(split_date[1])
            year = split_date[2]
            if not (1 <= int(day) <= 31) or len(year) != 4 or not year.isdigit():
                raise ValueError("Invalid Date Components")
            return "{} {}, {}".format(months[month], day, year)
            
        # ISO Format (YYYY-MM-DD)
        elif "-" in date:
            split_date = date.split("-", 2)
            year = split_date[0]
            month = int(split_date[1])
            day = split_date[2]
            if not (1 <= int(day) <= 31) or len(year) != 4 or not year.isdigit():
                raise ValueError("Invalid Date Components")
            return "{} {}, {}".format(months[month], day, year)
                
        # JIS Format (YYYYMMDD)    
        elif len(date) == 8:
            year = date[:4]
            month = int(date[4:6])
            day = date[6:8]
            if not (1 <= int(day) <= 31) or len(year) != 4 or not year.isdigit():
                raise ValueError("Invalid Date Components")
            return "{} {}, {}".format(months[month], day, year)
    
        # YMD Format (Year Month Day) 
        else: 
            numbers = "0123456789"
            if date[3] in numbers:
                year = date[:4]
                day = date[-2:]
                month = date.strip("[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]")
                month = (month.lower()).capitalize()
                if month not in months.values() or not (1 <= int(day) <= 31) or len(year) != 4 or not year.isdigit():
                    raise ValueError("Invalid Date Components")
                return "{} {}, {}".format(month, day, year)  
            
        # DMY Format (Day Month, Year)  
            else: 
                day = date[:2]
                split_month_year = date[2:].split(",", 2)
                month = split_month_year[0]
                year = split_month_year[1]
                month = (month.lower()).capitalize()
                if month not in months.values() or not (1 <= int(day) <= 31) or len(year) != 4 or not year.isdigit():
                    raise ValueError("Invalid Date Components")
                return "{} {}, {}".format(month, day, year)
                
    except ValueError as ve:
        return "Error: " + str(ve)
    except IndexError:
        return "Error: Invalid date format"
    except KeyError:
        return "Error: Month not recognized"
    except Exception as e:
        return "An error occurred: " + str(e)

while True:
    print("")
    print("CONVERT DATE INTO MDY (Month Day, Year) FORMAT")
    try:
        ask_user = input("Enter date: ")
        print(convert_to_MDY_format(ask_user))
    except KeyboardInterrupt:
        print("\n- - - - - Keyboard Interrupt Detected. Exiting . . . - - - - -\n")
        break
    except EOFError:
        print("- - - - - End of Input Reached Unexpectedly. Exiting . . . - - - - -\n")
        break