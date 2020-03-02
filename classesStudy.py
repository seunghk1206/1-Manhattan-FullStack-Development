# class Dog():
#     def __init__(self): #rule of python !!
#         print("Initiate anyways")
#     def speak(self, name):
#         print(name, "Bark!")
# KSH = Dog()
# Dan = Dog()
# KSH.speak('김승현')

class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("my name is ", self.name, self.age, "살 입니다.")
    def change_age(self, age):
        self.age = age
    def add_weight(self, weight):
        self.weight = weight
kim = Cat('Youngho', 88) 
#instance
kim2 = Cat('SeungHyeon', 90)
kim.speak()
kim2.speak()
kim.change_age(87)
kim.speak()
kim2.add_weight(150)
kim2.speak()
print("Get Weight: ", kim2.weight)
print(kim2.weight, kim.age, kim2.name)


# class player(object):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.velocity = 5
#         self.left = False
#         self.right = False
#         self.walkCount = 0 #standing 
#         self.isJump = False
#         self.jumpCount = 5

#     def draw(self, screen):
#         if self.walkCount + 1 >= 27:
#             self.walkCount = 0
#         if self.left:
#             screen.blit(walkLeft[self.walkCount//3],(self.x, self.y)) # //3 -> 나머지 값을 제외 한 몫
#             self.walkCount += 1
#         elif self.right:
#             screen.blit(walkRight[self.walkCount//3],(self.x,self.y))
#             self.walkCount += 1 
#         else:
#             screen.blit(char, (self.x, self.y))
#             self.walkCount = 0