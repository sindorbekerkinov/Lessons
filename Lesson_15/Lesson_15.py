# with open('pi.txt')as fayl:
#     pi = fayl.read()
# # print(pi)
# # print(type(pi))
# #
# # fayl = open('pi.txt')
# # PI = fayl.read()
# # print(PI)
# # fayl.close()
#
# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = float(pi)
# print(pi)
# print(type(pi))
#


# filename = 'talabalar'
# with open(filename) as file:
#     for line in file:
#         print(f'Talaba: {line}')


# with open('talabalar') as file:
#     talabalar = file.readlines()
#
# print(talabalar)
# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# faylnomi = ' ustozlar.txt'
# with open(faylnomi,'w') as fayl:
#     fayl.write('jonibek uraalov')
#
# faylnomi = 'new_file.txt'
# ism = "Sindorbek Erkinov "
# tyil = '2006'
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism+"\n")
#     fayl.write(tyil+"\n")

#
# import pickle
#
# talaba1 = {'ism':'hasan','familya':'uralov','tyil':2004,'kurs':2}
# talaba2 = {'ism':'alijon', 'familya':'valiyev',"tyil":2002, "kurs":2}
#
# with open('info.dat','wb') as file:
#     pickle.dump(talaba1.file)
#     pickle.dump(talaba2,file)
# with open('info','rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)
#
# print(talaba1)
# print(talaba2)





