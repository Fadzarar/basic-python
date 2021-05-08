# class class_saya:
# 	def __init__(self, name, age):
# 		self.nama = name
# 		self.umur = age
# 	def intro(self):
# 		print(f"My Name Is {self.nama}")
# 	def leaving(self):
# 		print(f"Good Bye!")

# orang1 = class_saya("Fadzar","18")
# orang2 = class_saya("Dovahkiin","35")
# # print(orang1.nama)
# # print(orang2.nama)
# # print( )
# # print(orang1.umur)
# # print(orang2.umur)
# orang1.intro()
# orang2.intro()
# print( )
# orang1.leaving()
# orang2.leaving()


def num1(x):
   def num2(y):
      return x * y
   return num2

print(num1(10)(20))