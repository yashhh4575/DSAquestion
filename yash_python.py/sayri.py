import time

shayari = [
    "Bas chhota sa bahana chahta hoon,",
    "Main tujhe apne gale se lagana chahta hoon.",
    "Chand dino ki mehmaan nahi hai meri mohabbat,",
    "Ta-umr main tujhe apnana chahta hoon. ❤️"
]

for line in shayari:
    for char in line:
        print(char, end="", flush=True)
        time.sleep(0.06)  # typing speed
    print()
    time.sleep(1)  