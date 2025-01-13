import turtle

def koch_curve(t, order, size):
    """Recursive function to draw a Koch curve segment."""
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    """Draw a full Koch snowflake with the specified recursion order."""
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Koch Snowflake Fractal")

    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Draw the Koch snowflake
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

if __name__ == "__main__":
    try:
        order = int(input("Enter the recursion level for the Koch Snowflake (e.g., 3): "))
        draw_koch_snowflake(order)
    except ValueError:
        print("Please enter a valid integer for the recursion level.")