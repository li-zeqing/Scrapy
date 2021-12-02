
list = []
for i in range(1, 101):
    url = 'http://search.dangdang.com/?key=python&act=input&page_index={}'.format(i)
    list.append(url)

print(list)