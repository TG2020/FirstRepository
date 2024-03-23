zakupy1 = {"warzywniak" : ["marchew", "seler", "rukola"]}
zakupy2 = {"piekarnia" : ["chleb", "pączek", "bułka"]}

for i in zakupy1.keys():
    for n in zakupy1.values():
        print("Idę do", i.title(), "kupuję tu :", str(n).title())

