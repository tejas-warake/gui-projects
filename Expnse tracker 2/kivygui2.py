import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import xlsxwriter
from kivy.uix.popup import Popup
import numpy as np
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import os
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

global N,T,A,Aplt,Ncpt,Nd,Ad,Td,Date,Flag,rnum
N=[]
rnum=[]
Flag=0
Date=[]
Nd=[]
T=[]
Td=[]
A=[]
Ad = []
Aplt=[]

class FirstWindow(Screen):
    
    
    #initialize infinite keywords
    '''name = ObjectProperty(None)
    title = ObjectProperty(None)
    amt = ObjectProperty(None)'''
    
    def press(self):
        nme= self.nme.text
        title = self.title.text
        Amount = self.amt.text
        date= self.dat.text
        
        if nme!="" or title!="" or Amount!="":
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            conn.execute("CREATE TABLE IF NOT EXISTS main1 (Srno INTEGER,Date Text,Name Text,Title Text,Amount Text)")
            cursor.execute('SELECT * ''FROM main1')
            data1=cursor.fetchall()
            conn.commit()
                    
            srno = 1
            srno= len(data1)+1
            conn.execute("INSERT INTO main1 VALUES (?,?, ?, ?, ?);", (srno,date, nme, title,Amount))
            conn.commit()
            rnum.append(srno)
            conn.close
            srno= len(data1)
            
        

            print(nme,Amount,title)
            #self.dspl= Label(text= f'{name},{title},{Amount}')
            #self.add_widget(self.dspl)
            #for j in range (i):
            
            N.append(nme)
            Nd.append(nme)
            T.append(title)
            Td.append(title)
            A.append(Amount)
            Ad.append(Amount)
            Date.append(date)
            
            Ncpt = [x.upper() for x in N]
            if len(N)>1:
            
                for t in range (len(A)):
                    u = int(A[t])
                    Aplt.append(u)
                    #x = N[p].upper
                    #print(x)
                for m in range (len(N)):

                
                    for p in range (len(N)) :
                        if p+1 == len(N):
                            break
                        if p+1>m:
                            if Ncpt[m] == Ncpt[p+1]:
                                Aplt[m]= Aplt[m]+Aplt[(p+1)]
                                if len(A)>1:
                                    del A[(p+1)]
                                if len(A)>0:
                                    del A[0]
                                
                                del Aplt[(p+1)]
                                del N[(p+1)]
                                break
                            elif len(A)!= 0:
                                if len(A)==2:
                                    A.pop()
                                    A.pop()
                                else:
                                    A.pop()
           
                    

        else:
            invalid()



def invalid():
    pop3 =Popup(title='Invalid Input',
content=Label(text='Please Enter Valid data'),
                size_hint=(None,None)
,
                size=(400,400))
    
    pop3.open()
    def graph(self):
        data = Aplt
        
        
        labels = N

        
        print(Aplt)
        print(A)
        plt.xticks(range(len(data)), labels)
        plt.xlabel('Names')
        plt.ylabel('Amounts')
        plt.bar(range(len(data)), data) 
        plt.show()

        


