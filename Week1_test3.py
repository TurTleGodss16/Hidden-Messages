#Reverse String DNA with their complementary nucleotide
#Using dataset_3_2.txt
lines = []
with open('dataset_3_2.txt') as f:
    lines = f.read()
str = lines[::-1]
#print(str)
#stringg = 'AAAACCCGGT'
#str = stringg[::-1]
str_new =[]
for i in range(0, len(str)):
    if str[i] == 'A':
        str_new.append('T')
    if str[i] == 'T':
        str_new.append('A')
    if str[i] == 'G':
        str_new.append('C')
    if str[i] == 'C':
        str_new.append('G')
print("".join(str_new))
