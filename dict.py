# a = {'key1':'value', 'key2':'value2'}
#
# print(a)
#
# a['key3'] = 'value3'
#
# print(a)
#
# try:
#     print(a['key4'])
# except KeyError:
#     print('이거슨 없다.')
#
import collections
#
# a = collections.defaultdict(int)
#
# a['A'] = 5
# a['B'] = 4
#
# print(a)
#
# a['c'] += 1
#
# print(a)

a = [1, 2, 3, 4, 5, 5, 5, 6, 6]

b = collections.Counter(a)

print(b)