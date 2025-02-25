class Shaxs:
    """Shaxslar haqida malumot"""
    def __init__(self, ism, familya, passport, tyil):
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
            """Shaxs haqida malumot"""
            info = f"{self.ism} {self.familya}. "
            info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ulgan"
            return info
    def get_age(self, yil):
            """Shaxsni yoshini qaytaruvchi metod"""
            return yil - self.tyil
#
# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self,ism, familya, passport,tyil,idraqam,manzil):
#         """Talabaning xuxusiyatlari"""
#         super().__init__(ism,familya,passport,tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
#     def get_info(self):
#         """Talaba haqida malumot"""
#         info  = f"{self.ism} {self.familya}. "
#         info += f"{self.get_bosqich()} - bosqich. ID raqami: {self.idraqam}"
#         return info
# class Manzil:
#     """Manzil saqlash uchun klass"""
#     def __init__(self,uy,kocha, tuman,viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
#
#     def get_manzil(self):
#         """Manzilni ko'rish"""
#         manzil = f"{self.viloyat} viloyat, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}- uy"
#         return manzil
# talaba_manzil = Manzil(17,"Beruniy", "Yangariq","Xorazm")
# talaba = Talaba("Sindorbek","Erkinov","AD6165436",2006,"2393",talaba_manzil)
# print(f"{talaba.get_info()}")
# print(talaba_manzil.get_manzil())
# print(talaba.manzil.tuman)

#
# from uuid import uuid4
#
# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self,make , model, rang, yil,narh , km=0):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
#     def get_km(self):
#         return self.__km
#
#     def get_id(self):
#         return self.__id
#
#     def add_km(self,km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >=0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")
#
#
#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto
# avto1 = Avto("Gm", "Malibu", "Qora",2020,40000,10000000000)
# avto1 = Avto("Gm", "Malibu", "Qora",2020,40000,10000000000)
# print(avto1.get_km())
# print(avto1.get_id())
# avto1.add_km(200)
# print(avto1.get_num_avto())
#
# def decorator(func):
#     def wrapper():
#         print("Before calling the function.")
#         func()
#         print("After calling the function.")
#     return wrapper
# # Applying the decorator to a function
# @decorator
# def greet():
#     print("Hello, World!")
# greet()






























