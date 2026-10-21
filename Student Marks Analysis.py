a = 0
sum = 0
max = 0
name_max = ""
while a<4:
    name = input('Enter Student Name: ')
    a+=1
    sum = 0
    print('Enter marks for Subjects one by one:')
    for i in range(1,4):
        marks = int(input('marks: '))
        sum = sum+marks
        avg = sum//3
        #print(name,'scored',sum,'in all three subjects totally and',name,'scored an average of',avg)
        if max>avg:
            max=avg
            name_max=name
print(name_max,'scored the highest marks of',max)