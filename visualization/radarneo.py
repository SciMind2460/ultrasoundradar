import tkinter as tk
import math
import time

# Radar class for Python definition.
class Radar:
    def __init__(self, range_cm: int):
        # Range of the radar in centimeters.
        self.range_cm = range_cm
    def update(self, angle_deg: int, distance: int):
        # Angle in degrees of the radar reading.
        self.angle_deg = angle_deg
        # Distance in centimeters of the radar reading.
        self.distance = distance
    def visualise(self, canvas: tk.Canvas):
        # Clear the canvas.
        canvas.delete("all")
        # Draw the radar circle.
        canvas.create_oval(10, 10, 2*self.range_cm + 10, 2*self.range_cm + 10, outline="green")
        # Draw the range lines.
        canvas.create_line(self.range_cm + 10, 10, self.range_cm + 10, 2*self.range_cm + 10, fill="green")
        canvas.create_line(10, self.range_cm + 10, 2*self.range_cm + 10, self.range_cm + 10, fill="green")
        # Draw the radar line.
        x = self.distance * math.cos(math.radians(self.angle_deg)) + self.range_cm + 10
        y = self.distance * math.sin(math.radians(self.angle_deg)) + self.range_cm + 10
        canvas.create_line(self.range_cm + 10, self.range_cm + 10, x, y, fill="red", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    # Initialization of canvas and root window.
    root.title("Radar Visualization")
    radar = Radar(range_cm=100)
    canvas = tk.Canvas(root, width=2*radar.range_cm + 20, height=2*radar.range_cm + 20, bg="black")
    canvas.pack()
    # Simulate radar updates.
    for i in range(0, 360, 1):
        radar.update(i, 50)
        radar.visualise(canvas)
        root.update()
        time.sleep(0.01)
    root.mainloop()