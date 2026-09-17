# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: InterviewNotes
ANSI = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'underline': '\033[4m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'black': '\033[30m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
}

def colorize(text, color_key, enabled=True):
    if not enabled:
        return text
    return ANSI.get(color_key, '') + text + ANSI['reset']

def success(text, enabled=True):
    return colorize(text, 'green', enabled)

def error(text, enabled=True):
    return colorize(text, 'red', enabled)

def warning(text, enabled=True):
    return colorize(text, 'yellow', enabled)

def info(text, enabled=True):
    return colorize(text, 'blue', enabled)

def dimmed(text, enabled=True):
    return colorize(text, 'dim', enabled)
