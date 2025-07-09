import re
import tkinter as tk

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]

    if all(not err for err in errors):
        return "🟢 STRONG - Fortified Password"
    elif sum(errors) <= 2:
        return "🟡 MEDIUM - Upgrade Suggested"
    else:
        return "🔴 WEAK - Security Risk"

def on_check():
    pwd = entry.get()
    
    if not pwd:
        result_label.config(text="⚠️ Please enter a password.", fg="#FF3333")
        return
    
    strength = check_password_strength(pwd)

    if "STRONG" in strength:
        result_label.config(text=strength, fg="#00FF00")
    elif "MEDIUM" in strength:
        result_label.config(text=strength, fg="#FFCC00")
    else:
        result_label.config(text=strength, fg="#FF3333")

root = tk.Tk()
root.title("Sameer Password Monitor")
root.configure(bg="#0f0f0f")
root.geometry("500x300")

tk.Label(
    root, 
    text="INZAMAM PASSWORD CHECKER",
    font=("Consolas", 16, "bold"),
    fg="#39FF14",
    bg="#0f0f0f"
).pack(pady=10)

tk.Label(
    root,
    text="ENTER PASSWORD:",
    font=("Consolas", 12, "bold"),
    fg="#00FFFF",
    bg="#0f0f0f"
).pack()

entry = tk.Entry(
    root,
    show="*",
    font=("Consolas", 14),
    width=30,
    bg="#1a1a1a",
    fg="#00FF00",
    insertbackground="#00FF00",
    relief="flat"
)
entry.pack(pady=10)

tk.Button(
    root,
    text="SCAN PASSWORD",
    command=on_check,
    font=("Consolas", 12, "bold"),
    bg="#39FF14",
    fg="black",
    activebackground="#00aa00",
    relief="flat"
).pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Consolas", 14, "bold"),
    bg="#0f0f0f"
)
result_label.pack(pady=15)

tk.Label(
    root,
    text="Developed by Sameer | CyberSec Mode: ON",
    font=("Consolas", 10),
    fg="#888888",
    bg="#0f0f0f"
).pack(side="bottom", pady=5)

root.mainloop()
