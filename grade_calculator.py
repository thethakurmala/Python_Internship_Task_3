def calculate_grade():
    print("--- Welcome to the Student Grade Portal ---")

    try:
        # 1. Take marks input from user (Convert to float to handle decimals)
        marks = float(input("Enter the student's marks (0-100): "))

        # 2. Handle invalid marks using conditions (Data Validation)
        if marks < 0 or marks > 100:
            print("Error: Invalid input. Marks must be between 0 and 100.")
        
        else:
            # 3. Use if-elif-else to determine grade
            # 4. Adding Nesting to simulate business rules
            if marks >= 40:
                print("Status: PASSED")
                
                # Nested condition for specific distinctions
                if marks >= 90:
                    grade = "A+"
                    msg = "Excellent performance! Keep it up."
                elif marks >= 80:
                    grade = "A"
                    msg = "Very good! You have a bright future."
                elif marks >= 70:
                    grade = "B"
                    msg = "Good job, but there is room for improvement."
                elif marks >= 60:
                    grade = "C"
                    msg = "Satisfactory. Focus more on core concepts."
                else:
                    grade = "D"
                    msg = "Just passed. You need to work much harder."
                
                # Using logical operators for a special business rule
                # Rule: If marks are between 40 and 50, suggest a counselor
                if marks >= 40 and marks < 50:
                    msg += " (Note: We recommend attending a bridge course.)"
            
            else:
                # Failing grade
                grade = "F"
                msg = "Failed. Please contact your tutor for a re-exam."

            # 5. Display proper messages
            print(f"Grade: {grade}")
            print(f"Feedback: {msg}")

    except ValueError:
        print("Error: Please enter a valid numerical number.")

if __name__ == "__main__":
    calculate_grade()