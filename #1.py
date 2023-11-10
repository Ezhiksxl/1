#this is new project for github version 1.3
import psycopg2
conn = psycopg2.connect( host = 'localhost' , dbname = 'sultan' , user = 'postgres' , password = '123456' , port = '5432')
print('connected')

cur = conn.cursor()
cur.execute('select name from manager;')
usernames = [r[0] for r in cur.fetchall()]
# Found = False
# while not Found:
#     username = input('введите логин:')
#     if username in usernames:
#         print('вы есть в списке')
#         Found = True
#     else:
#         print('К сожалению мы не нашли вас в списке')
# username = input('введите логин:')

username = input('')
arr = usernames
def binary_search(arr, x):
    global coefizhent
    coefizhent = x
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            print(arr)
            return mid

    print("tuta")
    return -1

result = binary_search(arr, username)
if result != -1:
    print(f"Имя пользователя {username} найдено в списке." , coefizhent)
else:
    print(f"Имя пользователя {username} не найдено в списке.")
    



conn.commit()
cur.close()
conn.close()
