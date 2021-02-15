dict_dat = {'chapter1': 'content1', 'chapter2': 'content1'}

key = 'chapter3'
dict_dat[key] = 'content1'

print(dict_dat)

# key = [1, 2, 3]
# dict_dat[key] = 'a list'
# print(dict_dat)

dict_temp = {'chapter1': {'name': 'basic', 'page': 31}, 'chapter2': {'name': 'senior', 'page': 42}}

print(dict_temp['chapter2'])
print(dict_temp['chapter2']['name'])
# print(dict_temp['chapter3'])

dict_temp['chapter3'] = {'name': 'middle', 'page': '50'}
print(dict_temp)

del dict_temp['chapter2']['name']
print(dict_temp)
dict_temp.clear()
print(dict_temp)
# del dict_temp
# print(dict_temp)

print(dict_temp.keys())

print(dict_temp.values())

print(dict_temp.items())