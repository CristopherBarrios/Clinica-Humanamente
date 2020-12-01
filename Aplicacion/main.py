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
                self.manager.current = 'menu'
            else:
                self.errM.text = 'Usuario o contrasena incorrecta'


class SecondWindow(Screen):
    #Crear usuario
    errM = ObjectProperty(None)

    def userVer(self):
        self.errM.text = ''
        nombr = self.ids.nombre_field.text
        apell = self.ids.apellido_field.text
        usern = self.ids.user_field.text
        passw = self.ids.pass_field.text
        confp = self.ids.confirmp_field.text
        nombres = str(nombr + ' '+ apell)
        
        if usern != '' and passw != '':
            #Verificar que no exista usuario
            cur.execute("SELECT COUNT(*) FROM secretarias WHERE username = '" + usern + "'")
            opcion1 = cur.fetchall()
            s = str(opcion1)
            if s != '[(1,)]':

                if passw != confp:
                    self.errM.text = 'Error al confirmar contrasena'
                else:
                    cur.execute(
                        "SELECT MAX(id) + 1 FROM secretarias")
                    opcion3 = cur.fetchall()
                    secreid = int(opcion3[0][0])

                    cur.execute("INSERT INTO secretarias VALUES(%s, %s, %s, %s)",
                                (secreid, str(nombres), str(usern), str(passw)))
                    con.commit()

                    self.manager.transition.direction = "right"
                    self.manager.current = 'log'
            else:
                self.errM.text = 'Usuario ya existe'
        else:
            self.errM.text = 'Por favor llene todos los campos requeridos'

class MenuWindow(Screen):
    pass

class ThirdWindow(Screen):
    #Inventario
    def on_enter(self, *args):
        medis = self.ids.medis
        medis.clear_widgets()
        meds = []
        cur.execute("SELECT * FROM medicamentos ORDER BY nombre ASC")
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

        esint = True
        try:
            int(unidades)
        except ValueError:
            esint = False
            self.errM.text = 'Cantidad de unidades invalida'
            inp += 1
        
        if (esint):
            if int(unidades) < 0:
                self.errM.text = 'Cantidad de unidades invalida'
                inp += 1
        if price == '':
            inp += 1
        
        esint2 = True
        try:
            float(price)
        except ValueError:
            esint2 = False
            self.errM.text = 'Precio invalido'
            inp += 1

        if (esint2):
            if float(price) < 0:
                self.errM.text = 'Precio invalido'
                inp += 1
        if date == '':
            inp += 1
        else:
            validFormat = True
            try:
                day,month,year = date.split('/')
            except ValueError:
                validFormat = False
                self.errM.text = 'Fecha invalida'
                inp += 1

            if (validFormat):
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
                cur.execute("INSERT INTO medicamentos VALUES(%s, %s, %s, %s, %s, %s)",
                        (medid, str(nombr), int(unidades), float(price), str(date), str(code)))
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

        esint = True
        try:
            int(unidades)
        except ValueError:
            esint = False
            self.errM.text = 'Cantidad de unidades invalida'
            inp += 1
        
        if (esint):
            if int(unidades) < 0:
                self.errM.text = 'Cantidad de unidades invalida'
                inp += 1
        if price == '':
            inp += 1
        
        esint2 = True
        try:
            float(price)
        except ValueError:
            esint2 = False
            self.errM.text = 'Precio invalido'
            inp += 1

        if (esint2):
            if float(price) < 0:
                self.errM.text = 'Precio invalido'
                inp += 1
        if date == '':
            inp += 1
        else:
            validFormat = True
            try:
                day,month,year = date.split('/')
            except ValueError:
                validFormat = False
                self.errM.text = 'Fecha invalida'
                inp += 1

            if (validFormat):
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
                cur.execute("UPDATE medicamentos SET disponible = %s , precio = %s, vencimiento = %s, codigo = %s WHERE nombre = %s",
                        (int(unidades), float(price),  str(date), str(code), str(nombr)))
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

