str = input("")
def z(str):
    glasnie = "аеёиоуыэюяaeiou"
    soglasnie = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
    
    glasnie_count = 0
    soglasnie_count = 0
    
    for char in str:
        if char in glasnie:
            glasnie_count += 1
        elif char in soglasnie:
            soglasnie_count += 1
    
    return glasnie_count, soglasnie_count

glasnie, soglasnie = z(str)
print(f"Гласные: {glasnie}, Согласные: {soglasnie}")
