# module load
import pymssql as ms
import numpy as np

# database connect
conn = ms.connect(server='localhost', user='bit',
                  password='1234', database='bitdb')

# cursor create
cursor = conn.cursor()

# cursor query insert and execute
cursor.execute('SELECT * FROM iris2;')

row = cursor.fetchall()
print(row)
conn.close()

aaa = np.asarray(row)
print(aaa)
print(aaa.shape)
print(type(aaa))

np.save('test_aaa.npy', aaa)

'''
# one row get
row = cursor.fetchone()
# print(type(row))    # tuple

while row:
    # print("첫 컬럼=%s, 둘 컬럼=%s" %(row[0], row[1]))
    print(row)
    row = cursor.fetchone()

# connect close
conn.close()
'''
