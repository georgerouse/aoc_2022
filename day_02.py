def p1_calculate_score(opponent_choice, your_choice):
    score = 0
    # Calculate score from your choice
    if your_choice == "ROCK":
        score += 1
    elif your_choice == "PAPER":
        score += 2
    elif your_choice == "SCISSORS":
        score += 3

    # Draws
    if (opponent_choice == "PAPER" and your_choice == "PAPER") or \
        (opponent_choice == "ROCK" and your_choice == "ROCK") or \
        (opponent_choice == "SCISSORS" and your_choice == "SCISSORS"):
        score += 3

    # Wins
    if (opponent_choice == "PAPER" and your_choice == "SCISSORS") or \
        (opponent_choice == "ROCK" and your_choice == "PAPER") or \
        (opponent_choice == "SCISSORS" and your_choice == "ROCK"):
        score += 6

    return score


def p2_calculate_score(opponent_choice, ending, debug_prints=False):
    # TODO: Update the below to be a win/lose dictionary lookup
    # Calculate score from your ending
    if ending == "Y": # Draw
        your_choice = opponent_choice
    elif ending == "Z": # Win
        # A for Rock, B for Paper, and C for Scissors
        if opponent_choice == "ROCK":
            your_choice = "PAPER"
        elif opponent_choice == "PAPER":
            your_choice = "SCISSORS"
        elif opponent_choice == "SCISSORS":
            your_choice = "ROCK"
    elif ending == "X": # Lose
        if opponent_choice == "PAPER":
            your_choice = "ROCK"
        elif opponent_choice == "SCISSORS":
            your_choice = "PAPER"
        elif opponent_choice == "ROCK":
            your_choice = "SCISSORS"

    if debug_prints:
        print(f"opponent_choice: {opponent_choice}")
        print(f"your_choice: {your_choice}")
        print(f"ending: {ending}")

    score = p1_calculate_score(opponent_choice, your_choice)

    if debug_prints:
        print(f"score: {score}")

    return score

opponent_choice_map = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
your_choice_map = {"X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}

if __name__ == "__main__":
    # Get the input data
    # A for Rock, B for Paper, and C for Scissors
    # X for Rock, Y for Paper, and Z for Scissors
    # Scores: 1 for Rock, 2 for Paper, and 3 for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    with open("inputs/day_02.txt") as f:
        file_data = f.read()

    file_totals = []
    elf_total = 0
    for line in file_data.split("\n"):
        opponent_choice, your_choice = line.split(" ")
        opponent_choice = opponent_choice_map[opponent_choice]
        your_choice = your_choice_map[your_choice]
        round_score = p1_calculate_score(opponent_choice, your_choice)
        file_totals.append(round_score)

    print(f"Answer to part 1: {sum(file_totals)}")

    file_totals = []

    # X means lose, Y means draw and Z means win
    for line in file_data.split("\n"):
        opponent_choice, ending = line.split(" ")
        opponent_choice = opponent_choice_map[opponent_choice]
        round_score = p2_calculate_score(opponent_choice, ending)
        file_totals.append(round_score)

    print(f"Answer to part 2: {sum(file_totals)}")
