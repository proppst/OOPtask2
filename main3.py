sum_line = {}

with open('files/1.txt', 'rt', encoding='utf-8') as f:
    sum_line_1 = {}
    counting_1 = 0
    for line in f.readlines():
        counting_1 += 1
    sum_line[counting_1] = '1.txt'


with open('files/2.txt', 'rt', encoding='utf-8') as f:
    sum_line_2 = {}
    counting_2 = 0
    for line in f.readlines():
        counting_2 += 1
    sum_line[counting_2] = '2.txt'


with open('files/3.txt', 'rt', encoding='utf-8') as f:
    sum_line_3 = {}
    counting_3 = 0
    for line in f.readlines():
        counting_3 += 1
    sum_line[counting_3] = '3.txt'
print(sum_line)

numb_keys=sorted(list(sum_line.keys()))
print(numb_keys)
with open ('files/4.txt', 'w', encoding='utf-8') as f_res:
    f_res.write('')
with open ('files/4.txt', 'a', encoding='utf-8') as f_res:
    for i in numb_keys:
        f_res.write(sum_line[i]+'\n')
        f_res.write(str(i)+'\n')
        with open ('files/'+sum_line[i], 'r', encoding='utf-8') as f:
            f_res.write(f.read()+'\n')
