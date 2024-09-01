attendance = int(input("ENTER STUDENT ATTENDANCE IN '%' "))

if attendance < 0 or attendance > 100:
    print("INVALID INPUT! Attendance must be between '0' and '100'!")
else:
    # Handle cases for attendance below 70
    if attendance < 70:
        details = input("If you have any medical issue type 'YES' else type 'NO': ").lower()
        if details == "yes":
            days = int(input("How many days were you sick? "))
            # Adjust attendance based on medical days
            new_attendance = days * 7  # assuming 7% attendance per sick day
            adjusted_attendance = attendance + new_attendance
            if adjusted_attendance > 100:
                adjusted_attendance = 100  # Cap the attendance at 100%
            attendance = adjusted_attendance

    # Check fine status after attendance adjustments (if any)
    if attendance >= 90:
        print("NO FINE! You are eligible for the prize distribution policy!")
    elif 85 <= attendance < 90:
        print("500rs/- fine will be imposed.")
    elif 80 <= attendance < 85:
        print("You have to submit 1000rs/- fine + 1 assignment.")
    elif 75 <= attendance < 80:
        print("You have to submit 1500rs + 2 assignments for every subject.")
    elif 70 <= attendance < 75:
        print("You have to submit 2000rs fine + 3 assignments for every subject.")
    elif 65 <= attendance < 70:
        print("You have to submit 2500rs + 4 assignments for every subject.")
    elif 60 <= attendance < 65:
        print("3000rs + 4 assignments for every subject.")
    elif 55 <= attendance < 60:
        print("You have to submit 3500rs + 5 assignments for every subject.")
    elif 50 <= attendance < 55:
        print("You have to submit 4000rs + 6 assignments for every subject.")
    else:
        print("Submit the fine to the Co-Ordinator, arigatto!")
