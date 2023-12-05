import tkinter as tk
import winsound
from datetime import datetime, timedelta
from tkinter import messagebox, ttk


class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("400x200")

        # current time
        self.current_time_label = ttk.Label(root, text="", font=("Helvetica", 16))
        self.current_time_label.pack(pady=10)

        # Set alarm
        self.label = ttk.Label(root, text="Set Your Alarm (hh:mm:ss):", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.time_entry = ttk.Entry(root, font=("Helvetica", 12))
        self.time_entry.insert(0, "HH:MM:SS")
        self.time_entry.pack(pady=10)

        self.set_button = ttk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_button['style'] = 'TButton'
        self.set_button.pack(pady=10)

        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.current_time_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_time)

    def set_alarm(self):
        alarm_time_str = self.time_entry.get()

        try:
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S")
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please use hh:mm:ss.")
            return

        current_time = datetime.now().time()
        current_datetime = datetime.combine(datetime.today(), current_time)

        alarm_datetime = datetime.combine(datetime.today(), alarm_time.time())

        if alarm_datetime < current_datetime:
            alarm_datetime += timedelta(days=1)

        time_difference = (alarm_datetime - current_datetime).seconds

        self.root.after(time_difference * 1000, self.alarm)

        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time_str}.")

    def alarm(self):
        messagebox.showinfo("Alarm", "Wake up Please!!!")
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
