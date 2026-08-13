def calculate_age(year_of_birth, current_year):
    if year_of_birth == current_year:
        return "You were born this very year!"  
    elif current_year > year_of_birth:
        age = current_year - year_of_birth
        if age == 1:
            return "You are 1 year old."
        else:
            return f"You are {age} years old."
            
    elif current_year < year_of_birth:
        years_until_birth = year_of_birth - current_year
        if years_until_birth == 1:
            return "You will be born in 1 year."
        else:
            return f"You will be born in {years_until_birth} years."
​
            
        