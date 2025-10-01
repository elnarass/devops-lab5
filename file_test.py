# Файл жасау және оған жазу
with open("test.txt", "w") as f:
    f.write("Hello system calls!\n")

# Файлдан оқу
with open("test.txt", "r") as f:
    content = f.read()
    print("Мазмұны:", content)
