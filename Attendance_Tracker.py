class AttendanceTracker:
    def __init__(self):
        self.attendance = {}

    def mark_attendance(self, student_id):
        if student_id in self.attendance:
            print(f"Student {student_id} is already marked present.")
        else:
            self.attendance[student_id] = True
            print(f"Attendance marked for student {student_id}.")

    def display_attendance(self):
        print("Attendance:")
        for student_id, present in self.attendance.items():
            status = "Present" if present else "Absent"
            print(f"Student {student_id}: {status}")

def main():
    tracker = AttendanceTracker()

    while True:
        print("Attendance Tracker Menu:")
        print("1. Mark Attendance")
        print("2. Display Attendance")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            tracker.mark_attendance(student_id)
        elif choice == "2":
            tracker.display_attendance()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        print()

if __name__ == "__main__":
    main()
