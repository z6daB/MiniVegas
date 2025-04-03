dict_screens = {}

current_screen = None

def add_screen(screen_name, screen):
    dict_screens[screen_name] = screen

def get_current_screen():
    return current_screen

def change_screen(screen_name):
    global current_screen
    current_screen = dict_screens.get(screen_name)  # Используем get для безопасного доступа
    if current_screen is None:
        raise ValueError(f"Screen with name '{screen_name}' not found!")
    print(f"Changed screen to: {screen_name}")