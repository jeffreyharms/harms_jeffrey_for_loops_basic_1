# Basic
for x in range(0, 151):
    print(x)
    
# Multiples of 5 from 5-1,000
for y in range(5, 1001, 5):
    if y%5 == 0:
        print(y)
# Counting the Dojo Way
for i in range(1, 101):
    if i%5 == 0 and i%10 != 0:
        print("Coding")
    elif i%10 == 0:
        print("Coding Dojo")
    else:
        print(i)
# Whoa, That Sucker's Huge: add odd ints from 0-500,000 and print the sum
sucker = 0

for o in range(1, 500000):
    if o%2 != 0:
        sucker += o
print(sucker)
# Countdown by 4

for f in range(2018, 0, -4):
    print(f)

#flexible counter
low_num = 1
high_num = 9
mult = 3

for j in range(low_num, high_num+1):
    if j%mult == 0:
        print(j)