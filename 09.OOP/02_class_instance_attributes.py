# Class attributes (static) are shared across all instances
# Instance attributes are independent/unique per instance


class Player:
    MAX_POSITION = 10  # Class attributes are shared across all instances

    def __init__(self, position):
        if position <= Player.MAX_POSITION:
            self.position = position
        else:
            self.position = Player.MAX_POSITION


# class Player {
#   static readonly MAX_POSITION: number = 10; # static attribute
#   constructor(public position: number) {
#     if (position > Player.MAX_POSITION) {
#       this.position = Player.MAX_POSITION;
#     }
#   }
# }

p1 = Player(11)
p2 = Player(12)

print("Position of p1 and p2 before assignment:")
print(p1.position)
print(p2.position)

p1.position = 8
p2.position = 9

# Instance attributes are independent
print(
    "Instance attributes are independent, we can assign different values to each instance"
)
print(p1.position)
print(p2.position)

print("Class attributes are shared across all instances")
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)

# Class attributes are shared across all instances
Player.MAX_POSITION = 15

print("When we modify one class attribute, it affects all instances")
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)
