from CTkMessagebox import CTkMessagebox

def show_check(message):
    CTkMessagebox(message=message, icon="check", option_1="OK")

def show_error(title, message):
    CTkMessagebox(title=title, message=message, icon="cancel")