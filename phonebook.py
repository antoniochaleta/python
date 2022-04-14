
n = 3 #int(input())

#name_numbers = [input().split() for _ in range(n)]

name_numbers = [["sam", "99912222"], ["tom", "11122222"] , ["harry", "12299933"]]
print(name_numbers)
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break