class SeventhWindow(Screen):
    #Agendar citas
    def on_enter(self, *args):
        cits = self.ids.cits
        cits.clear_widgets()
        citas = []
        cur.execute("SELECT * FROM citas ORDER BY fecha ASC")
        opcion1 = cur.fetchall()
        for i in opcion1:
            layout = GridLayout(cols=5, size_hint_y=None, height=40)
            year,month,day = str(i[1]).split('-')
            fecha = day + "/" + month + "/" + year
            layout.add_widget(Label(text=fecha, font_size=20, color=[0,0,0,1]))
            pacienteid = i[4]
            cur.execute("SELECT nombre FROM pacientes WHERE id = " + str(pacienteid))
            pacientec = cur.fetchall()
            nombrep = str(pacientec[0][0])

            doctorid = i[5]
            cur.execute("SELECT nombre FROM doctores WHERE id = " + str(doctorid))
            doctorc = cur.fetchall()
            nombred = str(doctorc[0][0])

            #Datos vacios
            if i[2] == None:
                hora = 'N/A'
            else:
                hora = i[2]
            if i[3] == None:
                descripcion = 'N/A'
            else:
                descripcion = str(i[3])

            layout.add_widget(Label(text=str(hora), font_size=20, color=[0,0,0,1]))
            layout.add_widget(Label(text=str(nombrep), font_size=20, color=[0,0,0,1]))
            layout.add_widget(Label(text=str(nombred), font_size=20, color=[0,0,0,1]))
            layout.add_widget(Label(text=descripcion, font_size=20, color=[0,0,0,1]))

            citas.append(layout)
        
        for i in citas:
            cits.add_widget(i)

class EigthWindow(Screen):
    #Agregar cita
    errM = ObjectProperty(None)

    def addCit(self):
        self.errM.text = ''
        date = self.ids.fecha_field.text
        time = self.ids.hora_field.text
        paciente = self.ids.paciente_field.text
        doctor = self.ids.doctor_field.text
        desc = self.ids.desc_field.text

        #Inputs vacios o invalidos
        inp = 0
        if paciente == '':
            inp += 1
        if doctor == '':
            inp += 1
        if desc == '':
            inp += 1

        if date == '':
            inp += 1
        else:
            validFormat = True
            try:
                day,month,year = date.split('/')
            except ValueError:
                validFormat = False
                self.errM.text = 'Fecha invalida'
                inp += 1

            if (validFormat):
                isValidDate = True
                try :
                    datetime.datetime(int(year),int(month),int(day))
                except ValueError :
                    isValidDate = False

                if isValidDate == False or int(year) < 2020:
                    self.errM.text = 'Fecha invalida'
                    inp += 1
        
        if time == '':
            inp += 1
        else:
            try:
                datetime.datetime.strptime(time, "%H:%M")
            except ValueError:
                self.errM.text = 'Hora invalida'
                inp += 1

        if inp == 0:
            cur.execute(
                "SELECT MAX(id) + 1 FROM citas")
            opcion3 = cur.fetchall()
            citaid = int(opcion3[0][0])

            #Verificar que exista doctor y agarrar id
            cur.execute("SELECT id FROM doctores WHERE nombre = '" + doctor + "'")
            opcion1 = cur.fetchall()
            if len(opcion1) > 0:
                doctorid = opcion1[0][0]

                #Verificar que exista paciente y agarrar id
                cur.execute("SELECT id FROM pacientes WHERE nombre = '" + paciente + "'")
                opcion1 = cur.fetchall()
                if len(opcion1) > 0:
                    pacienteid = opcion1[0][0]
                    #Verificar que no hay cita
                    day,month,year = date.split('/')
                    fecha = year + '-' + month + '-' + day
                    hour = int(time.split(':')[0])
                    mintime = str(hour - 1) + ':00'
                    maxtime = str(hour + 2) + ':00'
                    cur.execute("SELECT COUNT(*) FROM citas WHERE fecha = '" + fecha + "' and hora > '" + mintime + "' and hora < '" + maxtime + "' and (doctorid = " + str(doctorid) + " or pacienteid = " + str(pacienteid) + ")")
                    opcion1 = cur.fetchall()
                    s = str(opcion1)
                    if s == '[(0,)]':
                        
                        cur.execute("INSERT INTO citas VALUES(%s, %s, %s, %s, %s, %s)",
                                (citaid, str(fecha), str(time), str(desc), int(pacienteid), int(doctorid)))
                        con.commit()

                        self.manager.transition.direction = "right"
                        self.manager.current = 'citas'
                    else:
                        self.errM.text = 'El doctor no esta disponible o el paciente tiene otra cita durante ese tiempo'
                else:
                    self.errM.text = 'Paciente incorrecto o no esta registrado'
            else:
                self.errM.text = 'Doctor incorrecto o no esta registrado'
        elif self.errM.text == '':
            self.errM.text = 'Por favor llene todos los campos requeridos'

