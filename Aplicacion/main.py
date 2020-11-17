#Aplicacion Clinica Humanamente
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
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
    #cambiar password
    password = "Diego199")

#create a cursor
cur = con.cursor()

class MainWindow(Screen):
    #Log in
    errM = ObjectProperty(None)

    def userVer(self):
        usern = self.ids.user_field.text
        passw = self.ids.pass_field.text

        if usern != '':
            cur.execute("SELECT COUNT(*) FROM secretarias WHERE username = %s AND password = %s", (str(usern), str(passw)))
            opcion1 = cur.fetchall()
            s = str(opcion1)
            if s != '[(0,)]':
                self.errM.text = ''
                self.manager.transition.direction = "left"
                self.manager.current = 'inventario'
            else:
                self.errM.text = 'Usuario o contrasena incorrecta'


class SecondWindow(Screen):
    #Crear usuario
    errM = ObjectProperty(None)

    def userVer(self):
        nombr = self.ids.nombre_field.text
        apell = self.ids.apellido_field.text
        usern = self.ids.user_field.text
        passw = self.ids.pass_field.text
        confp = self.ids.confirmp_field.text
        nombres = str(nombr + ' '+ apell)
        
        if usern != '' and passw != '':
            if passw != confp:
                self.errM.text = 'Error al confirmar contrasena'
            else:
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
    #Inventario
    def on_enter(self, *args):
        medis = self.ids.medis
        medis.clear_widgets()
        meds = []
        cur.execute("SELECT * FROM medicamentos")
        opcion1 = cur.fetchall()
        for i in opcion1:
            layout = GridLayout(cols=5, size_hint_y=None, height=40)
            layout.add_widget(Label(text=str(i[1]), font_size=22, color=[0,0,0,1]))
            #Datos vacios
            if i[2] == None:
                fecha = 'N/A'
            else:
                fecha = i[2]
            if i[3] == None:
                precio = 'N/A'
            else:
                precio = 'Q: ' + str(i[3])
            if i[4] == None:
                venci = 'N/A'
            else:
                venci = i[4]
            if i[5] == None:
                codi = 'N/A'
            else:
                codi = i[5]
            layout.add_widget(Label(text=str(codi), font_size=22, color=[0,0,0,1]))
            layout.add_widget(Label(text=str(venci), font_size=22, color=[0,0,0,1]))
            layout.add_widget(Label(text=str(fecha), font_size=22, color=[0,0,0,1]))
            layout.add_widget(Label(text=precio, font_size=22, color=[0,0,0,1]))

            meds.append(layout)
        
        for i in meds:
            medis.add_widget(i)

class FourthWindow(Screen):
    #Agregar medicamento
    errM = ObjectProperty(None)

    def addMed(self):
        self.errM.text = ''
        nombr = self.ids.name_field.text
        code = self.ids.code_field.text
        date = self.ids.date_field.text
        price = self.ids.price_field.text
        unidades = self.ids.unidades_field.text

        #Inputs vacios o invalidos
        inp = 0
        if nombr == '':
            inp += 1
        if code == '':
            inp += 1
        if unidades == '':
            unidades = 0
        elif int(unidades) < 0:
            self.errM.text = 'Cantidad de unidades invalida'
            inp += 1
        if price == '':
            inp += 1
        elif float(price) < 0:
            self.errM.text = 'Precio invalido'
            inp += 1
        if date == '':
            inp += 1
        else:
            day,month,year = date.split('/')

            isValidDate = True
            try :
                datetime.datetime(int(year),int(month),int(day))
            except ValueError :
                isValidDate = False

            if isValidDate == False or int(year) < 2020:
                self.errM.text = 'Fecha invalida'
                inp += 1

        if inp == 0:
            cur.execute(
                "SELECT MAX(id) + 1 FROM medicamentos")
            opcion3 = cur.fetchall()
            medid = int(opcion3[0][0])

            #Verificar que no este registrado
            cur.execute("SELECT COUNT(*) FROM medicamentos WHERE nombre = '" + nombr + "'")
            opcion1 = cur.fetchall()
            s = str(opcion1)
            if s != '[(1,)]':
                cur.execute("INSERT INTO medicamentos VALUES(%s, %s, %s, %s, %s)",
                        (medid, str(nombr), int(unidades), float(price), str(date)))
                con.commit()

                self.manager.transition.direction = "right"
                self.manager.current = 'inventario'
            else:
                self.errM.text = 'El medicamento ya esta registrado'
        elif self.errM.text == '':
            self.errM.text = 'Por favor llene todos los campos requeridos'

class FifthWindow(Screen):
    #Editar medicamento
    errM = ObjectProperty(None)

    def editMed(self):
        self.errM.text = ''
        nombr = self.ids.name_field.text
        code = self.ids.code_field.text
        date = self.ids.date_field.text
        price = self.ids.price_field.text
        unidades = self.ids.unidades_field.text

        #Inputs vacios o invalidos
        inp = 0
        if nombr == '':
            inp += 1
        if code == '':
            inp += 1
        if unidades == '':
            unidades = 0
        elif int(unidades) < 0:
            self.errM.text = 'Cantidad de unidades invalida'
            inp += 1
        if price == '':
            inp += 1
        elif float(price) < 0:
            self.errM.text = 'Precio invalido'
            inp += 1
        if date == '':
            inp += 1
        else:
            day,month,year = date.split('/')

            isValidDate = True
            try :
                datetime.datetime(int(year),int(month),int(day))
            except ValueError :
                isValidDate = False

            if isValidDate == False or int(year) < 2020:
                self.errM.text = 'Fecha invalida'
                inp += 1

        if inp == 0:
            cur.execute("SELECT * FROM medicamentos WHERE nombre = '" + str(nombr) + "'")
            opcion1 = cur.fetchall()
            if len(opcion1) == 0:
                self.errM.text = 'No se encontro el medicamento'
            else:
                cur.execute("UPDATE medicamentos SET disponible = %s , precio = %s, vencimiento = %s WHERE nombre = %s",
                        (int(unidades), float(price),  str(date), str(nombr)))
                con.commit()

                self.manager.transition.direction = "right"
                self.manager.current = 'inventario'
        elif self.errM.text == '':
            self.errM.text = 'Por favor llene todos los campos requeridos'


class SixthWindow(Screen):
    #Eliminar medicamento
    errM = ObjectProperty(None)

    def deleteMed(self):
        nombr = self.ids.name_field.text
        if nombr != '':
            cur.execute("SELECT * FROM medicamentos WHERE nombre = '" + str(nombr) + "'")
            opcion1 = cur.fetchall()
            if len(opcion1) == 0:
                self.errM.text = 'No se encontro el medicamento'
            else:
                cur.execute("DELETE FROM medicamentos WHERE nombre= %s", (nombr,))
                con.commit()

                self.errM.text = ''
                self.manager.transition.direction = "right"
                self.manager.current = 'inventario'
        else:
            self.errM.text = 'Por favor llene todos los campos requeridos'



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()

