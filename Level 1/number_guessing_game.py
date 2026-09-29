import random

def number_guessing_game():
    # 1 se 100 ke beech random number generate karega
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("===== NUMBER GUESSING GAME =====")
    print(f"Maine 1 se 100 ke beech ek number socha hai.")
    print(f"Aapke paas total {max_attempts} attempts hain!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Apna guess batao: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Thoda bada number guess karo.\n")
            elif guess > secret_number:
                print("Too high! Thoda chota number guess karo.\n")
            else:
                print(f"🎉 Sahi guess! Aapne {attempts} attempts me sahi number pehchan liya!")
                break
        except ValueError:
            print("Invalid input! Kripya sirf ek number enter karein.\n")

    if attempts == max_attempts and guess != secret_number:
        print(f"❌ Game Over! Aapke saare attempts khatam ho gaye. Sahi number tha: {secret_number}")

if __name__ == "__main__":
    number_guessing_game()