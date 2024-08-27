# 2588
# 곱셈

# 문제
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (그림)
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

# 출력
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.


# 풀이 1
num1 = int(input())
num2 = list(input())

print(num1 * int(num2[2]))
print(num1 * int(num2[1]))
print(num1 * int(num2[0]))
print(num1 * int(num2[0] + num2[1] + num2[2]))


# 풀이 2
num1 = int(input())
num2 = int(input())

print(num1 * (num2 % 10))
print(num1 * ((num2 % 100) // 10))
print(num1 * ((num2 % 1000) // 100))
print(num1 * num2)


# 풀이 3
num1 = int(input())
num2 = input()

for i in range(len(num2), 0, -1):
    print(num1 * int(num2[i - 1]))

print(num1 * int(num2))


# 풀이 4
num1 = int(input())
num2 = list(map(int, input()))

for i in range(len(num2), 0, -1):
    print(num1 * num2[i - 1])

join_str = ''.join(map(str, num2))
print(num1 * int(join_str))


# 풀이 5
num1 = int(input())
num2 = list(map(int, input()))

result = []

for i in range(len(num2), 0, -1):
    result.append(num1 * num2[i - 1])

print(result[0], result[1], result[2], sep='\n')
print(result[0] + (result[1] * 10) + result[2] * 100)
