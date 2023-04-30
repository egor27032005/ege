k=0
for a1 in "АКАДЕМИК":
    for a2 in "АКАДЕМИК":
        for a3 in "АКАДЕМИК":
            for a4 in "АКАДЕМИК":
                for a5 in "АКАДЕМИК":
                    for a6 in "АКАДЕМИК":
                        for a7 in "АКАДЕМИК":
                            for a8 in "АКАДЕМИК":
                                res=a1+a2+a3+a4+a5+a5+a6+a7+a8
                                t=res.count("АА")+res.count("ЕА")+res.count("АЕ")+res.count("ИE")+res.count("ЕИ")+res.count("AИ")+res.count("ИA")
                                s=res.count("КК")+res.count("КД")+res.count("ДК")+res.count("КМ")+res.count("МК")+res.count("МД")+res.count("ДМ")
                                if res.count("А")==2 and res.count("К")==2 and res.count("Д")==1 and res.count("Е")==1 and res.count("М")==1 and res.count("И")==1 and t==0 and s==0:
                                    k+=1
                                    print(k,res)
