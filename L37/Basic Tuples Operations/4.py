a=input('data1: ').split(',')
val=int(input('value: '))
print(f"tuple *  {val} = {tuple(a*val)}")
b=input('data2: ').split(',')
print(f'concatenation: {tuple(a+b)}')