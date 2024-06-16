def execute_help_command(commands):
    print("\nAvailable commands:")
    for command, description in commands.items():
        print(f"  {command:<8} - {description}")
    print("")

