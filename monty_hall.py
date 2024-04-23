import random

def monty_hall_simulation(num_trials):
    switch_wins = 0
    stay_wins = 0
    
    for _ in range(num_trials):
        # 세 개의 문과 각각의 뒤에 있는 상품(차 또는 염소) 설정
        doors = ['car', 'goat', 'goat']
        # 참가자가 선택한 문을 무작위로 설정
        choice = random.choice(doors)
        
        # 진행자가 열 문 선택 (참가자가 선택한 문이 아니고, 염소가 있는 문)
        opened = None
        for i in range(3):
            if doors[i] != choice and doors[i] == 'goat':
                opened = i
                break
        
        # 참가자가 선택을 변경
        switched_choice = None
        for i in range(3):
            if i != opened and i != doors.index(choice):
                switched_choice = i
                break
                
        # 선택을 변경하지 않고 이기는 경우
        if choice == 'car':
            stay_wins += 1
        # 선택을 변경해서 이기는 경우
        if doors[switched_choice] == 'car':
            switch_wins += 1
            
    stay_win_percentage = stay_wins / num_trials * 100
    switch_win_percentage = switch_wins / num_trials * 100
    
    print(f"시뮬레이션 결과 (시행 회수: {num_trials}):\n")
    print(f"선택을 변경하지 않고 이긴 경우: {stay_wins} 번 ({stay_win_percentage:.2f}%)")
    print(f"선택을 변경해서 이긴 경우: {switch_wins} 번 ({switch_win_percentage:.2f}%)")

# 시뮬레이션 회수 입력 받기
num_trials = int(input("몇 번의 시뮬레이션을 실행하시겠습니까? "))
monty_hall_simulation(num_trials)

