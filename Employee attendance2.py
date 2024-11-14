import datetime

class StaffMember:
    def __init__(self, staff_id, full_name):
        self.staff_id = staff_id
        self.full_name = full_name
        self.attendance_records = []

    def record_attendance(self, attendance_status):
        today_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.attendance_records.append({
            'date': today_date,
            'status': attendance_status
        })
        print(f"Attendance recorded for {self.full_name} on {today_date} as '{attendance_status}'.")

    def get_attendance_summary(self):
        summary = {"Present": 0, "Absent": 0, "Late": 0}
        for record in self.attendance_records:
            summary[record['status']] += 1
        return summary

    def show_attendance_history(self):
        print(f"\nAttendance history for {self.full_name}:")
        for record in self.attendance_records:
            print(f"Date: {record['date']}, Status: {record['status']}")
        if not self.attendance_records:
            print("No attendance history found.")

    def show_attendance_on_date(self, date):
        records = [record for record in self.attendance_records if record['date'] == date]
        if records:
            print(f"\nAttendance for {self.full_name} on {date}:")
            for record in records:
                print(f"Status: {record['status']}")
        else:
            print(f"No attendance record found for {self.full_name} on {date}.")


class AttendanceManager:
    def __init__(self):
        self.staff_directory = {}

    def add_staff_member(self, staff_id, full_name):
        if staff_id in self.staff_directory:
            print("Staff ID already exists. Please use a unique ID.")
        else:
            self.staff_directory[staff_id] = StaffMember(staff_id, full_name)
            print(f"Staff member '{full_name}' added with ID: {staff_id}")

    def register_attendance(self, staff_id, attendance_status):
        if staff_id in self.staff_directory:
            self.staff_directory[staff_id].record_attendance(attendance_status)
        else:
            print("Staff ID not found. Please check and try again.")

    def view_individual_attendance(self, staff_id):
        if staff_id in self.staff_directory:
            self.staff_directory[staff_id].show_attendance_history()
        else:
            print("Staff ID not found.")

    def attendance_report_summary(self):
        print("\n--- Attendance Summary Report ---")
        for staff_id, staff in self.staff_directory.items():
            summary = staff.get_attendance_summary()
            print(f"{staff.full_name} (ID: {staff_id}) - Present: {summary['Present']}, Absent: {summary['Absent']}, Late: {summary['Late']}")
        print("---------------------------------")

    def check_attendance_on_date(self, staff_id, date):
        if staff_id in self.staff_directory:
            self.staff_directory[staff_id].show_attendance_on_date(date)
        else:
            print("Staff ID not found.")

    def start_system(self):
        while True:
            print("\n=== Staff Attendance Management ===")
            print("1. Add New Staff Member")
            print("2. Register Attendance")
            print("3. View Staff Attendance History")
            print("4. Attendance Summary Report")
            print("5. Check Attendance on Specific Date")
            print("6. Exit")

            choice = input("Select an action: ")
            if choice == '1':
                staff_id = input("Enter Staff ID: ")
                full_name = input("Enter Staff Name: ")
                self.add_staff_member(staff_id, full_name)
            elif choice == '2':
                staff_id = input("Enter Staff ID to register attendance: ")
                attendance_status = input("Enter status (Present/Absent/Late): ")
                if attendance_status in ["Present", "Absent", "Late"]:
                    self.register_attendance(staff_id, attendance_status)
                else:
                    print("Invalid status. Please enter 'Present', 'Absent', or 'Late'.")
            elif choice == '3':
                staff_id = input("Enter Staff ID to view attendance history: ")
                self.view_individual_attendance(staff_id)
            elif choice == '4':
                self.attendance_report_summary()
            elif choice == '5':
                staff_id = input("Enter Staff ID to check attendance on a specific date: ")
                date = input("Enter date (YYYY-MM-DD): ")
                self.check_attendance_on_date(staff_id, date)
            elif choice == '6':
                print("Exiting the Attendance Management System. Have a great day!")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    manager = AttendanceManager()
    manager.start_system()