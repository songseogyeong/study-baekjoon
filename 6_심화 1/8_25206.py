# 25206
# 너의 평점은

# 문제
# 인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다.
# 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!
# 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
# 인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.
# P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.
# 과연 치훈이는 무사히 졸업할 수 있을까?

# 입력
# 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.

# 출력
# 치훈이의 전공평점을 출력한다.
# 정답과의 절대오차 또는 상대오차가 10-4 이하이면 정답으로 인정한다.


# 풀이 1
total_score = 0
total_credit = 0

for _ in range(20):
  subject = list(input().split())
  credit = float(subject[1])

  if subject[2] == "A+":
    grade = 4.5
  elif subject[2] == "A0":
    grade = 4.0
  elif subject[2] == "B+":
    grade = 3.5
  elif subject[2] == "B0":
    grade = 3.0
  elif subject[2] == "C+":
    grade = 2.5
  elif subject[2] == "C0":
    grade = 2.0
  elif subject[2] == "D+":
    grade = 1.5
  elif subject[2] == "D0":
    grade = 1.0
  elif subject[2] == "F":
    grade = 0.0
  else:
    continue
  
  total_score += credit * grade
  total_credit += credit

result = total_score / total_credit

print(f"{result:.6f}")


# 풀이 2
rating = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total_score = 0
total_credit = 0

for _ in range(20):
  subject = list(input().split())

  if subject[2] == "P":
    continue
  else:
    total_score += float(subject[1]) * grade[rating.index(subject[2])]
    total_credit += float(subject[1])

result = total_score / total_credit

print(f"{result:.6f}")

# 풀이 3
grade = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

total_score = 0
total_credit = 0

for _ in range(20):
  subject = list(input().split())

  if subject[2] == "P":
    continue
  else:
    total_score += float(subject[1]) * grade[subject[2]]
    total_credit += float(subject[1])

result = total_score / total_credit

print(f"{result:.6f}")