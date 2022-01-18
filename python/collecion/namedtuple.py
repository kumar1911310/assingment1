store_item = dict()
for _ in range(int(input())):
    key,_,value = input().rpartition(" ")
    store_item[key] = store_item.get(key,0) + int(value)
for k,v in store_item.items():
    print(k,v)