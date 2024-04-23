camel = input("camelCase: ").strip()

snake_chars = []

for ch in camel:
    if ch.isupper():
        snake_chars.append('_' + ch.lower())
    else:
        snake_chars.append(ch)

snake = ''.join(snake_chars)

#shorthand if:snake = ''.join(['_' + ch.lower() if ch.isupper() else ch for ch in camel])

print("snake_case:", snake)