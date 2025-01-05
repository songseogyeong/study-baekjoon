# 1157
# 단어 공부

# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


# 풀이 1
text = input().strip().upper()

alphabet_count = {}

for char in text:
    if char in alphabet_count:
        alphabet_count[char] += 1
    else:
        alphabet_count[char] = 1

max_count = max(alphabet_count.values())
max_check = [key for key, value in alphabet_count.items() if value == max_count]

if len(max_check) > 1:
    print("?")
else:
    print(max_check[0])


# 풀이 2
text = input().upper()
text_list = list(set(text))

cnt = []

for i in text_list:
    count = text.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(text_list[(cnt.index(max(cnt)))])
