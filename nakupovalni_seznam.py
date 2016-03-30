nakupovalni_listek = ["banane", "ananas",]

print("Seznam izdelkov")

while True:
    novi_izdelek = raw_input("Napisite izdelke, ki jih zelite oddati: ")

    if novi_izdelek == "ne":
     break

     nakupovalni_listek.append(novi_izdelek)

print("Tvoj seznam izdelkov:")

for izdelek in nakupovalni_listek:
    print(izdelek)

