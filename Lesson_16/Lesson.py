# import json
# x = 10
# x_json = json.dumps(x)
# print(type(x_json))
#
# ism = "jonibek"
# ism_json = json.dumps(ism)
# print(type(ism_json))
# print(ism_json)
#
# sonlar = [12,23,4444,54,3]
# sonlar_json = json.dumps(sonlar)
# print(type(sonlar_json))
# print(sonlar_json)


import json
#
# bemor = {
#     "ism":"Erkinov Sindorbek",
#     "yosh":30,
#     "oila": True,
#     "farzandlar":("Ahmad","Bonu"),
#     "Alllergiya":None,
#     'dorilar': [
#         {"nomi":"Analgin","miqdori":0.5},
#         {"nomi":"Panadol", "miqdori":1.2}
#     ]
# }
# print(type(bemor))
# bemor_json = json.dumps(bemor)
# print(type(bemor_json))
# print(bemor_json)


# bemor_json = json.dumps(bemor, indent=4)
# print(bemor_json)


#
# import json
#
# bemor = {
#     "ism":"Erkinov Sindorbek",
#     "yosh":30,
#     "oila": True,
#     "farzandlar":("Ahmad","Bonu"),
#     "Alllergiya":None,
#     'dorilar': [
#         {"nomi":"Analgin","miqdori":0.5},
#         {"nomi":"Panadol", "miqdori":1.2}
#     ]
# }
# with open("bemor.json", "w") as f:
#     json.dump(bemor, f, indent=4)

#
# import json
# sonlar = [12, 24,24,43]
# sonlar_json = json.dumps(sonlar)
# bemor = {
#     "ism":"Erkinov Sindorbek",
#     "yosh":30,
#     "oila": True,
#     "farzandlar":("Ahmad","Bonu"),
#     "Alllergiya":None,
#     'dorilar': [
#         {"nomi":"Analgin","miqdori":0.5},
#         {"nomi":"Panadol", "miqdori":1.2}
#     ]
# }
# bemor_json = json.dumps(bemor)
#
# sonlar = json.loads(sonlar_json)
# bemor = json.loads(bemor_json)
# print(type(bemor))
# print(type(sonlar))



# import json
# filename = "bemor.json"
# with open(filename) as f:
#     bemor = json.load(f)
# print(type(bemor))

# data = {
#     "address_components": [
#         {
#             "long_name": "Tinchlik Street",
#             "short_name": "Tinchlik Street",
#             "types": [
#                 "political",
#                 "sublocality",
#                 "sublocality_level_1"
#             ]
#         },
#         {
#             "long_name": "Khorezm",
#             "short_name": "Khorezm",
#             "types": [
#                 "locality",
#                 "political"
#             ]
#         },
#         {
#             "long_name": "Khorezm Region",
#             "short_name": "Khorezm Region",
#             "types": [
#                 "administrative_area_level_1",
#                 "political"
#             ]
#         },
#         {
#             "long_name": "Uzbekistan",
#             "short_name": "UZ",
#             "types": [
#                 "country",
#                 "political"
#             ]
#         }
#     ],
#     "formatted_address": "Tinchlik Street, Khorezm, Urgench",
#     "geometry": {
#         "bounds": {
#             "northeast": {
#                 "lat": 41.3954567,
#                 "lng": 69.269883
#             },
#             "southwest": {
#                 "lat": 41.3249733,
#                 "lng": 69.16497629999999
#             }
#         },
#         "location": {
#             "lat": 41.55860870120288,
#             "lng": 60.6218083747805
#         },
#         "location_type": "APPROXIMATE",
#         "viewport": {
#             "northeast": {
#                 "lat": 41.3954567,
#                 "lng": 69.269883
#             },
#             "southwest": {
#                 "lat": 41.3249733,
#                 "lng": 69.16497629999999
#             }
#         }
#     },
#     "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
#     "types": [
#         "political",
#         "sublocality",
#         "sublocality_level_1"
#     ]
# }
# kenglik = data['geometry']['location']['lat']
# uzunlik = data['geometry']['location']['lng']
# print(f"{kenglik},{uzunlik}")



# yosh = input("Yoshinigizni kiriting:")
# try:
#     yosh = int(yosh)
#     print(f"Siz {2025-yosh} yilda tug'ilgansiz")
# except:
#     print("Butun son kiritmadimgiz")
#
# print("Dastur Tugadi!")



# yosh = input("Yoshinigizni kiriting:")
# try:
#     yosh = int(yosh)
# except:
#     print("Butun son kiritmadimgiz")
# else:
#     print(f"Siz {2025 - yosh} yilda tug'ilgansiz")
# print("Dastur Tugadi!")


# x,y = 5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bolib bo'lmaydi")



# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yhatda {len(mevalar)} ta element bor xolos")


# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi!")
# else:
#     print(f"x={x}")

#
# import json
# files=['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         pass
#     else:
#         print(talaba['ism'])





















































