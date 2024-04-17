from enum import Enum


class MessageType(Enum):
    ERROR = "error"
    WARN = "warn"
    INFO = "info"
    SUCCESS = "success"


def print_color(message, type):
    colors = {
        "reset": "\033[0m",
        "error": "\033[91m",  # red
        "warn": "\033[93m",
        "info": "\033[94m",  # blue
        "success": "\033[92m"
    }

    color = colors.get(type, colors["reset"])
    print(color + message + colors["reset"])
