import time
import datetime
import threading
import os
import sys

class AlarmClock:
    def __init__(self):
        
        self.alarms = []
        self.running = True

    def set_alarm(self, time_str, label="Alarm"):
        """Validates and stores a new alarm."""
        try:
            
            datetime.datetime.strptime(time_str, "%H:%M")
            self.alarms.append({"time": time_str, "label": label, "triggered": False})
            print(f"Alarm set for {time_str}.")
        except ValueError:
            print("Error: Invalid time format. Please use HH:MM (24-hour).")

    def view_alarms(self):
        """Displays all alarms and their status."""
        if not self.alarms:
            print("No alarms set.")
            return
        
        print("\n--- Your Alarms ---")
        for idx, alarm in enumerate(self.alarms):
            status = "Ringed" if alarm["triggered"] else "Pending"
            print(f"{idx + 1}. {alarm['time']} - {alarm['label']} [{status}]")
        print("-------------------")

    def _check_alarms_worker(self):
        """Background worker that polls the system time against set alarms."""
        while self.running:
            now = datetime.datetime.now().strftime("%H:%M")
            for alarm in self.alarms:
                if alarm["time"] == now and not alarm["triggered"]:
                    print(f"\n\n [ALARM RINGING] {alarm['label']}! ")
                    alarm["triggered"] = True
                    
                   
                    os.system('afplay /System/Library/Sounds/Glass.aiff &')
                    
                    print("Press Enter to return to menu...")
            time.sleep(5)

    def start(self):
        checker_thread = threading.Thread(target=self._check_alarms_worker, daemon=True)
        checker_thread.start()

        print("=== Python CLI Alarm Clock ===")
        while self.running:
            print("\n1. Set Alarm\n2. View Alarms\n3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                t = input("Enter time (HH:MM in 24-hour format): ")
                label = input("Enter a label (optional): ") or "Wake up!"
                self.set_alarm(t, label)
            elif choice == '2':
                self.view_alarms()
            elif choice == '3':
                self.running = False
                print("Exiting...")
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    try:
        app = AlarmClock()
        app.start()
    except KeyboardInterrupt:
        print("\nExiting via keyboard interrupt...")
        sys.exit(0)