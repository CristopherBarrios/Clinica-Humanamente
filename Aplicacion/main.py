
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import datetime
import psycopg2
import csv

Window.size = (1100, 700)
Window.clearcolor = (1, 1, 1, 1)

#connect to de database
con = psycopg2.connect(
    host = "localhost",
    database = "Humanamente",
    user = "postgres",
    password = "Diego199")

#create a cursor
cur = con.cursor()

class MainWindow(Screen):
    errM = ObjectProperty(None)


    def userVer(self):
        usern = self.ids.user_field.text
        passw = self.ids.pass_field.text
        #EleventhWindow.userActual = usern
        #TwelveWindow.userActual = usern

        self.manager.current = 'inventario'

        '''if usern != '':
            cur.execute("SELECT COUNT(*) FROM secretarias WHERE username = %s AND password = %s", (str(usern), str(passw)))
            opcion1 = cur.fetchall()
            s = str(opcion1)
            print(s)
            if s != '[(0,)]':
                self.errM.text = ''
                self.manager.transition.direction = "left"
                self.manager.current = 'home'
            else:
                self.errM.text = 'Usuario o contrasena incorrecta'''


class SecondWindow(Screen):
    errM = ObjectProperty(None)

    def userVer(self):
        nombr = self.ids.nombre_field.text
        apell = self.ids.apellido_field.text
        usern = self.ids.user_field.text
        passw = self.ids.pass_field.text
        confp = self.ids.confirmp_field.text
        nombres = str(nombr + ' '+ apell)
        
        if usern != '':
            cur.execute(
                "SELECT MAX(id) + 1 FROM secretarias")
            opcion3 = cur.fetchall()
            r = str(opcion3)
            r = r.replace('[', "")
            r = r.replace(']', "")
            r = r.replace('(', "")
            r = r.replace(')', "")
            r = r.replace("'", "")
            r = r.replace('"', "")
            r = r.replace(",", '')
            secreid = int(r)

            cur.execute("INSERT INTO secretarias VALUES(%s, %s, %s, %s)",
                        (secreid, str(nombres), str(usern), str(passw)))
            con.commit()

            self.manager.transition.direction = "right"
            self.manager.current = 'log'


class ThirdWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()

