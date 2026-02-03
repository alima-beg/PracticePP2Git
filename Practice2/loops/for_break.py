fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

for i in range(5):
    if i == 3:
        break
    print(i)

for letter in "Python":
    if letter == "h":
        break
    print(letter)