# Assignment 3: Real World Application of Loop Control Statements
def display_menu():
    print("       FIFA WORLD CUP 2026 SIMULATOR    ") 
    print("1. Win this match")
    print("2. Draw this match")
    print("3. Lose this match")
    print("4. Skip this round (rest)")
    print("5. View team stats")
    print("6. Forfeit tournament")
       
def main():
    team_name = str(input("Enter your country team: "))
    opponents = [
        "Brazil", "Argentina", "France",
        "Germany", "Spain", "England",
        "Portugal","Scotland"
    ]
    wins = 0
    losses = 0
    draws = 0
    goals_for = 0
    goals_against = 0
    current_round = 0
    total_rounds = len(opponents)
    skips_remaining = 2

    print(f"Welcome! You are managing: {team_name}")
    print(f"Win the tournament by surviving all {total_rounds} rounds!")
    print(f"You have {skips_remaining} rest/skip(s) available.")

    while current_round < total_rounds:
        opponent = opponents[current_round]
        round_name = "FINAL" if current_round == total_rounds - 1 else f"Round {current_round + 1}"
        print(f" {round_name}: {team_name} vs {opponent}")
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        # Win the match
        if choice == "1":
            gf = int(input("Goals scored: "))
            ga = int(input("Goals conceded (must be less than goals scored): "))
            if ga >= gf:
                print("For a win, goals scored must be greater than goals conceded. Try again")
                continue
            goals_for += gf
            goals_against += ga
            wins += 1
            print(f"MATCH RESULT: {team_name} {gf} - {ga} {opponent}")
            print(f" Victory! {team_name} advances!")
            current_round += 1
            if current_round == total_rounds:
                print(f"CONGRATULATIONS! {team_name} has WON the FIFA WORLD CUP 2026!")
                break  # Tournament complete — exit the loop

        # Draw the match
        elif choice == "2":
            goals = int(input("Goals each team scored (same score): "))
            goals_for += goals
            goals_against += goals
            draws += 1
            print(f" MATCH RESULT: {team_name} {goals} - {goals} {opponent}")
            print(" It's a draw! Going to penalties...")
            penalty = input("Did you win the penalty shootout? (yes/no): ").strip().lower()
            if penalty == "yes":
                print(f"{team_name} wins on penalties! Advancing...")
                wins += 1
                current_round += 1
            else:
                print(f"{team_name} loses on penalties. Eliminated!")
                losses += 1
                break  # Eliminated — exit the loop

        # Lose the match
        elif choice == "3":
            gf = int(input("Goals scored: "))
            ga = int(input("Goals conceded (must be more than goals scored): "))
            if ga <= gf:
                print(" For a loss, goals conceded must be greater than goals scored. Try again.")
                continue
            goals_for += gf
            goals_against += ga
            losses += 1
            print(f" MATCH RESULT: {team_name} {gf} - {ga} {opponent}")
            print(f" Defeat. {team_name} is eliminated from the World Cup.")
            break  # Eliminated — exit the loop

        # continue — skip this round
        elif choice == "4":
            if skips_remaining > 0:
                skips_remaining -= 1
                print(f" {team_name} chose to rest this round.")
                print(f"The match vs {opponent} is forfeited as a 0-3 loss.")
                print(f"Skips remaining: {skips_remaining}")
                losses += 1
                goals_against += 3
                current_round += 1
                continue  # Skip to the next iteration without further action
            else:
                print(" No skips remaining! You must play.")
                continue  # Re-show menu without advancing round

        # pass — view stats, no other action
        elif choice == "5":
            print(f" Stats for {team_name}:")
            print(f"   Rounds played : {current_round}")
            print(f"   Wins          : {wins}")
            print(f"   Draws         : {draws}")
            print(f"   Losses        : {losses}")
            print(f"   Goals For     : {goals_for}")
            print(f"   Goals Against : {goals_against}")
            pass  # No further action needed — loop continues naturally

        # break — forfeit the tournament
        elif choice == "6":
            print(f" {team_name} has forfeited the World Cup 2026.")
            print("Better luck next time!")
            break  # Exit the while loop immediately

        else:
            print("Invalid choice. Please enter 1 to 6.")
            continue  # Re-display menu

    # Final summary
    print(f"       FINAL STATS: {team_name}")
    print(f"  Rounds Played : {current_round}")
    print(f"  Wins          : {wins}")
    print(f"  Draws         : {draws}")
    print(f"  Losses        : {losses}")
    print(f"  Goals For     : {goals_for}")
    print(f"  Goals Against : {goals_against}")
main()