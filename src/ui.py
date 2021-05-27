from rich import print
from os import system, name

def banner():
    """
    Returns the application banner
    """

    with open('src/banner.txt') as file:
        content = file.read()
        return print(f"[bold yellow]{content}[/]")

def clear():
    system('cls' if name == 'nt' else 'clear')