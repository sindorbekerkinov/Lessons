# # car0 = {
# #     'model':'lacetti',
# #     'rang':'oq',
# #     'yil':2018,
# #     'narh': 13000,
# #     'km':50000,
# #     'korobka':"mexanika"
# # }
# # car1 = {
# #     'model': 'matiz',
# #     'rang': 'qizil',
# #     'yil': 2011,
# #     'narh': 1000,
# #     'km': 502000,
# #     'korobka': "avtomat"
# # }
# # car2 = {
# #     'model': 'cobalt',
# #     'rang': 'qora',
# #     'yil': 2020,
# #     'narh': 130000,
# #     'km': 500450,
# #     'korobka': "avtomat"
# #
# # }
# # cars = [car0, car1, car2]
# # # for car in cars:
# # #     print(f"{car['model'].title()},"
# # #           f"{car['rang']} rang,"
# # #           f"{car['yil']}-yil, {car['narh']}$")
# # print(cars[0])
# # print(cars[0]['model'])
# # print(f"{cars[2]['rang'].title()}"
# #       f"{cars[2]['model']}")
# #
# #
# #
# malibus=[]
# for n in range(10):
#     new_car ={
#         'model':'malibu',
#         'rang':None,
#         "yil":2020,
#         'narh':None,
#         "km":0,
#         'korobka':"avto"
#     }
#     malibus.append(new_car)
#
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'
#
# for malibu in malibus[3:6]:
#     malibu['rang']= 'qora'
#
#
# for malibu in malibus[6:]:
#     malibu['rang']='qora'
#     malibu['korobka']='mexanika'
#
# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narh']=40000
#     else:
#         malibu['narh']=35000
#
# print(malibus)
#

# dasturchilar = {
#     'ali':["python","c++"],
#     "vali":["html","css","js"],
#     "hasan":["php","sql"],
#     'husan':["python","php"],
#     "maryam":["c++","c#"]
# }
#
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi daasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# hamkasblar = {
#     "ali":{"familya":"valiyev",
#            "tyil":1995,
#            "malumot":"oliy",
#            "tillar":["python","c++"]
#            },
#     "ali":{"familya":"valiyev",
#            "tyil":1995,
#            "malumot":"oliy",
#            "tillar":["python","c++"]
#            },
#     "ali":{"familya":"valiyev",
#            "tyil":1995,
#            "malumot":"oliy",
#            "tillar":["python","c++"]
#            }
# }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()},"
#           f"{info['tyil']}-yilda tug'ilgan."
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())
#
# son = 1
# while son<=5:
#     print(son, end=' ')
# #     son = son+1
#
#
# print("Kiritilgan sonni kvadratini ko'rsatuvchi dastur.")
# savol = "Istalgan son kiriting "
# savol +="(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
#
# print("Kiritilgan sonni kvadratini ko'rsatuvchi dastur.")
# savol = "Istalgan son kiriting "
# savol +="(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#
#         print(float(qiymat)**2)
#
# sonlar = list(range(1,10))
# for son in sonlar:
#     if son ==5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")
























#
#
#
#
#
#
#
#
