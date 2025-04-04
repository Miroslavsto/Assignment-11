# Function to compute average score and average score with handicap
def compute_average_scores(game1, game2, game3, handicap):
    average_score = (game1 + game2 + game3) / 3  # Calculate average of 3 games
    average_with_handicap = average_score + handicap  # Add handicap to average
    return average_score, average_with_handicap

# Main program
def main():
    # Get input from the user
    last_name = input("Enter bowler's last name: ")
    game1 = float(input("Enter score for Game 1: "))
    game2 = float(input("Enter score for Game 2: "))
    game3 = float(input("Enter score for Game 3: "))
    handicap = float(input("Enter handicap: "))

    # Compute averages
    average_score, average_with_handicap = compute_average_scores(game1, game2, game3, handicap)

    # Display results
    print("\nBowling Score Report")
    print("---------------------")
    print(f"Bowler: {last_name}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Average Score with Handicap: {average_with_handicap:.2f}")

# Run the main function
main()
