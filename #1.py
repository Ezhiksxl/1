#this is new project for github version 1.3
import psycopg2
conn = psycopg2.connect( host = 'localhost' , dbname = 'sultan' , user = 'postgres' , password = '123456' , port = '5432')
print('connected')

cur = conn.cursor()
cur.execute('select name from manager limit 3;')
usernames = [r[0] for r in cur.fetchall()]
Found = False
while not Found:
    username = input('введите логин:')
    if username in usernames:
        print('вы есть в списке')
        Found = True
    else:
        print('К сожалению мы не нашли вас в списке')

conn.commit()
cur.close()
conn.close()
