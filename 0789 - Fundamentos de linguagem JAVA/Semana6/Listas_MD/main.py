from datetime import date


data = "10/12/2021" #input("Data (dd/mm/aaaa):")
data2 = data.split("/")


dt = date(int(data2[2]),int(data2[1]), int(data2[0]))



print(dt.strftime("%d / %b / %Y"))
print( type(dt.strftime("%x")) == str)
print( type(dt) == date)