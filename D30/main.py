

# file not found
# try:
#     file = open(r"D30\a.txt")
# except FileNotFoundError:
#     # print("there was an error")
#     file = open(r"D30\a.txt", "w")
#     file.write("abd")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)

# finally:
#     raise TypeError("This is an error")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)