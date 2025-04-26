import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import math
import string
import secrets
import requests
import hashlib
import datetime
from reportlab.pdfgen import canvas
import pyperclip

# --------------------------- Password Analysis Logic ---------------------------

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in string.punctuation for c in password): charset += len(string.punctuation)
    if charset == 0: return 0
    return round(len(password) * math.log2(charset), 2)

def estimate_crack_time(password):
    guesses = 2 ** calculate_entropy(password)
    crack_time_sec = guesses / (2 * 10**9)  # 2 billion guesses per second
    if crack_time_sec < 60:
        return f"{int(crack_time_sec)} seconds"
    elif crack_time_sec < 3600:
        return f"{int(crack_time_sec / 60)} minutes"
    elif crack_time_sec < 86400:
        return f"{int(crack_time_sec / 3600)} hours"
    elif crack_time_sec < 2592000:
        return f"{int(crack_time_sec / 86400)} days"
    elif crack_time_sec < 31104000:
        return f"{int(crack_time_sec / 2592000)} months"
    else:
        return f"{int(crack_time_sec / 31104000)} years"

def detect_patterns(password):
    patterns = []
    if password.lower() in ['password', '123456', 'qwerty']:
        patterns.append("Common password")
    if any(password.lower().startswith(word) for word in ['abc', '123', 'qwe']):
        patterns.append("Starts with predictable sequence")
    if password.isdigit():
        patterns.append("Only numbers")
    if password.isalpha():
        patterns.append("Only letters")
    return patterns

def check_breach(password):
    sha1_pw = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_pw[:5], sha1_pw[5:]
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)
    hashes = (line.split(':') for line in response.text.splitlines())
    return any(h == suffix for h, count in hashes)

# --------------------------- Password Generator ---------------------------

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# --------------------------- Report Export ---------------------------

def export_report(password, entropy, crack_time, patterns, breached):
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        c = canvas.Canvas(file_path)
        c.setFont("Helvetica", 12)
        c.drawString(50, 800, f"Password Strength Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        c.drawString(50, 770, f"Password: {password}")
        c.drawString(50, 750, f"Entropy: {entropy} bits")
        c.drawString(50, 730, f"Estimated Crack Time: {crack_time}")
        c.drawString(50, 710, f"Patterns Detected: {', '.join(patterns) if patterns else 'None'}")
        c.drawString(50, 690, f"Breached: {'Yes' if breached else 'No'}")
        c.save()
        messagebox.showinfo("Export Success", f"Report saved at:\n{file_path}")

# --------------------------- GUI App ---------------------------

class PasswordAnalyzerApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Password Strength Analyzer Pro")
        self.root.geometry("600x500")
        self.history = []
        self.dark_mode = False

        self.build_ui()

    def build_ui(self):
        self.style = ttk.Style(self.root)
        self.set_theme()

        # Entry
        ttk.Label(self.root, text="Enter Password:").pack(pady=5)
        self.pw_var = tk.StringVar()
        self.pw_entry = ttk.Entry(self.root, textvariable=self.pw_var, width=40, show="*")
        self.pw_entry.pack(pady=5)

        # Analyze
        ttk.Button(self.root, text="Analyze", command=self.analyze_password).pack(pady=5)

        # Output
        self.output = tk.Text(self.root, height=10, width=70, state='disabled', wrap='word')
        self.output.pack(pady=5)

        # Buttons
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Generate Password", command=self.insert_generated_password).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Copy Password", command=self.copy_password).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Export Report", command=self.export_last_report).grid(row=0, column=2, padx=5)
        ttk.Button(btn_frame, text="Toggle Theme", command=self.toggle_theme).grid(row=0, column=3, padx=5)

        # History
        ttk.Label(self.root, text="History:").pack()
        self.history_box = tk.Listbox(self.root, height=5)
        self.history_box.pack(fill="x", padx=10)

    def set_theme(self):
        if self.dark_mode:
            self.root.configure(bg="#1e1e1e")
            self.style.theme_use("clam")
            self.style.configure("TLabel", background="#1e1e1e", foreground="white")
            self.style.configure("TButton", background="#333", foreground="white")
        else:
            self.root.configure(bg="SystemButtonFace")
            self.style.theme_use("default")

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.set_theme()

    def analyze_password(self):
        pw = self.pw_var.get()
        if not pw:
            messagebox.showwarning("Empty Input", "Please enter a password.")
            return

        entropy = calculate_entropy(pw)
        crack_time = estimate_crack_time(pw)
        patterns = detect_patterns(pw)
        breached = check_breach(pw)

        result = f"""
Password: {pw}
Entropy: {entropy} bits
Estimated Crack Time: {crack_time}
Patterns Detected: {', '.join(patterns) if patterns else 'None'}
Breached: {'Yes 😢' if breached else 'No ✅'}
"""
        self.output.configure(state='normal')
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, result.strip())
        self.output.configure(state='disabled')

        self.history.append(pw)
        self.history_box.insert(tk.END, pw)

        # Store for export
        self.last_result = (pw, entropy, crack_time, patterns, breached)

    def insert_generated_password(self):
        new_pw = generate_strong_password()
        self.pw_var.set(new_pw)

    def copy_password(self):
        pw = self.pw_var.get()
        if pw:
            pyperclip.copy(pw)
            messagebox.showinfo("Copied", "Password copied to clipboard.")

    def export_last_report(self):
        if hasattr(self, "last_result"):
            export_report(*self.last_result)
        else:
            messagebox.showwarning("No Analysis", "Analyze a password first.")

# --------------------------- Run App ---------------------------

if _name_ == "_main_":
    root = tk.Tk()
    app = PasswordAnalyzerApp(root)
    root.mainloop()
