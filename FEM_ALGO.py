import tkinter as tk
from tkinter import messagebox
import webbrowser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# ---------------- COLORS ----------------
BG = "#FFE4EC"
SIDEBAR = "#E0BBE4"
BTN = "#C77DFF"
ACCENT = "#FF8FAB"

# ---------------- DATA ----------------
class User:
    def _init_(self):
        self.name = ""
        self.age = 0
        self.height = 0
        self.weight = 0
        self.cycles = []
        self.avgCycle = 28
        self.lastDay = 1

user = User()

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("FEM-ALGO 🌸")
root.geometry("1000x650")
root.config(bg=BG)

sidebar = tk.Frame(root, bg=SIDEBAR, width=220)
main = tk.Frame(root, bg=BG)

# ---------------- CLEAR ----------------
def clear():
    for w in main.winfo_children():
        w.destroy()

# ---------------- START SCREEN ----------------
def start_screen():
    sidebar.pack_forget()
    main.pack(expand=True, fill="both")
    clear()

    tk.Label(main, text="🌸 FEM-ALGO", font=("Arial", 32, "bold"),
             bg=BG, fg="#6A0572").pack(pady=20)

    tk.Label(main, text="Your AI Wellness Companion 💖",
             font=("Arial", 14), bg=BG).pack(pady=10)

    entries = {}
    fields = ["Name", "Age", "Height (cm)", "Weight (kg)"]

    for f in fields:
        frame = tk.Frame(main, bg=BG)
        frame.pack(pady=6)

        tk.Label(frame, text=f, width=18, bg=BG).pack(side="left")
        e = tk.Entry(frame)
        e.pack(side="right")
        entries[f] = e

    def start_app():
        try:
            user.name = entries["Name"].get()
            user.age = int(entries["Age"].get())
            user.height = float(entries["Height (cm)"].get())
            user.weight = float(entries["Weight (kg)"].get())

            sidebar.pack(side="left", fill="y")
            dashboard()

        except:
            messagebox.showerror("Error", "Enter valid details")

    tk.Button(main, text="Start 💖", bg=ACCENT, fg="white",
              command=start_app, width=15).pack(pady=20)

# ---------------- DASHBOARD ----------------
def dashboard():
    main.pack(side="right", expand=True, fill="both")
    clear()

    tk.Label(main, text=f"🌸 Welcome {user.name}",
             font=("Arial", 24, "bold"), bg=BG).pack(pady=20)

    next_day = user.lastDay + user.avgCycle

    tk.Label(main, text=f"Next Period: Day {next_day}", bg=BG).pack()
    tk.Label(main, text=f"Age: {user.age} | Height: {user.height} cm | Weight: {user.weight} kg",
             bg=BG).pack(pady=10)

