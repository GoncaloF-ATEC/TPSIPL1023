from datetime import date


data = input("Data (dd/mm/aaaa):")
data2 = data.split("/")


dt = date(int(data2[2]),int(data2[1]), int(data2[0]))

print(dt.strftime("%d / %b / %Y"))
print(dt.strftime("%x"))
