# Top secret encryption formula
# Usage: cat input.txt | python3 encryption.py

import sys
password = "applesandoranges"
index = 0

plaintext = sys.stdin.read()
output = ""

for letter in plaintext:
    output = output + chr(ord(password[index]) ^ ord(letter))
    index = (index + 1) % len(password)

sys.stdout.write(output)
