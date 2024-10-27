def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            if snake_case:
                snake_case += '_'
            snake_case +=char.lower()
        else:
            snake_case += char