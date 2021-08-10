# IMPORTS
import tkinter as TK

# VARIABLES
# Use a boolean variable to help control state of time (running or not running)
running = False
# time variables initially set to 0
hours, minutes, seconds = 0, 0, 0

# NOTES ON GLOBAL
# Global will be used to modify variables outside functions
# Another option would be to use a class and subclass Frame

# FUNCTIONS
# The start, pause, and reset functions will be called when the buttons are clicked

# Starting the function
def start():
    global running
    if not running:
        update()
        running = True

# Pausing the function
def pause():
    global running
    if running:
        # Cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

# Reset function
def reset():
    global running
    if running:
        # Cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

    # Set variables back to zero
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    # Set label back to zero
    stopwatch_label.config(text='00:00:00')

# Update stopwatch function
def update():
    # Update seconds with (addition) compound assignment operator
    global hours, minutes, seconds
    seconds += 1

    if seconds == 60:
       minutes += 1
       seconds = 0

    if minutes == 60:
       hours += 1
       minutes = 0
    # Format time to include leading zeros

    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    # Update timer label after 1000 ms (1 second)
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # After each second (1000 milliseconds), call update function
    # Use update_time variable to cancel or pause the time using after_cancel

    global update_time
    update_time = stopwatch_label.after(1000, update)

# WIDGETS
# Create main window
root = TK.Tk()
root.geometry('485x220')
root.title('Stopwatch')

# Label to display time
stopwatch_label = TK.Label(text='00:00:00', font=('Arial', 80))
stopwatch_label.pack()

# Start, pause, reset, quit buttons
start_button = TK.Button(text='Start', height=5, width=7, font=('Arial', 20), command=start)
start_button.pack(side=TK.LEFT)
pause_button = TK.Button(text='Pause', height=5, width=7, font=('Arial', 20), command=pause)
pause_button.pack(side=TK.LEFT)
reset_button = TK.Button(text='Reset', height=5, width=7, font=('Arial', 20), command=reset)
reset_button.pack(side=TK.LEFT)
quit_button = TK.Button(text='Quit', height=5, width=7, font=('Arial', 20), command=root.quit)
quit_button.pack(side=TK.LEFT)

# MAINLOOP
# Run app
root.mainloop()