class SecondWindow(Screen):
        
    def mail(self):
        if self.sendfile.text != "" and self.sendto.text != "":
            print(self.sendfile.text+".xlsx")
            sender_email = "xpensetrackerr@gmail.com"
            receiver_email = self.sendto.text
            message = MIMEMultipart()
            message["From"] = sender_email
            message['To'] = receiver_email
            message['Subject'] = "Here's your Data"
            file = self.sendfile.text+".xlsx"
            attachment = open(file,'rb')
            obj = MIMEBase('application','octet-stream')
            obj.set_payload((attachment).read())
            encoders.encode_base64(obj)
            obj.add_header('Content-Disposition',"attachment; filename= "+file)
            message.attach(obj)
            my_message = message.as_string()
            email_session = smtplib.SMTP('smtp.gmail.com',587)
            email_session.starttls()
            email_session.login(sender_email,'22010394')
            email_session.sendmail(sender_email,receiver_email,my_message)
            email_session.quit()
            print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")
            sent()



    
    def view(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * ''FROM main1')
        data2=cursor.fetchall()
        conn.commit()
        color1 = 'lightgreen'
        color2 = 'lightblue'
        
        fig = go.Figure(data=[go.Table(
            header=dict(values=["row number",'Name', 'Amount','Title']),
            cells=dict(values=[ [data2[x][0]  for x in range(len(data2)) ],
                                [data2[x][2] for x in range (len(data2))],
                                [data2[x][4] for x in range (len(data2))],
                                [data2[x][3] for x in range (len(data2))]],
                        fill_color=[[color1, color2, color1,
                                    color2, color1]*2],))
        ])
        fig.show()

    def deletee(self):
        if self.rownum.text != "":
            srno = int(self.rownum.text)
            print(srno)
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            conn.execute("""
               DELETE FROM main1
               WHERE Srno = ?
               """, (srno,))
            conn.commit()
            d1()
    def deleteall(self):

        conn = sqlite3.connect('test.db')
        conn.execute('DELETE FROM main1;',);
        conn.commit()
        d2()
    def press2(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * ''FROM main1')
        data=cursor.fetchall()
        conn.commit()
        i = 1
        j="A"
        k="B"
        l="C"
        v="D"
        x=str(i)
        a=self.filename.text

        outworkbook = xlsxwriter.Workbook(a+".xlsx")
        outsheet = outworkbook.add_worksheet()
        outsheet.write(j+"1" ,"Date")
        outsheet.write(k+"1" ,"Name")
        outsheet.write(l+"1" , "Title")
        outsheet.write(v+"1" , "Amount")
        for o in range (len(data)):
            #print(Nd[o],Td[o],Ad[o])
            #print(data[0][0])
            for r in range (1):
                x=str(o+2)
                print(x)
                outsheet.write(j+x ,data[o][r+1])
                outsheet.write(k+x ,data[o][r+2])
                outsheet.write(l+x ,data[o][r+3])
                outsheet.write(v+x ,data[o][r+4])
        outworkbook.close()
    def openxl(self):
        if self.filename1.text != "":
            b = os.getcwd()
            a= self.filename1.text+".xlsx"
            os.startfile(b+"\\"+a)
        
def d1():
    pop5 =Popup(title='',
content=Label(text='Given row deleted'),
                size_hint=(None,None)
,
                size=(400,400))
    Button
    pop5.open()
    
def d2():
    pop6 =Popup(title='',
content=Label(text='Previous History cleared'),
                size_hint=(None,None)
,
                size=(400,400))
    
    pop6.open()

 


    def graph(self):
        data = Aplt
        
        
        labels = N

        
        print(Aplt)
        print(A)
        plt.xticks(range(len(data)), labels)
        plt.xlabel('Names')
        plt.ylabel('Amounts')
        plt.bar(range(len(data)), data) 
        plt.show()
        

def sent():
    pop4 =Popup(title="",
content=Label(text='YOUR MAIL HAS BEEN SENT SUCCESSFULLY'),
                size_hint=(None,None)
,
                size=(400,400))
    Button
    pop4.open()        


class WindowManager(ScreenManager):
	pass



kv=Builder.load_file("elder.kv")
'''class MyGridlayout(Widget):
    pass'''
'''class MyGridlayout(Widget):'''

    #initialize infinite keywords
name = ObjectProperty(None)
date = ObjectProperty(None)
title = ObjectProperty(None)
amt = ObjectProperty(None)
filename = ObjectProperty(None)
#filename1 = ObjectProperty(None)
rownum = ObjectProperty(None)
sendto = ObjectProperty(None)
sendfile = ObjectProperty(None)    
        
   
        
class AwesomeApp(App):
    def build(self):
        return kv
if __name__=='__main__':
    AwesomeApp().run()

