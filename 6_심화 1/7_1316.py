# 1316
# 그룹 단어 체커

# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.


# 풀이 1
N = int(input())
cnt = N

for _ in range(N):
    word = input()

    for i in range(0, len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            cnt -= 1
            break

print(cnt)


# 풀이 2
N = int(input())
count = 0

for _ in range(N):
    word = input()
    set_word = set()
    before_word = ''
    check_word = True

    for alphabet in word:
        if alphabet != before_word:
            if alphabet in set_word:
                check_word = False
                break
            else:
                set_word.add(alphabet)
                before_word = alphabet

    if check_word:
        count += 1

print(count)