class NinthWindow(Screen):
    #Editar cita
    errM = ObjectProperty(None)

    def editCit(self):
        date = self.ids.date_field.text
        time = self.ids.hora_field.text
        nombr = self.ids.patient_field.text
        
        inp = 0
        
        if nombr == '':
            inp += 1
        
        if date == '':
            inp += 1
        else:
            validFormat = True
            try:
                day,month,year = date.split('/')
            except ValueError:
                validFormat = False
                self.errM.text = 'Fecha invalida'
                inp += 1

            if (validFormat):
                isValidDate = True
                try :
                    datetime.datetime(int(year),int(month),int(day))
                except ValueError :
                    isValidDate = False

                if isValidDate == False or int(year) < 2020:
                    self.errM.text = 'Fecha invalida'
                    inp += 1

        if time == '':
            inp += 1
        else:
            try:
                datetime.datetime.strptime(time, "%H:%M")
            except ValueError:
                self.errM.text = 'Hora invalida'
                inp += 1

        if inp == 0:
            cur.execute("SELECT id FROM pacientes WHERE nombre = '" + str(nombr) + "'")
            opcion1 = cur.fetchall()
            if len(opcion1) == 0:
                self.errM.text = 'No se encontro el paciente indicado'
            else:
                pacienteid = opcion1[0][0]
                #Verificar existe cita
                day,month,year = date.split('/')
                fecha = year + '-' + month + '-' + day
                cur.execute("SELECT id FROM citas WHERE fecha = '" + fecha + "' and hora = '" + time + "' and pacienteid = " + str(pacienteid))
                opcion1 = cur.fetchall()
                if len(opcion1) > 0:
                    citaid = opcion1[0][0]
                    TenthWindow.citae = citaid

                    self.errM.text = ''
                    self.manager.transition.direction = "left"
                    self.manager.current = 'editci'
                else:
                    self.errM.text = 'No se encontro la cita'
        elif self.errM.text == '':
            self.errM.text = 'Por favor llene todos los campos requeridos'

