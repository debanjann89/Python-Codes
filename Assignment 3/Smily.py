import curses

def fill_screen_with_smiling_faces(screen):
    # Get the dimensions of the terminal
    height, width = screen.getmaxyx()

    # Define the smiling face character using its ASCII value
    smiling_face = chr(1)

    # Fill the screen with the smiling face
    for y in range(height):
        for x in range(width):
            screen.addch(y, x, smiling_face)

    # Refresh the screen to display the changes
    screen.refresh()

    # Wait for user input to exit
    screen.getch()

# Initialize the curses screen and run the function
curses.wrapper(fill_screen_with_smiling_faces)
