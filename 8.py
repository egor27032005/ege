k=0
for a in "1234567":
    for b in "01234567":
        for c in "01234567":
            for d in "01234567":
                for e in "01234567":
                    for f in "01234567":
                        for n in "01234567":
                            for m in "01234567":
                                result=a+b+c+d+e+f+n+m
                                sog1=result.count('00')+result.count('02')+result.count('04')+result.count('06')+result.count('20')+result.count('22')+result.count('24')+result.count('26')+result.count('40')+result.count('42')+result.count('44')+result.count('46')+result.count('60')+result.count('62')+result.count('64')+result.count('66')
                                sog2=result.count('11')+result.count('13')+result.count('15')+result.count('17')+result.count('31')+result.count('33')+result.count('35')+result.count('37')+result.count('51')+result.count('53')+result.count('55')+result.count('57')+result.count('71')+result.count('73')+result.count('75')+result.count('77')
                                if sog1+sog2==0 and result.count('0')==1 and result.count('1')==1 and result.count('2')==1 and result.count('3')==1 and result.count('4')==1 and result.count('5')==1 and result.count('6')==1 and result.count('7')==1:
                                    k+=1
                                    print(k, result)