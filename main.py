zakupy1 = {"warzywniak" : ["marchew", "seler", "rukola"]}
zakupy2 = {"piekarnia" : ["chleb", "pączek", "bułka"]}

for i in zakupy1.keys():
    for n in zakupy1.values():
        print("Idę do", i.title(), "kupuję tu :", str(n).title())

for i in zakupy2.keys():
    for n in zakupy2.values():
        print("Idę do", i.title(), "kupuję tu :", str(n).title())

shopping_list = ["marchew", "seler", "rukola", "chleb", "pączek", "bułka"]
print("W sumie kupię ", len(shopping_list), "produktów")
print("Teraz to działa na bank")
