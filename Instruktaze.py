
# #Pomoc z wykonywaniem zadan


# #Listy obiektow

# lst_obiektow = []

# class Obiekt:
#     def __init__(self,a,b,c) -> None:
#         self.zmienna1 = a
#         self.zmienna2 = b
#         self.zmienna3 = c

#     def inf(self):
#         print(self.zmienna1)
#         print(self.zmienna2)
#         print(self.zmienna3)
    
#     def zmien(self):
#         self.zmienna1 = float(input())
#         self.zmienna2 = float(input())
#         self.zmienna3 = float(input())

# lst_obiektow.append(Obiekt(2,4,6))      #by uzyskac liste obiektow ktorych funkcje mozna
#                                         #wywolac trzeba je dodawac w taki sposob
# lst_obiektow[0].inf()
# lst_obiektow[0].zmien()
# lst_obiektow[0].inf()

# #Dziedziczenie_kilku elementow========================================================================================================

# class Element1():
#     def __init__(self) -> None:
#         self.cecha1 = 1
    
#     def zmien1(self):
#         self.cecha1 = float(input())

#     def inf1(self):
#         print(self.cecha1)

# class Element2():
#     def __init__(self) -> None:
#         self.cecha2 = 1
    
#     def zmien2(self):
#         self.cecha2 = float(input())

#     def inf2(self):
#         print(self.cecha2)

# class Element3:
#     def __init__(self) -> None:
#         self.cecha3 = 1
    
#     def zmien3(self):
#         self.cecha3 = float(input())

#     def inf3(self):
#         print(self.cecha3)

# class Calosc():                 #nie moznadziedziczyc wiecej niz jednje classy 
#     def __init__(self):         #ale za ro mozna zapisac je jako obiekty
#         self.elm1 = Element1()
#         self.elm2 = Element2()
#         self.elm3 = Element3()
    
#     def inf(self):
#         self.elm1.inf1()
#         self.elm2.inf2()
#         self.elm3.inf3()
    
#     def zmien(self):
#         self.elm1.zmien1()
#         self.elm2.zmien2()
#         self.elm3.zmien3()
    
# x = Calosc()

# x.inf()
# x.zmien()
# x.inf()



