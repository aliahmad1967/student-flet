from flet import *
import sqlite3


conn = sqlite3.connect('dato.db',check_same_thread=False)# الغاء الارسال التعدد
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS student(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stdname TEXT NOT NULL,
            stdemail TEXT NOT NULL,
            stdphone TEXT NOT NULL,
            stdaddress TEXT NOT NULL,
            stmathmatic INTEGER,
            starabic INTEGER,
            stfrance INTEGER,
            stenglish INTEGER,
            stdrowing INTEGER,
            stchemistry INTEGER               
)""")

conn.commit()


def main(page:Page):
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    page.window.title = 'Flet Demo'
    page.window.bgcolor = '#ffffff'
    page.theme_mode = ThemeMode.LIGHT


   #####################################################

    table_name = 'student'
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]

    def add(e):
        cursor.execute("INSERT INTO student(stdname,stdemail,stdphone,stdaddress,stmathmatic,starabic,stfrance,stenglish,stdrowing,stchemistry)VALUES (?,?,?,?,?,?,?,?,?,?)",(tname.value,temail.value,tphone.value,taddresss.value,mathmatic.value,arabic.value,france.value,english.value,drawing.value,chemistry.value))  
        conn.commit()


    def show(e):
        page.clean()
        c = conn.cursor()
        c.execute("SELECT * FROM student")
        users = c.fetchall()
        print(users)
        if not users=="":
            keys = ['id', 'stdname', 'stdemail', 'stdphone', 'stdaddress', 'stmathmatic', 'starabic', 'stfrance', 'stenglish', 'stdrowing', 'stchemistry']
            result = [dict(zip(keys,values)) for values in users]
            for x in result:
                ########## Marks #######################
                m= x['stmathmatic']
                a= x['starabic']
                f= x['stfrance']
                e= x['stenglish']
                d= x['stdrowing']
                c= x['stchemistry']
                res = m+a+f+e+d+c
                if res < 299:
                    status = Text('😒 راسب', size=19,color='white')
                else:
                    status = Text('😊 ناجح', size=19,color='white')






                page.add(
                    Card(
                        color='#C63C51',
                        content=Container(
                            content=Column([
                                ListTile(
                                    leading=Icon(icons.PERSON),
                                    title=Text('Name : '+ x['stdname'],color='white'),
                                    subtitle=Text('Student Email : '+ x['stdemail'],color='amber'),
                                    # on_click=...
                                ),
                                Row([
                                    Text('Phone : '+ x['stdphone'],color='#CCE0AC'),
                                    Text('Address : '+ x['stdaddress'],color='#F0EAAC')
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text('رياضيات : '+ str(x['stmathmatic']),color='#5AB2FF'),
                                    Text('عربي : ' + str(x['starabic']),color='#5AB2FF'),
                                    Text('فرنسي : ' + str(x['stfrance']),color='#5AB2FF'),

                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text('انكليزي : '+ str(x['stenglish']),color='#5AB2FF'),
                                    Text('رسم : '+ str(x['stdrowing']),color='#5AB2FF'),
                                    Text('كيمياء : '+ str(x['stchemistry']),color='#5AB2FF'),
                                ],alignment=MainAxisAlignment.CENTER),

                                Row([
                                    status
                                ],alignment=MainAxisAlignment.CENTER)


                            ])
                        )
                    )
                )
                page.update()                
      



    









    #################### Feilds #######################
    tname = TextField(label='اسم الطالب',icon=icons.PERSON,rtl=True,height=38)
    temail = TextField(label='البريد الألكتروني',icon=icons.EMAIL,rtl=True,height=38)
    tphone= TextField(label='رقم الهاتف',icon=icons.PHONE,rtl=True,height=38)
    taddresss= TextField(label='عنوان السكن',icon=icons.LOCATION_ON,rtl=True,height=38)

    ##################################################


    #################### Marks #######################
    
    markText = Text('علامات الطالب',text_align= 'center',weight='BOLD')
    mathmatic = TextField(label='الرياضيات',text_align= 'center',width=110,rtl=True,height=38)
    arabic = TextField(label='عربي',text_align= 'center',width=110,rtl=True,height=38)
    france = TextField(label='الفرنسي',text_align= 'center',width=110,rtl=True,height=38)
    english = TextField(label='الإنكليزي',text_align= 'center',width=110,rtl=True,height=38)
    drawing = TextField(label='الرسم',text_align= 'center',width=110,rtl=True,height=38)
    chemistry = TextField(label='الكيمياء',text_align= 'center',width=110,rtl=True,height=38)
    ###################################################

    addbuttton = ElevatedButton(
        'إضافة طالب جديد',
         width=170,
         style=ButtonStyle(bgcolor='blue',color='white',padding=15,),
         on_click=add
         )
    
    showbutton = ElevatedButton(
        'عرض الطلاب',
         width=170,
         style=ButtonStyle(bgcolor='blue',color='white',padding=15,),
         on_click=show
         )

     

    page.add(
        Row([
            Image(src='home.gif',width=200,height=200,fit=ImageFit.CONTAIN),
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text('تطبيق الطالب و المعلم في جيبك',size=20,font_family='Cairo')
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text('عدد الطلاب المسجلين :',size=18,font_family='Cairo',color='blue'),
            Text(row_count,size=20,font_family='Cairo'),
        ],alignment=MainAxisAlignment.CENTER,rtl=True),

        tname, temail, tphone, taddresss,
        Row([
            markText
            ],alignment=MainAxisAlignment.CENTER,rtl=True),

        Row([
            mathmatic, arabic, france
            ],alignment=MainAxisAlignment.CENTER,rtl=True),
        Row([
            english, drawing, chemistry
            ],alignment=MainAxisAlignment.CENTER,rtl=True),

        Row([
            addbuttton, showbutton
            ],alignment=MainAxisAlignment.CENTER,rtl=True),
    )









    page.update()
app(main)