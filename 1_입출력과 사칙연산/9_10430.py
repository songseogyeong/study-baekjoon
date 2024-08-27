# 10430
# 나머지

# 문제
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

# 출력
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.


# 풀이 1
A, B, C = input().split()
A, B, C = int(A), int(B), int(C)
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)


# 풀이 2
A, B, C = map(int, input().split())

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)


# 풀이 3
A, B, C = map(int, input().split())

print('%d\n%d\n%d\n%d' % ((A + B) % C, ((A % C) + (B % C)) % C, (A * B) % C, ((A % C) * (B % C)) % C))
