from hashlib import sha256
x = 5
y = 0  # We don't know what y should be yet...
z = x*y
# print(sha256(f"{z}".encode()).hexdigest()[-1])
while sha256("{} * {}".format(x,y).encode()).hexdigest()[-1] != "0":
    y += 1
print("The solution is y = {}".format(y))
print(sha256(str("5 * 21").encode()).hexdigest())
