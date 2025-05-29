def get_input(prompt):
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
        exit()

def print_error(message):
    print(f"[ERROR] {message}")