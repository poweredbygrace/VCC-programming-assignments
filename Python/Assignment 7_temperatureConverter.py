from graphics import *
from myButton import myButton

def main():
    def cel_to_far(celsius):
        return (celsius * 9 / 5) + 32

    def far_to_cal(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    win = GraphWin("Temperature Converter", 400, 400)

    celsius_label = Text(Point(150, 50), "Celsius Temperature:")
    celsius_label.draw(win)
    celsius_input = Entry(Point(300, 50), 10)
    celsius_input.draw(win)

    fahrenheit_label = Text(Point(150, 250), "Fahrenheit:")
    fahrenheit_label.draw(win)
    fahrenheit_input = Entry(Point(300, 250), 10)
    fahrenheit_input.draw(win)

    cel_to_far_but = myButton(Point(100, 150), 50, 20, "red", "C to F", win)
    far_to_cel_but = myButton(Point(250, 150), 50, 20, "green", "F to C", win)
    quit_button = myButton(Point(175, 300), 50, 20, "blue", "Quit", win)

    while True:
        click_point = win.getMouse()

        if cel_to_far_but.isClicked(click_point):
            try:
                celsius_value = float(celsius_input.getText())
                fahrenheit_result = cel_to_far(celsius_value)
                fahrenheit_input.setText(f"{fahrenheit_result:.2f}")
            except ValueError:
                fahrenheit_input.setText("Invalid input")

        elif far_to_cel_but.isClicked(click_point):
            try:
                fahrenheit_value = float(fahrenheit_input.getText())
                celsius_result = far_to_cal(fahrenheit_value)
                celsius_input.setText(f"{celsius_result:.2f}")
            except ValueError:
                celsius_input.setText("Invalid input")

        elif quit_button.isClicked(click_point):
            break

    win.close()


if __name__ == "__main__":
    main()
