# words = ['a', 1, 2]
# sentence = ' '.join(words)
# print(sentence) #### 에러 원인?


# x = input()
# print(x.split())

# y = input()
# z = y.split()
# print('-'.join(z))


# iterable 최상위클래스, list, str, range... 상속?

# l = [x**2 for x in range(1, 21) if x % 3 == 0]
# print(l)

# l = [1, 2, 3, 4, 5]
# l_1 = [x ** 2 for x in l]
# print(l)

# l = ['s1', 'n', 'l', 's2', 'p', 't']
# l_1 = [x for x in l if x[0] == 's'] # if 's' in x 
# print(l_1)

# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)

# l = ['a', 'b', 'c']
# for i, v in enumerate(l):
#     print(f'fruit{i} name is {v}')

# names = ['john', 'jane', 'doe']
# ages = [25, 30, 35]

# for name, age in zip(names, ages):
#     print(f'{name} is {age} years old.')


# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# dt = dict(zip(keys, values))

# list1 = [1,2,3]
# list2 = [4,5,6]
# list3 = [7,8,9]
# z = zip(list1, list2, list3)
# print(sum(z[0])) # 1 + 4 + 7 출력하기

# name = ['m', 'n', 's', 'a']
# roll_no = [4, 1, 3, 2]
# s = set(zip(name, roll_no))
# print(s)

# names = ['m', 'r', 'c']
# ages = [24, 50, 18]
# for i, v in enumerate(zip(names, ages)):
#     print(i, v) # 괄호 없애려면 좀더 여기서 좀 더 세부조정


# # 람다함수
# add = lambda x, y: x + y
# print(add(1, 3))
# # print(lambda x, y: x + y(4, 5))

# 람다, 리스트 컴프리헨션 중요, 공부하기
# 심화문법 github올리기
# 중간고사 필기시험 월 75분 시험










