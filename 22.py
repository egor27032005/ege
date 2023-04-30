f = open('22.txt', 'r')
data = [x.replace(';', ' ').split() for x in f]
process = {'0': 0}
while len(data) + 1 != len(process):
    for x in data:
         if all(rel in process for rel in x[2:]):
             process[x[0]] = int(x[1]) + max(process[rel] for rel in x[2:])
print(max(process.values()))




