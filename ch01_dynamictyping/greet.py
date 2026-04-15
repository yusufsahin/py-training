def greet(name):
    """
    Greet the person with the given name.
    Parameters:
    name (str):The name of the person to greet.
    Returns:
    str:A greeting message.
    """
    return f"Hello, {name}!"
print(greet.__doc__)
print(greet("John"))