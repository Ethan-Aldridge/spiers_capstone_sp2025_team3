import tkinter as tk
from tkinter import messagebox, ttk
import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        sslmode="require"
    )

class BarcodeScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Battery Barcode Scanner")
        self.root.geometry("480x320")

        self.serial_num = None
        self.part_num = None
        self.expecting = "serial"
        self.user_ID = None

        self.user_frame = tk.Frame(root)
        self.barcode_frame = tk.Frame(root)
        self.desc_frame = tk.Frame(root)
        self.madlib_frame = tk.Frame(root)

        self.setup_user_screen()
        self.setup_barcode_screen()
        self.setup_desc_screen()
        self.setup_madlib_screen()

    def setup_user_screen(self):
        self.user_label = tk.Label(self.user_frame, text="Enter User ID", font=("Arial", 14))
        self.user_label.pack(pady=5)

        self.user_entry = tk.Entry(self.user_frame, font=("Arial", 14))
        self.user_entry.pack(pady=5, ipadx=10, ipady=5)
        self.user_entry.focus()

        self.user_keyboard_frame = tk.Frame(self.user_frame)
        self.user_keyboard_frame.pack()

        user_keys = ['1234567890', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm', ' ']
        for row in user_keys:
            row_frame = tk.Frame(self.user_keyboard_frame)
            row_frame.pack()
            for char in row:
                label = 'Space' if char == ' ' else char
                btn = tk.Button(row_frame, text=label, width=6 if char == ' ' else 3, font=("Arial", 10),
                                command=lambda c=char: self.user_entry.insert(tk.END, c))
                btn.pack(side=tk.LEFT, padx=1, pady=1)

        user_back_btn = tk.Button(self.user_keyboard_frame, text="Backspace", width=10, font=("Arial", 10),
                                  command=self.backspace_user)
        user_back_btn.pack(pady=3)

        self.continue_button = tk.Button(self.user_frame, text="Continue", font=("Arial", 12), command=self.continue_to_scan)
        self.continue_button.pack(pady=5)

        self.user_frame.pack(fill="both", expand=True)

    def setup_barcode_screen(self):
        self.user_display = tk.Label(self.barcode_frame, text="", font=("Arial", 10))
        self.user_display.pack(pady=2)

        self.label = tk.Label(self.barcode_frame, text="Scan Serial Number", font=("Arial", 14))
        self.label.pack(pady=5)

        self.entry = tk.Entry(self.barcode_frame, font=("Arial", 14))
        self.entry.pack(pady=5, ipadx=10, ipady=5)
        self.entry.bind("<Return>", self.scan_barcode)

        self.enter_button = tk.Button(self.barcode_frame, text="Enter", font=("Arial", 12), command=self.scan_barcode)
        self.enter_button.pack(pady=5)

        self.battery_type_var = tk.StringVar()
        self.battery_dropdown = ttk.Combobox(self.barcode_frame, textvariable=self.battery_type_var, state="readonly")
        self.battery_dropdown['values'] = ["Lead-Acid", "Lithium-Ion", "Ni-Mh", "Ni-Cd"]
        self.battery_dropdown.current(0)
        self.battery_dropdown.pack(pady=2)

        self.location_var = tk.StringVar()
        self.location_dropdown = ttk.Combobox(self.barcode_frame, textvariable=self.location_var, state="readonly")
        self.location_dropdown['values'] = ["Warehouse A", "Warehouse B", "Warehouse C"]
        self.location_dropdown.current(0)
        self.location_dropdown.pack(pady=2)

        self.status = tk.Label(self.barcode_frame, text="Waiting for input...", font=("Arial", 12))
        self.status.pack(pady=5)

        self.logout_button = tk.Button(self.barcode_frame, text="Logout", font=("Arial", 12), command=self.logout_user)
        self.logout_button.pack(pady=5)

    def setup_desc_screen(self):
        self.desc_label = tk.Label(self.desc_frame, text="Enter Description", font=("Arial", 12))
        self.desc_label.pack(pady=3)

        self.description_entry = tk.Entry(self.desc_frame, font=("Arial", 12), width=32)
        self.description_entry.pack(pady=3)

        self.keyboard_frame = tk.Frame(self.desc_frame)
        self.keyboard_frame.pack()

        keys = ['1234567890', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm', ' ']
        for row in keys:
            row_frame = tk.Frame(self.keyboard_frame)
            row_frame.pack()
            for char in row:
                label = 'Space' if char == ' ' else char
                btn = tk.Button(row_frame, text=label, width=6 if char == ' ' else 3, font=("Arial", 10),
                                command=lambda c=char: self.description_entry.insert(tk.END, c))
                btn.pack(side=tk.LEFT, padx=1, pady=1)

        back_btn = tk.Button(self.keyboard_frame, text="Backspace", width=10, font=("Arial", 10), command=self.backspace_description)
        back_btn.pack(pady=3)

        self.next_button = tk.Button(self.desc_frame, text="Next", font=("Arial", 12), command=self.show_madlib_screen)
        self.next_button.pack(pady=5)

    def setup_madlib_screen(self):
        self.madlib_label = tk.Label(self.madlib_frame, text="This battery is", font=("Arial", 12))
        self.madlib_label.pack(pady=3)

        madlib_dropdown_frame = tk.Frame(self.madlib_frame)
        madlib_dropdown_frame.pack()

        self.adj1 = tk.StringVar()
        self.adj2 = tk.StringVar()

        self.adj1_dropdown = ttk.Combobox(madlib_dropdown_frame, textvariable=self.adj1, state="readonly", width=10)
        self.adj1_dropdown['values'] = ["happy", "sad", "melancholy", "angry"]
        self.adj1_dropdown.current(0)
        self.adj1_dropdown.pack(side=tk.LEFT, padx=2)

        tk.Label(madlib_dropdown_frame, text="and").pack(side=tk.LEFT)

        self.adj2_dropdown = ttk.Combobox(madlib_dropdown_frame, textvariable=self.adj2, state="readonly", width=10)
        self.adj2_dropdown['values'] = ["safe", "hot", "old", "new"]
        self.adj2_dropdown.current(0)
        self.adj2_dropdown.pack(side=tk.LEFT, padx=2)

        self.submit_button = tk.Button(self.madlib_frame, text="Submit", font=("Arial", 12), command=self.save_battery)
        self.submit_button.pack(pady=5)

    def backspace_user(self):
        current_text = self.user_entry.get()
        self.user_entry.delete(0, tk.END)
        self.user_entry.insert(0, current_text[:-1])

    def continue_to_scan(self):
        entered_user_ID = self.user_entry.get().strip()
        if not entered_user_ID:
            messagebox.showwarning("Input Required", "Please enter a User ID!")
            return
        self.user_ID = entered_user_ID
        self.user_frame.pack_forget()
        self.user_display.config(text=f"User: {self.user_ID}")
        self.barcode_frame.pack(fill="both", expand=True)
        self.entry.focus()

    def logout_user(self):
        self.serial_num = None
        self.part_num = None
        self.expecting = "serial"
        self.user_ID = None
        self.entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.madlib_frame.pack_forget()
        self.desc_frame.pack_forget()
        self.barcode_frame.pack_forget()
        self.user_entry.delete(0, tk.END)
        self.user_display.config(text="")
        self.label.config(text="Scan Serial Number")
        self.status.config(text="Waiting for input...")
        self.user_frame.pack(fill="both", expand=True)
        self.user_entry.focus()

    def scan_barcode(self, event=None):
        code = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        if not code.isdigit():
            self.status.config(text="❌ Invalid barcode: must be numeric")
            return

        if self.expecting == "serial":
            self.serial_num = int(code)
            self.status.config(text=f"✅ Serial number scanned: {self.serial_num}")
            self.label.config(text="Scan Part Number")
            self.expecting = "part"
        elif self.expecting == "part":
            self.part_num = int(code)
            self.status.config(text=f"✅ Part number scanned: {self.part_num}")
            self.barcode_frame.pack_forget()
            self.desc_frame.pack(fill="both", expand=True)

    def show_madlib_screen(self):
        self.desc_frame.pack_forget()
        self.madlib_frame.pack(fill="both", expand=True)

    def backspace_description(self):
        current_text = self.description_entry.get()
        self.description_entry.delete(0, tk.END)
        self.description_entry.insert(0, current_text[:-1])

    def save_battery(self):
        item_type = self.battery_type_var.get()
        location = self.location_var.get()
        description = self.description_entry.get().strip()
        madlibs = f"This battery is {self.adj1.get()} and {self.adj2.get()}"

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM testdb_battery WHERE serial_num = %s", (self.serial_num,))
            if cursor.fetchone() is not None:
                conn.close()
                messagebox.showerror("Duplicate Error", "❌ This Serial Number already exists in the database!")
                self.reset()
                return

            now = datetime.now()
            cursor.execute("""
                INSERT INTO testdb_battery (serial_num, part_num, item_type, "user_ID", location, description, madlibs, image, date_added, last_modified)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (
                self.serial_num,
                self.part_num,
                item_type,
                self.user_ID,
                location,
                description,
                madlibs,
                "",
                now,
                now
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Saved", "Battery saved successfully!")
        except Exception as e:
            if conn:
                conn.rollback()
            messagebox.showerror("Database Error", f"Could not save to database:\n\n{e}")

        self.reset()

    def reset(self):
        self.serial_num = None
        self.part_num = None
        self.expecting = "serial"
        self.label.config(text="Scan Serial Number")
        self.status.config(text="Waiting for input...")
        self.entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.madlib_frame.pack_forget()
        self.desc_frame.pack_forget()
        self.barcode_frame.pack(fill="both", expand=True)
        self.entry.focus()

def main():
    load_dotenv()
    root = tk.Tk()
    BarcodeScannerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
