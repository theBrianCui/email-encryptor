import sys
password = "applesandoranges"
index = 0

for line in sys.stdin:
    output = ""
    for letter in line:
        if letter == "\n" or letter == "\r":
            continue
        output = output + chr(ord(password[index]) ^ ord(letter))
        index = (index + 1) % len(password)
    print(output)
