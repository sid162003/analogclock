import tkinter as tk
import time
import math

class Clock:
    def __init__(self):
        self.root = tk.Tk()  
        self.root.title("Analog Clock")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='white')
        self.canvas.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.localtime()
        self.canvas.delete("all")
        origin_x = 200
        origin_y = 200
        self.canvas.create_oval(40, 40, 360, 360, width=5)

        for i in range(1, 13):
            x = origin_x + 150 * math.sin(math.radians(i * 30))
            y = origin_y - 150 * math.cos(math.radians(i * 30))
            self.canvas.create_text(x, y, text=str(i), font=('Arial', 12))

        hour_angle = (now.tm_hour % 12 + now.tm_min / 60) * 30
        minute_angle = now.tm_min * 6
        second_angle = now.tm_sec * 6

        self.draw_hand(origin_x, origin_y, hour_angle, 100, 5)
        self.draw_hand(origin_x, origin_y, minute_angle, 120, 3)
        self.draw_hand(origin_x, origin_y, second_angle, 140, 1)

        self.canvas.after(1000, self.update_clock)

    def draw_hand(self, origin_x, origin_y, angle, length, width):
        end_x = origin_x + length * math.sin(math.radians(angle))
        end_y = origin_y - length * math.cos(math.radians(angle))
        self.canvas.create_line(origin_x, origin_y, end_x, end_y, width=width)

if __name__ == "__main__":
    clock = Clock()
