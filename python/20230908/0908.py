is_active = True
is_student = False

if is_active:
    print("The user is active!")
else:
    print("The user is not active!")

if is_student:
    print("The user is a student!")
else:
    print("The user is not a student!")

x = True
y = False

print(x and y)
print(x or y)
print()
x, y = True, False

print(x and y)
print(x or y)

x = (147.9604 / 12.78) ** 10
print(x)


a = True
a = a and not a
print(a)

c = 1.2
c = 100 * c
print(c)

print(3 & 2)

d = "1dd"

d = d * 10
print(d)

print(1 is not 10)


print('------------')

print(3 & 2)

c = 5
print(f"{c}")

print(~3)
# 컴퓨터에서는 2의 보수라는 형태로 표현함. 그래서 어떤 정수값에 대응하는 음수를 더했을 때 -1이 되게 되어 있다. 그래서 3+a = -1이니까 a가 -1임
if c >= 10:
    print(c)

a = '1234'

print(a[3:-1])
print(a[0:-1])
print(a[:2])  # 0 생략 가능
print(a[:])
x = 1
y = 2
print(a[x:y])


print(a[:10])

# a[1] = 'a'  ~~> 불가능

a = '1234'

print(a[:-1])
