import re

def update_key_positions(match):
    content = match.group(1)
    numbers = [int(x) for x in content.split()]
    new_numbers = []
    for num in numbers:
        if num < 11:
            new_num = num
        elif 11 <= num <= 21:
            new_num = num + 1
        elif 22 <= num <= 32:
            new_num = num + 2
        elif num >= 33:
            new_num = num + 3
        else:
            new_num = num # Should not happen based on logic
        new_numbers.append(str(new_num))
    return f"key-positions = <{' '.join(new_numbers)}>"

with open('config/skeletyl.combos', 'r') as f:
    content = f.read()

new_content = re.sub(r'key-positions = <([^>]+)>', update_key_positions, content)

with open('config/skeletyl.combos', 'w') as f:
    f.write(new_content)
