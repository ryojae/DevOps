# # 모듈 import
# import pymysql

# # MySQL 데이터베이스 연결
# db = pymysql.connect(host='127.0.0.1', user='tester2', password='0000',
# port=3306 ,db='TEST', charset='utf8')

# # 데이터에 접근
# cursor = db.cursor()

# # SQL query 작성
# sql = "select * from test"

# # SQL query 실행
# cursor.execute(sql)

# # db 데이터 가져오기
# res = cursor.fetchall() #모든 행 가져오기
# #cursor.fetchone() # 하나의 행만 가져오기
# #cursor.fetchmany(id) # n개의 데이터 가져오기
# for x in res:
#     print(x)

# # 수정 사항 db에 저장
# db.commit()

# # Database 닫기
# db.close()

# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="tester2",
# passwd="0000",
# database="TEST"
)
mc = mydb.cursor()
#mc.execute("ALTER TABLE test AUTO_INCREMENT=1")
mc.execute("SELECT * FROM test")
mr = mc.fetchall()
for x in mr:
    print(x)

# #page 18
# import pymysql

# #전역변수 선언
# conn, cur = None, None
# data1, data2, data3, data4 = "","","",""
# sql = ""

# #메인 코드
# conn = pymysql.connect(host='127.0.0.1',user='tester2',password ='0000', db='TEST', charset='utf8')
# cur = conn.cursor()

# cur.execute('CREATE TABLE IF NOT EXISTS userTable (id char(4), userName char(15), email char(20), birthYear int)')

# while 1:
#     data1 = input('사용자 ID ==>')
#     if data1 == "":
#         break
#     data2 = input('사용자 이름 ==>')
#     data3 = input('사용자 이메일 ==>')
#     data4 = input('사용자 출생년도 ==>')
    
#     sql = "INSERT INTO userTable VALUES ('"+data1+"','" +data2+"','"+data3+"','"+data4+"')"
#     cur.execute(sql)

# conn.commit()
# conn.close()

# #page 22
# import pymysql

# #전역변수 선언
# conn, cur = None, None
# data1, data2, data3, data4 = "","","",""
# row = None

# #메인 코드
# conn = pymysql.connect(host='127.0.0.1',user='tester2',password ='0000', db='TEST', charset='utf8')
# cur = conn.cursor()

# cur.execute('SELECT * FROM userTable')

# print('사용자ID     사용자이름      이메일      출생년도')
# print('-----------------------------------------------------')

# while 1:
#     row = cur.fetchone()
#     if row == None:
#         break
#     data1 = row[0]
#     data2 = row[1]
#     data3 = row[2]
#     data4 = row[3]
#     print('%5s      %15s        %20s        %d' %(data1, data2, data3, data4))

# conn.close()

# #page 25
# import pymysql
# from tkinter import *
# from tkinter import messagebox

# #함수 선언부
# def insertData():
#     con, cur = None, None
#     data1, data2, data3, data4 = '','','',''
#     sql = ''

#     conn = pymysql.connect(host='127.0.0.1',user='tester2',password ='0000', db='TEST', charset='utf8')
#     cur = conn.cursor()

#     data1 = edt1.get(); data2 =edt2.get(); data3 = edt3.get(); data4 = edt4.get()
#     try:
#         sql = "INSERT INTO userTable VALUES('"+data1+"','"+data2+"','"+data3+"','"+data4+"')"
#         cur.execute(sql)
#     except:
#         messagebox.showerror('오류','데이터 입력 오류가 발생함')
#     else:
#         messagebox.showinfo('성공', '데이터 입력 성공')
#     conn.commit()
#     conn.close()

# def selectData():
#     strData1, strData2, strData3, strData4 = [], [], [], []
#     conn = pymysql.connect(host='127.0.0.1',user='tester2',password ='0000', db='TEST', charset='utf8')
#     cur = conn.cursor()
#     cur.execute('SELECT *FROM userTable')
#     strData1.append('사용자 ID'); strData2.append('사용자이름'); strData3.append('이메일'); strData4.append('출생년도')
#     strData1.append('------------'); strData2.append('------------'); strData3.append('------------'); strData4.append('------------')

#     while 1:
#         row = cur.fetchone()
#         if row == None:
#             break
#         strData1.append(row[0]); strData2.append(row[1]); strData3.append(row[2]); strData4.append(row[3])
#     listData1.delete(0,listData1.size()-1); listData2.delete(0,listData2.size()-1)
#     listData3.delete(0,listData3.size()-1); listData4.delete(0,listData4.size()-1)

#     for item1, item2, item3, item4 in zip(strData1,strData2,strData3,strData4):
#         listData1.insert(END, item1); listData2.insert(END, item2)
#         listData3.insert(END, item3); listData4.insert(END, item4)
#     conn.close()

# #메인 코드
# window =Tk()
# window.geometry('600x300')
# window.title('GUI 데이터 입력')

# edtFrame = Frame(window)
# edtFrame.pack()
# listFrame = Frame(window)
# listFrame.pack(side = BOTTOM,fill = BOTH, expand=1)

# edt1= Entry(edtFrame, width=10); edt1.pack(side=LEFT,padx=10,pady=10)
# edt2= Entry(edtFrame, width=10); edt2.pack(side=LEFT,padx=10,pady=10)
# edt3= Entry(edtFrame, width=10); edt3.pack(side=LEFT,padx=10,pady=10)
# edt4= Entry(edtFrame, width=10); edt4.pack(side=LEFT,padx=10,pady=10)

# btnInsert = Button(edtFrame, text='입력', command=insertData)
# btnInsert.pack(side=LEFT,padx=10,pady=10)
# btnSelect = Button(edtFrame, text='조회', command=selectData)
# btnSelect.pack(side=LEFT,padx=10,pady=10)

# listData1 = Listbox(listFrame,bg = 'white'); listData1.pack(side=LEFT,fill=BOTH, expand=1)
# listData2 = Listbox(listFrame,bg = 'white'); listData2.pack(side=LEFT,fill=BOTH, expand=1)
# listData3 = Listbox(listFrame,bg = 'white'); listData3.pack(side=LEFT,fill=BOTH, expand=1)
# listData4 = Listbox(listFrame,bg = 'white'); listData4.pack(side=LEFT,fill=BOTH, expand=1)

# window.mainloop()


import pymysql

#전역변수 선언
conn, cur = None, None
data1, data2, data3, data4 = "","","",""
sql = ""

#메인 코드
conn = pymysql.connect(host='127.0.0.1',user='tester2',password ='0000', db='TEST', charset='utf8')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS userTable (id char(4), userName char(15), email char(20), birthYear int)')

while 1:
    data1 = input('사용자 ID ==>')
    if data1 == "":
        break
    
    sql = "DELETE FROM userTable WHERE id = "+data1
    cur.execute(sql)

conn.commit()
conn.close()