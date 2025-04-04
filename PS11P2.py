# Function to compute total points and average score
def compute_total_and_average(score1, score2, score3):
    total_points = score1 + score2 + score3  # Calculate total points
    average_score = total_points / 3  # Calculate average score
    return total_points, average_score

# Main program
def main():
    # Get input from the user
    last_name = input("Enter student's last name: ")
    score1 = float(input("Enter Exam 1 score: "))
    score2 = float(input("Enter Exam 2 score: "))
    score3 = float(input("Enter Exam 3 score: "))

    # Compute total points and average score
    total_points, average_score = compute_total_and_average(score1, score2, score3)

    # Display results
    print("\nStudent Exam Report")
    print("-------------------")
    print(f"Student: {last_name}")
    print(f"Total Points: {total_points:.2f}")
    print(f"Average Exam Score: {average_score:.2f}")

# Run the main function
main()
