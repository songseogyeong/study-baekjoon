# 2439
# 별 찍기 - 2

# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.


# 공부
# rjust(전체 자릿수)
# ljust(전체 자릿수)

# r/ljust 메서드에서는 문자열을 지정한 길이만큼 특정 문자를 채울 수 있는데,
# 딱 한 글자만 채울 수 있다.
# 디폴트는 ' ' 인 공백이며 생략이 가능하고, '' 또는 한 글자 초과 시 TypeError가 발생한다.
# TypeError: The fill character must be exactly one character long

N = 5

for i in range(1, N + 1):
  print(('*' * i).rjust(N, '-'))

# 하지만, replace를 사용하여 두 글자 이상도 가능하다!
# 대신 그만큼 정렬이 밀려난다...
  
N = 5

for i in range(1, N + 1):
  print(('*' * i).rjust(N, '-').replace('-', '--'))


# 풀이
N = int(input())

for i in range(1, N + 1):
  print(('*' * i).rjust(N))
