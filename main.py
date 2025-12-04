# mashiqlar2_0412

#1 - masala
sonlar = [1, 2, 3, 4, 5]
natija = list(map(lambda x: x**3, sonlar))
print(natija)

#2 - masala
sozlar = ["Salom", "Dunyo", "Kitob", "Python"]
natija = list(map(lambda x: x[0], sozlar))
print(natija)

#3 - masala
sonlar = [1, 2, 3, 4, 5, 6]

natija = list(map(lambda x: "Juft" if x % 2 == 0 else "Toq", sonlar))
print(natija)

#4 - masala
a = [1, 2, 3]
b = [4, 5, 6]

natija = list(map(lambda x, y: x * y, a, b))
print(natija)

#5 - masala
matnlar = ["sa123lom", "py!@th#on", "ko45d"]

natija = list(map(lambda x: ''.join(filter(str.isalpha, x)), matnlar))
print(natija)

#6 - masala
sonlar = [2, 3, 4]
daraja = 3

natija = list(map(lambda x: x**daraja, sonlar))
print(natija)
