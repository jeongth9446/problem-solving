# python은 int만 사용하면 된다. (큰 숫자에 대해 자동으로 C언어의 long 처럼 동작)

# set
a = {'a', 'b', 'c'}

# dict
b = {'a': 'A', 'b': 'B', 'c': 'C'}

# set에는 이미 있는 값을 추가해도 변화가 없다.
a.add('c')
print(a)

# 파이썬은 원시타입을 지원하지 않는다. (객체 타입)

# 파이썬의 리스트를 활용하면 아주 편함

a_list = list()
a_set = set()
a_dict = dict()