class TenthWindow(Screen):
    #Editar cita
    errM = ObjectProperty(None)
    citae = ''

    def editCit(self):
        self.errM.text = ''
        date = self.ids.fecha_field.text
        time = self.ids.hora_field.text
        paciente = self.ids.paciente_field.text
        doctor = self.ids.doctor_field.text
        desc = self.ids.desc_field.text

        #Inputs vacios o invalidos
        inp = 0
        if paciente == '':
            inp += 1
        if doctor == '':
            inp += 1
        if desc == '':
            inp += 1

        if date == '':
            inp += 1
        else:
            validFormat = True
            try:
                day,month,year = date.split('/')
            except ValueError:
                validFormat = False
                self.errM.text = 'Fecha invalida'
                inp += 1

            if (validFormat):
                isValidDate = True
                try :
                    datetime.datetime(int(year),int(month),int(day))
                except ValueError :
                    isValidDate = False

                if isValidDate == False or int(year) < 2020:
                    self.errM.text = 'Fecha invalida'
                    inp += 1
        
        if time == '':
            inp += 1
        else:
            try:
                datetime.datetime.strptime(time, "%H:%M")
            except ValueError:
                self.errM.text = 'Hora invalida'
                inp += 1

        if inp == 0:
            #Verificar que exista doctor y agarrar id
            cur.execute("SELECT id FROM doctores WHERE nombre = '" + doctor + "'")
            opcion1 = cur.fetchall()
            if len(opcion1) > 0:
                doctorid = opcion1[0][0]

                #Verificar que exista paciente y agarrar id
                cur.execute("SELECT id FROM pacientes WHERE nombre = '" + paciente + "'")
                opcion1 = cur.fetchall()
                if len(opcion1) > 0:
                    pacienteid = opcion1[0][0]
                    #Verificar que no hay cita
                    day,month,year = date.split('/')
                    fecha = year + '-' + month + '-' + day
                    hour = int(time.split(':')[0])
                    mintime = str(hour - 1) + ':00'
                    maxtime = str(hour + 2) + ':00'
                    cur.execute("SELECT COUNT(*) FROM citas WHERE fecha = '" + fecha + "' and hora > '" + mintime + "' and hora < '" + maxtime + "' and (doctorid = " + str(doctorid) + " or pacienteid = " + str(pacienteid) + ") and id != " + str(self.citae))
                    opcion1 = cur.fetchall()
                    s = str(opcion1)
                    if s == '[(0,)]':
                        
                        cur.execute("UPDATE citas SET fecha = %s, hora = %s, descripcion = %s, pacienteid = %s, doctorid = %s WHERE id = %s",
                                (str(fecha), str(time), str(desc), int(pacienteid), int(doctorid), int(self.citae)))
                        con.commit()

                        self.manager.transition.direction = "right"
                        self.manager.current = 'citas'
                    else:
                        self.errM.text = 'El doctor no esta disponible o el paciente tiene otra cita durante ese tiempo'
                else:
                    self.errM.text = 'Paciente incorrecto o no esta registrado'
            else:
                self.errM.text = 'Doctor incorrecto o no esta registrado'
        elif self.errM.text == '':
            self.errM.text = 'Por favor llene todos los campos requeridos'

class EleventhWindow(Screen):
    #Eliminar cita
    errM = ObjectProperty(None)

    def deleteCit(self):
        nombr = self.ids.name_field.text
        date = self.ids.date_field.text
        time = self.ids.hora_field.text
        
        inp = 0
        
        if nombr == '':
            inp += 1
        
        if date == '':
            inp += 1
        else:
            validFormat = True
            try:
                day,month,year = date.split('/')
            except ValueError:
                validFormat = False
                self.errM.text = 'Fecha invalida'
                inp += 1

            if (validFormat):
                isValidDate = True
                try :
                    datetime.datetime(int(year),int(month),int(day))
                except ValueError :
                    isValidDate = False

                if isValidDate == False or int(year) < 2020:
                    self.errM.text = 'Fecha invalida'
                    inp += 1

        if time == '':
            inp += 1
        else:
            try:
                datetime.datetime.strptime(time, "%H:%M")
            except ValueError:
                self.errM.text = 'Hora invalida'
                inp += 1

        if inp == 0:
            cur.execute("SELECT id FROM pacientes WHERE nombre = '" + str(nombr) + "'")
            opcion1 = cur.fetchall()
            if len(opcion1) == 0:
                self.errM.text = 'No se encontro el paciente indicado'
            else:
                pacienteid = opcion1[0][0]
                #Verificar que hay cita
                day,month,year = date.split('/')
                fecha = year + '-' + month + '-' + day
                cur.execute("SELECT COUNT(*) FROM citas WHERE fecha = '" + fecha + "' and hora = '" + time + "' and pacienteid = " + str(pacienteid))
                opcion1 = cur.fetchall()
                s = str(opcion1)
                if s != '[(0,)]':
                    cur.execute("DELETE FROM citas WHERE pacienteid = %s and fecha = %s and hora = %s", (str(pacienteid), fecha, time))
                    con.commit()

                    self.errM.text = ''
                    self.manager.transition.direction = "right"
                    self.manager.current = 'citas'
                else:
                    self.errM.text = 'No se encontro la cita'
        elif self.errM.text == '':
            self.errM.text = 'Por favor llene todos los campos requeridos'


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()

