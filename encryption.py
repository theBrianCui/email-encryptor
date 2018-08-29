import sys
password = "applesandoranges"
index = 0

plaintext = sys.stdin.read()
output = ""

for letter in plaintext:
    output = output + chr(ord(password[index]) ^ ord(letter))
    index = (index + 1) % len(password)

sys.stdout.write(output)
