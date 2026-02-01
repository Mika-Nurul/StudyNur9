str = input("")
n = str.lower().replace('.', '').replace(',', '').split()
m_count = {}
for m in n:
    if m in m_count:
        m_count[m] += 1  
    else:
        m_count[m] = 1
for m, count in m_count.items():
    print(f"{m}: {count}")
