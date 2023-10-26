name1 = input("Your name: ")
name2 = input("Girlfriend's / Boyfriend's name: ")

love = len(name1) + len(name2)

if len(name1) > len(name2):
    love -= 5
else:
    love += 3

love *= 42
love = love / (100 + len(name2))

love = 10 if love > 10 else round(love, 0)

print("{} and {} score is {} out of 10".format(name1, name2, love))