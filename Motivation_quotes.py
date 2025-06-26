import tkinter as tk
import random

quotes = [
    "Believe you can and you're halfway there.",
    "Push yourself, because no one else is going to do it for you.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Success is what comes after you stop making excuses.",
    "Dream it. Wish it. Do it.",
    "It always seems impossible until it’s done.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Little things make big days.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Stay positive. Work hard. Make it happen."
]

def show_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)

# GUI Setup
root = tk.Tk()
root.title("Motivation Booster")
root.geometry("700x350+300+200")
root.config(bg="#E9F8F9")
root.resizable(False, False)

# Header
header_frame = tk.Frame(root, width=700, height=60, bg="#006C67")
header_frame.place(x=0, y=0)

header_label = tk.Label(header_frame, text="💬 Daily Motivation 💪", font=("Times New Roman", 26, "bold"), bg="#006C67", fg="#000000")
header_label.place(relx=0.5, rely=0.5, anchor="center")

divider = tk.Frame(root, bg="#102542", height=5, width=700)
divider.place(x=0, y=60)

# Quote Label
quote_label = tk.Label(root, text="", font=("Georgia", 18), wraplength=600, justify="center", bg="#E9F8F9", fg="#000000")
quote_label.place(relx=0.5, rely=0.5, anchor="center")

# Generate Button
generate_btn = tk.Button(root, text="✨ New Quote", font=("Times New Roman", 16, "bold"), bg="#006C67", fg="#000000", command=show_quote)
generate_btn.place(relx=0.5, rely=0.85, anchor="center")

root.mainloop()