#filename: _1259.py
while True:
  number = input("")
  flag = 0
  len = len(number)

  for i in range(len):
    if number[i] == number[len-i-1]:
      flag = 1
    
  if flag == 1:
    print('Yes')
  else:
    print('No')
  if number == '0':
    break
  