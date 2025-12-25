import random

# 1~100 사이의 숫자를 맞추는 게임
# 사용자가 첫번째 숫자를 입력하면 높은지 낮은지 알려주고
# 숫자 범위를 좁혀서 제시하면서 반복 시도하는 게임

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    min_range = 1
    max_range = 100

    # 게임 소개
    print("\nWelcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    # 게임 루프
    while attempts < max_attempts:

        try:
            # 사용자 입력 받기
            guess = int(input(f"Enter your guess ({min_range}~{max_range}): "))
            attempts += 1

            # 입력 유효성 검사
            if guess < min_range or guess > max_range:
                print(f"\nPlease enter a number within the range {min_range}~{max_range}.")
                continue
            # 정답 확인
            if guess < number_to_guess:
                print("\nToo low! Please enter a higher number.")
                min_range = guess + 1
            elif guess > number_to_guess:
                print("\nToo high! Please enter a lower number.")
                max_range = guess - 1
            else:
                # 정답 맞춤
                print(f"\nCongratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
            # 남은 시도 횟수 안내
            print(f"\nYou have {max_attempts - attempts} attempts left.")

        except ValueError:
            # 예외 처리
            print("\nInvalid input. Please enter a valid integer.")

        # 게임 종료 안내
        if attempts == max_attempts:
            # 정답 공개
            print(f"\nSorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_number_game() 
            