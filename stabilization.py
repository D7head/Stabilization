import tkinter as tk

class StabilizationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Stabilization")

        self.window_width = 600
        self.window_height = 400

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width // 2) - (self.window_width // 2)
        y = (screen_height // 2) - (self.window_height // 2)
        master.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

        self.master.configure(bg="#4B4B4B")
        self.fixed_x = x + (self.window_width // 2)
        self.fixed_y = y + (self.window_height // 2)

        self.button = tk.Button(master, text="Stabilization", command=self.on_button_click, font=("Arial", 20), width=15, height=3)
        self.update_button_position()
        self.master.bind("<Configure>", self.on_window_move)

    def on_button_click(self):
        print("стабилизация!")

    def on_window_move(self, event):
        self.update_button_position()

    def update_button_position(self):
        window_x = self.master.winfo_x()
        window_y = self.master.winfo_y()
        self.button.place(x=self.fixed_x - window_x, y=self.fixed_y - window_y)

if __name__ == "__main__":
    root = tk.Tk()
    app = StabilizationApp(root)
    root.mainloop()