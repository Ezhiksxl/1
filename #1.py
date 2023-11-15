#this is new project for github version 1.3
import csv
import psycopg2
conn = psycopg2.connect( host = 'localhost' , dbname = '123' , user = 'postgres' , password = '123' , port = '5432')
# print('connected')

cur = conn.cursor()
cur.execute('select * from manager;')
results = cur.fetchall()
for i in results:
    print(i)


conn.commit()
cur.close()
conn.close()


zadaniye = "results1.csv"

# Запись данных в CSV файл
with open(zadaniye, mode='w', newline='') as файл_csv:
    reader_csv = csv.writer(файл_csv)
    reader_csv.writerows(results)

print(f"Данные успешно записаны в файл {zadaniye}")









# Found = False
# while not Found:
#     username = input('введите логин:')
#     if username in usernames:
#         print('вы есть в списке')
#         Found = True
#     else:
#         print('К сожалению мы не нашли вас в списке')
# username = input('введите логин:')

# username = input('')
# arr = usernames
# def binary_search(arr, x):
#     global coefizhent
#     coefizhent = x
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (high + low) // 2

#         if arr[mid] < x:
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             print(arr)
#             return mid

#     print("tuta")
#     return -1

# result = binary_search(arr, username)
# if result != -1:
#     print(f"Имя пользователя {username} найдено в списке." , coefizhent)
# else:
#     print(f"Имя пользователя {username} не найдено в списке.")
    



