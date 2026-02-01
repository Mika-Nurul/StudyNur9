surnames = ["Невский", "СувороВ", "УшАКов", "Жуков", "Кутузов"]
def change_surname(surname):
    return surname.capitalize()  
afterchange_surnames = [change_surname(surname.lower()) for surname in surnames]  
for surname in afterchange_surnames:
    print(surname)
