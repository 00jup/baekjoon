n, k = map(int, input().split())
people = [i for i in range(1, n+1)]
key = 0
temp = k - 1
order = []
while people:
    key = (key+temp) % len(people)
    order.append(people.pop(key))

print('<'+', '.join(map(str, order))+'>')

# gwonjiyoung07
