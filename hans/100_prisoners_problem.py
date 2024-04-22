# 랜덤 모듈 임포트
import random


# 초기 변수 설정
n_prisoners = 100  # 죄수의 수
prisoners = list(range(n_prisoners))  # 0부터 99까지의 죄수 번호 리스트
boxes = []  # 박스의 내용 (초기화)
failures = 0  # 실패한 횟수
attempts = 1000  # 총 시도 횟수



# 1000번의 시도 동안 다음 단계 수행
for i in range(attempts):
    boxes = list(prisoners)  # 박스 안의 번호 섞기
    random.shuffle(boxes)

    for prisoner in prisoners:  # 각 죄수에 대해 번호 뽑기
        box_nr = prisoner
        for turn in range(n_prisoners // 2):  # 총 50개의 박스를 열 수 있음
            if boxes[box_nr] == prisoner:  # 자신의 번호를 뽑으면 반복 중지
                break
            box_nr = boxes[box_nr]  # 그렇지 않으면 박스에 적힌 번호로 다음 박스 선택
        else:  # 만약 50개의 박스를 모두 열었는데도 자신의 번호를 찾지 못하면 실패로 간주
            failures += 1  # 실패 횟수 추가
            break  # for 문 빠져나오기

print(f'{failures / attempts * 100}% 의 시도가 실패했습니다. ')