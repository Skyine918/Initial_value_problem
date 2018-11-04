from tkinter import *
from calc import InitialValueMethods
import matplotlib.pyplot as plt


class Drawer:

    ivm = InitialValueMethods()

    def draw_euler(self):
        plt.cla()

        plt.title("Function  y = 2*x - 1 + e^(-2*x)  ")

        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")

        plt.legend(["exact solution", "euler Method"])
        plt.grid()

        cords = self.ivm.excact_method()
        plt.plot(cords[0], cords[1])

        cords = self.ivm.euler_method()
        plt.plot(cords[0], cords[1])

        plt.show()

    def draw_euler_improved(self):

        plt.cla()

        plt.title("Function  y = 2*x - 1 + e^(-2*x)  ")

        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")

        plt.legend(["exact solution", "euler improved Method"])
        plt.grid()

        cords = self.ivm.excact_method()
        plt.plot(cords[0], cords[1])

        cords = self.ivm.euler_method_improved()
        plt.plot(cords[0], cords[1])

        plt.show()

    def draw_runge_kutta(self):

        plt.cla()

        plt.title("Function  y = 2*x - 1 + e^(-2*x)  ")

        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")

        plt.legend(["exact solution", "Runge-Kutta Method"])
        plt.grid()

        cords = self.ivm.excact_method()
        plt.plot(cords[0], cords[1])

        cords = self.ivm.runge_kutta_method()
        plt.plot(cords[0], cords[1])

        plt.show()

    def start(self):
        root = Tk()
        root.title("Initial Value Problem")
        root.geometry("300x250")

        steps = ""
        message_entry = Entry(textvariable=steps)
        message_entry.place(relx=.5, rely=.1, anchor="c")

        button_euler = Button(text="Euler simple", command=self.draw_euler)
        button_euler.place(relx=.5, rely=.5, anchor="c")

        button_euler_improved = Button(text="Euler Improved", command=self.draw_euler_improved)
        button_euler_improved.place(relx=.15, rely=.5, anchor="c")

        button_runge_kutta = Button(text="Runge-Kutta", command=self.draw_runge_kutta)
        button_runge_kutta.place(relx=.85, rely=.5, anchor="c")

        root.mainloop()


