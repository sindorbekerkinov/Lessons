# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiritning: ")
#         baholar[ism] = baho
#     return baholar
# talabalar = ['ali', 'vali', 'hasan','husan']
# baholar = bahola(talabalar)
# print(baholar)

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()
#         print(matnlar[i])
#
# ismlar = ['ali', 'vali', 'hasan','husan']
# katta_harf(ismlar)
# print(ismlar)



# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiritning: ")
#         baholar[ism] = baho
#     return baholar
#
# baholar = bahola(talabalar)
# print(baholar)


# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1,2))
# print(summa(1,2,3,4,5))




# def summa(*sonlar):
#     return sum(sonlar)
# print(summa(1,2,3,4,5))


#
# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)
# print(summa(1,2,3,4,5))
#
# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qay.funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
# avto1 = avto_info("Gm", "malibu",rang ='qora', yil=2018)
# avto2 = avto_info("kia","k5", rang='qizil', narh='300000$')
# print(avto1,avto2)





























