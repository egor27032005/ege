
s='1'*75
while '111' in s or '222' in s:
    if '111' in s:
         s=s.replace('111','2',1)
    else:
        s=s.replace('222','1',1)
    # sum=s.count("3")*3+s.count("2")*2+s.count("1")
        # if sum==50:
    
print(s)
# for one in range(50):
#     for two in range(50):
#         for three in range(50):
#             s = "0"+ "1" * one + "2" * two + "3" * three + "0"
#             s_original = s
#             while "00" not in s:
#                 s = s.replace("01", "210", 1)
#                 s = s.replace("02",  "3101", 1)
#                 s = s.replace("03", "2012", 1)
#             if s.count("1") == 56 and s.count("2") == 44 and s.count("3") == 19:
#                 print(len(s_original))
#                 quit()
