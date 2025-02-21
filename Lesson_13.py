# class Talaba:
#     """Talaba nomli klas yaratamiz"""
#     def __init__(self, ism,familya,tyil):
#         """Talabaning xusiyatlari"""
#         self.ism = ism
#         self.familya = familya
#         self.tyil = tyil
#
# # talaba1 = Talaba("Sindorbek","Erkinov",2006)
# # print(talaba1.ism, talaba1.tyil)




class Talaba:
    """Talaba nomli klas yaratamiz"""

    def __init__(self, ism, familya, tyil):
        """Talabaning xusiyatlari"""
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
        self.bosqich = 1

    def tanishtir(self):
         print(f"Ismim {self.ism} {self.familya}. {self.tyil} yilda tug'ilganman")

    def get_name(self):
         return self.ism

    def get_lastname(self):
         return self.familya

    def get_fullname(self):
         return f"{self.ism} {self.familya}"

    def get_age(self, yil):
        """Talabaning yoshini kiritadi"""
        return yil-self.tyil
    def get_info(self):
        return f"{self.ism} {self.familya}. {self.bosqich}-bosqich talabasi"

    def set_bosqich(self, bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich
    def update_bosqich(self):
        self.bosqich += 1

class Fan():
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni +=1

matematika = Fan("Oliy Matematika")
talaba1 = Talaba ("Sindorbek" ,"Valiyev" ,2005)


matematika.add_student(talaba1)

print(matematika.talabalar_soni)



























# talaba1 = Talaba("Alijon","Valiyev",2003)
# talaba2 = Talaba("xdexdexd", "dxxd4xde",1233)
# talaba3 = Talaba("dxdxe","xdedxe",1212)
# # print(talaba2.get_name(), talaba1.get_fullname())
# # print(talaba1.get_age(2025))
# # talaba1 = Talaba("Sindorbek" , "Erkinov",2006)
# talaba1.update_bosqich()
# talaba1.update_bosqich()
# talaba1.update_bosqich()
# print(talaba1.get_info())






























