# ---------------- GRAPH ----------------
def show_graph():
    if not user.cycles:
        messagebox.showinfo("No Data", "Track cycles first")
        return

    clear()

    fig = plt.Figure(figsize=(5,4), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot(user.cycles, marker='o')
    ax.set_title("Cycle Trend")
    ax.set_xlabel("Cycle Number")
    ax.set_ylabel("Days")

    canvas = FigureCanvasTkAgg(fig, master=main)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

# ---------------- TRACK ----------------
def track():
    clear()

    tk.Label(main, text="🩸 Track Cycle Length", bg=BG, font=("Arial", 16)).pack(pady=20)

    entry = tk.Entry(main)
    entry.pack()

    def save():
        try:
            val = int(entry.get())
            user.cycles.append(val)
            user.avgCycle = sum(user.cycles) // len(user.cycles)
            messagebox.showinfo("Saved", "Cycle added")
        except:
            messagebox.showerror("Error", "Enter valid number")

    tk.Button(main, text="Save", bg=BTN, command=save).pack(pady=10)
    tk.Button(main, text="Show Graph", bg=BTN, command=show_graph).pack()

# ---------------- PCOS ----------------
def pcos():
    clear()

    tk.Label(main, text="🧬 PCOS / PCOD Check", bg=BG, font=("Arial", 18)).pack(pady=20)

    vars = []
    symptoms = [
        "Irregular periods", "Acne", "Weight gain",
        "Hair loss", "Facial hair", "Mood swings",
        "Dark skin patches", "Fatigue"
    ]

    for s in symptoms:
        v = tk.IntVar()
        tk.Checkbutton(main, text=s, variable=v, bg=BG).pack(anchor="w")
        vars.append(v)

    def check():
        score = sum(v.get() for v in vars)

        if score >= 5:
            msg = "⚠ High Risk → Consult doctor"
        elif score >= 3:
            msg = "⚠ Moderate Risk"
        else:
            msg = "✔ Low Risk"

        messagebox.showinfo("Result", msg)

    tk.Button(main, text="Check", bg=BTN, command=check).pack(pady=20)

# ---------------- MOOD ----------------
def mood():
    clear()

    tk.Label(main, text="😊 Mood Booster", bg=BG, font=("Arial", 18)).pack(pady=20)

    entry = tk.Entry(main)
    entry.pack()

    def analyze():
        try:
            score = int(entry.get())

            if score <= -3:
                msg = "💔 Very Low\nTry:\n• Music\n• Talk to friend\n• Rest"
            elif score <= 0:
                msg = "😐 Neutral\nTry:\n• Walk\n• Relax"
            else:
                msg = "😊 Happy!\nKeep shining 💖"

            messagebox.showinfo("Mood", msg)
        except:
            messagebox.showerror("Error", "Enter valid number")

    tk.Button(main, text="Analyze", bg=BTN, command=analyze).pack(pady=10)

    tk.Label(main, text="🎧 Soft Music Apps:", bg=BG).pack(pady=10)
    tk.Button(main, text="Spotify", bg=BTN,
              command=lambda: webbrowser.open("https://open.spotify.com")).pack()
    tk.Button(main, text="YouTube", bg=BTN,
              command=lambda: webbrowser.open("https://youtube.com")).pack()

# ---------------- SHOP ----------------
def shop():
    clear()

    tk.Label(main, text="🛒 FEM-ALGO SHOP", font=("Arial", 18, "bold"), bg=BG).pack(pady=20)

    def buy(item, price):
        messagebox.showinfo("Order", f"{item} (₹{price}) ordered successfully 💖")

    # Pads
    tk.Label(main, text="🩸 Pads", bg=BG, font=("Arial", 14)).pack()
    pads = [
        ("Whisper", [("Regular", 80), ("XL", 120), ("XXL", 150)]),
        ("Stayfree", [("Regular", 70), ("Large", 110)]),
        ("Sofy", [("XL", 130), ("XXL", 160)]),
        ("Carefree", [("Regular", 60), ("XL", 100)])
    ]

    for brand, sizes in pads:
        frame = tk.Frame(main, bg=BG)
        frame.pack(pady=5)

        tk.Label(frame, text=brand, bg=BG, width=12).pack(side="left")

        for size, price in sizes:
            tk.Button(frame, text=f"{size} ₹{price}", bg=BTN,
                      command=lambda b=brand, s=size, p=price: buy(f"{b} {s} Pads", p)
                      ).pack(side="left", padx=5)

    # Chocolates
    tk.Label(main, text="\n🍫 Chocolates", bg=BG, font=("Arial", 14)).pack()
    chocolates = [
        ("Dairy Milk", 50),
        ("Bournville", 100),
        ("Ferrero Rocher", 300),
        ("KitKat", 40),
        ("Snickers", 50),
        ("Lindt", 400),
        ("Galaxy", 120)
    ]

    for name, price in chocolates:
        tk.Button(main, text=f"{name} ₹{price}", bg=BTN,
                  command=lambda n=name, p=price: buy(n, p)).pack(pady=2)

    # Hampers
    tk.Label(main, text="\n🎁 Gift Hampers", bg=BG, font=("Arial", 14)).pack()
    hampers = [
        ("Mini Care Kit", 250),
        ("Comfort Box", 500),
        ("Premium Hamper", 800),
        ("Luxury Kit", 1200)
    ]

    for name, price in hampers:
        tk.Button(main, text=f"{name} ₹{price}", bg=BTN,
                  command=lambda n=name, p=price: buy(n, p)).pack(pady=3)

# ---------------- DOCTORS ----------------
def doctors():
    clear()

    tk.Label(main, text="👩‍⚕️ Gynecologists Near You", font=("Arial", 18, "bold"), bg=BG).pack(pady=20)

    doctors_list = [
        ("Dr Bhavna Gulati", "Ballupur, Dehradun"),
        ("Dr Anshu Kakkar", "Rajpur Road, Dehradun"),
        ("Dr Vibha Parihar", "EC Road, Dehradun"),
        ("Dr Sumita Prabhakar", "Patel Nagar, Dehradun"),
        ("Luthra Nursing Home", "Haridwar Road, Dehradun")
    ]

    def book(name):
        messagebox.showinfo("Appointment", f"Appointment booked with {name} 💖")

    for name, location in doctors_list:
        frame = tk.Frame(main, bg=BG)
        frame.pack(pady=6, padx=20, fill="x")

        tk.Label(frame, text=f"{name} 📍 {location}", bg=BG).pack(side="left")
        tk.Button(frame, text="Book", bg=BTN,
                  command=lambda n=name: book(n)).pack(side="right")

# ---------------- SIDEBAR ----------------
menu = [
    ("Dashboard", dashboard),
    ("Track + Graph", track),
    ("PCOS Check", pcos),
    ("Mood + Music", mood),
    ("Shop", shop),
    ("Doctors", doctors)
]

for text, cmd in menu:
    tk.Button(sidebar, text=text, bg=BTN, width=18, command=cmd).pack(pady=8)

# ---------------- START ----------------
start_screen()
root.mainloop()