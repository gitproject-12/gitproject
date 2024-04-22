import random

class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def add_score(self, score):
        """플레이어의 총점에 주어진 점수를 추가합니다."""
        self.total_score += score

    def reset_score(self):
        """플레이어의 총점을 초기화합니다."""
        self.total_score = 0

def roll_dice():
    """1에서 6 사이의 무작위 숫자를 반환하는 주사위를 굴리는 함수입니다."""
    return random.randint(1, 6)

def pig_game(players, target_score=100):
    """Pig Dice 게임을 실행하는 함수입니다.
    
    Args:
        players (list): 플레이어 객체로 이루어진 리스트입니다.
        target_score (int, optional): 게임에서 이길 수 있는 최소 점수입니다. 기본값은 100입니다.
    """
    current_player_index = 0
    while True:
        current_player = players[current_player_index]

        print(f"\n{current_player.name}의 차례입니다.")
        input("주사위를 굴릴 준비가 되셨다면 Enter 키를 눌러주세요...")

        round_score = 0
        dice_value = roll_dice()
        print(f"주사위 숫자: {dice_value}")

        if dice_value == 1:
            round_score = 0
            print("1이 나왔습니다. 라운드 점수가 초기화됩니다.")
        else:
            round_score += dice_value
            print(f"라운드 점수: {round_score}")

            while True:
                decision = input("계속해서 주사위를 굴릴까요 (r) 아니면 점수를 저장할까요 (h)? ").lower()
                if decision == 'r':
                    dice_value = roll_dice()
                    print(f"주사위 숫자: {dice_value}")
                    if dice_value == 1:
                        round_score = 0
                        print("1이 나왔습니다. 라운드 점수가 초기화됩니다.")
                        break
                    else:
                        round_score += dice_value
                        print(f"라운드 점수: {round_score}")
                elif decision == 'h':
                    current_player.add_score(round_score)
                    print(f"{current_player.name}님이 점수를 저장했습니다. 현재 라운드의 점수 {round_score}가 총점에 추가되었습니다.")
                    break
                else:
                    print("잘못된 입력입니다. 'r'을 입력하면 주사위를 다시 굴리고, 'h'를 입력하면 점수를 저장합니다.")

        if current_player.total_score >= target_score:
            print(f"\n{current_player.name}님이 {current_player.total_score}점으로 승리하셨습니다!")
            break

        current_player_index = (current_player_index + 1) % len(players)

# Main code
num_players = int(input("플레이어의 수를 입력하세요: "))
players = [Player(input(f"플레이어 {i+1}의 이름을 입력하세요: ")) for i in range(num_players)]

pig_game(players)

