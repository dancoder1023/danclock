import tkinter as tk
import time

class ElegantClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Dan's Clock (Arch's) Clock")
        self.root.geometry("500x300")
        self.root.configure(bg="#1e1e2e")

        self.gradient_colors = ["#ff6f61", "#fcb045", "#9fe5a0", "#42a5f5", "#7c4dff"]
        self.color_index = 0

        self.clock_label_shadow = tk.Label(
            root,
            font=("Helvetica", 56, "bold"),
            bg="#1e1e2e",
            fg="#2a2a3b",
        )
        self.clock_label_shadow.pack(expand=True)

        self.clock_label = tk.Label(
            root,
            font=("Helvetica", 56, "bold"),
            bg="#1e1e2e",
        )
        self.clock_label.pack(expand=True)

        self.date_label = tk.Label(
            root,
            font=("Helvetica", 16, "italic"),
            bg="#1e1e2e",
            fg="#a8a8b7",
        )
        self.date_label.pack()

        self.quit_button = tk.Button(
            root,
            text="Exit Clock",
            font=("Helvetica", 12, "bold"),
            bg="#ff6f61",
            fg="white",
            command=root.quit,
            relief="flat",
            highlightthickness=0,
        )
        self.quit_button.pack(side="bottom", pady=10)

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%A, %d %B %Y")

        self.clock_label.config(text=current_time, fg=self.gradient_colors[self.color_index])
        self.clock_label_shadow.config(text=current_time)
        self.date_label.config(text=current_date)

        self.color_index = (self.color_index + 1) % len(self.gradient_colors)

        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    clock = ElegantClock(root)
    root.mainloop()
