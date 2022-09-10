import io
import os
import mysql.connector as mysql
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import Screen as Sc
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import TwoLineIconListItem, ImageLeftWidget
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics.texture import Texture
from kivy.uix.bubble import Bubble
from kivy_garden.mapview import MapView, MapMarkerPopup
import kivy.core.text.markup
import geocoder
from matplotlib import pyplot as plt
import cv2
import random
import hashlib
import requests
from PIL import Image as pil
from requests_toolbelt import MultipartEncoder
import json

Window.size = (360, 640)

connection = mysql.connect(user="uif6hvcazhneszyn", password=some_secrete_password,
                           host='bmqwq6xgokafzfwckzqj-mysql.services.clever-cloud.com')
cursor = connection.cursor()
account_id = 0
mushroom_id = 0

class WindowManager(ScreenManager):
    pass


class MainWindow(Screen):
    btn1 = ObjectProperty(None)
    btn2 = ObjectProperty(None)
    btn3 = ObjectProperty(None)
    btn4 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        Clock.schedule_once(self.after_init)

    def after_init(self, dt):
        self.app = App.get_running_app()

    def press_btn1(self):
        sm.current = "camera_screen"
        sm.transition.direction = "left"
        return

    def press_btn2(self):
        sm.current = "save_location"
        sm.transition.direction = "left"
        return

    def press_btn3(self):
        sm.current = "quiz"
        sm.transition.direction = "left"
        return

    def press_btn4(self):
        sm.current = "encyclopedia"
        sm.transition.direction = "left"
        return


class Quiz(Screen):
    btn5 = ObjectProperty(None)
    btn6 = ObjectProperty(None)
    btn7 = ObjectProperty(None)
    btn9 = ObjectProperty(None)
    lab1 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Quiz, self).__init__(**kwargs)
        self.initialize_variables()

    def initialize_variables(self):
        self.questions = []
        self.loaded_questions = []
        self.counter = -1
        self.points = 0
        self.load_questions = True
        self.next_question = False

    def set_default_values(self):
        self.lab1.text = "Aby rozpoczac quiz - wcisnij przycisk next"
        self.btn5.text = ""
        self.btn6.text = ""
        self.btn7.text = ""
        self.btn5.background_color = "#D5BC90"
        self.btn6.background_color = "#D5BC90"
        self.btn7.background_color = "#D5BC90"

    def build(self):
        self.window = FloatLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        return self.window

    def quit_quiz(self):
        pop = Popup(title='Punktacja',
                    content=Label(text=f'Twój wynik to: {self.points} / {len(self.loaded_questions)}'),
                    size_hint=(None, None), size=(200, 200))
        pop.open()
        sm.current = "main"
        sm.transition.direction = "right"
        self.initialize_variables()
        self.set_default_values()
        return

    def change_question(self):
        if self.load_questions == True:
            with open('quiz.txt', 'r', encoding='utf-8') as f:
                line = f.readline()[:-1]
                while line != "":
                    temp = []
                    for n in range(5):
                        temp.append(line)
                        line = f.readline()[:-1]
                    self.questions.append(temp[:])

            id = random.sample(range(0, 40), 10)
            for n in id:
                self.loaded_questions.append(self.questions[n])
            self.load_questions = False

        if self.next_question == False:
            self.counter += 1
            self.next_question = True
        if self.counter >= len(self.loaded_questions):
            self.quit_quiz()
            return
        self.buttons = [self.btn5, self.btn6, self.btn7]
        self.lab1.text = self.loaded_questions[self.counter][0]
        self.btn5.text = self.loaded_questions[self.counter][1]
        self.btn6.text = self.loaded_questions[self.counter][2]
        self.btn7.text = self.loaded_questions[self.counter][3]

        self.btn5.background_color = "#D5BC90"
        self.btn6.background_color = "#D5BC90"
        self.btn7.background_color = "#D5BC90"

    def ans_1(self):
        if self.next_question == True:
            if int(self.loaded_questions[self.counter][4]) == 1:
                self.points += 1
                self.btn5.background_color = "#90ea93"
            else:
                self.btn5.background_color = "#f56f72"
                self.buttons[int(self.loaded_questions[self.counter][4]) - 1].background_color = "#90ea93"
            self.next_question = False
            # print(self.questions)

    def ans_2(self):
        if self.next_question == True:
            if int(self.loaded_questions[self.counter][4]) == 2:
                self.points += 1
                self.btn6.background_color = "#90ea93"
            else:
                self.btn6.background_color = "#f56f72"
                self.buttons[int(self.loaded_questions[self.counter][4]) - 1].background_color = "#90ea93"
            self.next_question = False

    def ans_3(self):
        if self.next_question == True:
            if int(self.loaded_questions[self.counter][4]) == 3:
                self.points += 1
                self.btn7.background_color = "#90ea93"
            else:
                self.btn7.background_color = "#f56f72"
                self.buttons[int(self.loaded_questions[self.counter][4]) - 1].background_color = "#90ea93"
            self.next_question = False


class Encyclopedia(Screen):
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Encyclopedia, self).__init__(**kwargs)
        self.buttons_added = False
        self.mushroom_names = []

    def add_buttons(self):
        if self.buttons_added:
            return
        scroll = ScrollView()
        list_view = MDList()
        cursor.execute('Select nazwa_Polska, nazwa_Lacinska from bmqwq6xgokafzfwckzqj.grzyby')
        data = []
        for n in cursor:
            data.append(n)
        for i in range(len(data)):
            icons = ImageLeftWidget(source=f"Images/{i + 1}.jpg")
            items = TwoLineIconListItem(text=data[i][0], secondary_text=data[i][1], on_release=self.set_mushroom_data)
            self.mushroom_names.append(data[i][0])
            items.add_widget(icons)
            list_view.add_widget(items)
        scroll.add_widget(list_view)
        self.container.add_widget(scroll)
        self.buttons_added = True

    def set_mushroom_data(self, item):
        global mushroom_id
        mushroom_id = int(self.mushroom_names.index(item.text)) + 1
        sm.current = "mushroom"
        sm.transition.direction = "left"
        return

    def go_back(self):
        sm.current = "main"
        sm.transition.direction = "right"
        return


class CameraScreen(Screen):
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)

    def go_back(self):
        sm.current = "main"
        sm.transition.direction = "right"
        self.container.remove_widget(self.image)
        self.capture.release()
        cv2.destroyAllWindows()
        return

    def go_to_gallery(self):
        sm.current = "file_manager"
        sm.transition.direction = "left"
        self.container.remove_widget(self.image)
        self.capture.release()
        cv2.destroyAllWindows()
        return

    def load_camera(self):
        self.image = Image()
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0 / 30.0)
        self.container.add_widget(self.image)

    def load_video(self, *args):
        try:
            ret, frame = self.capture.read()
            self.image_frame = frame
            buffer = cv2.flip(frame, 0).tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
            self.image.texture = texture
        except:
            return

    def take_photo(self):
        self.taken_photo = self.image_frame
        plt.imsave('grzyb.jpg', self.taken_photo)
        form = MultipartEncoder(
            fields={
                'box_threshold': '0.5',
                'number_threshold': '0.3',
                'file': ('grzyb.jpg', open('grzyb.jpg', 'rb'), 'image/jpg')
            }
        )
        #http://127.0.0.1:5000/images - for localhost
        #http://172.105.71.50:5000/images - for server
        self.response = requests.post('http://127.0.0.1:5000/images', data=form,
                                      headers={'Content-Type': form.content_type})
        response_dict = json.loads(self.response.text)
        if len(response_dict['grzyb']) != 0:
            global mushroom_id
            cursor.execute(
                f"Select id, nazwa_Polska from bmqwq6xgokafzfwckzqj.grzyby where nazwa_Lacinska = '{response_dict['grzyb']}'")
            mushroom_info = [n for n in cursor]
            mushroom_id = int(mushroom_info[0][0])
            mushroom_name = mushroom_info[0][1]
            confidence = round(float(response_dict['confidence']) * 100, 2)
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(
                text=f"Wykryto grzyba:\n{mushroom_name}\nPrawdopodobieństwo: {confidence}%\nCzy pokazać informacje na temat tego grzyba?",
                text_size=(200, None), halign="center", valign="center"))
            btn1 = Button(text="Tak, pokaż", size_hint_y=0.3)
            btn2 = Button(text="Nie, powróć", size_hint_y=0.3)
            box.add_widget(btn1)
            box.add_widget(btn2)

            self.popup_to_save = Popup(title='Wykryto grzyba', title_size=(16),
                                       title_align='center', content=box,
                                       size_hint=(None, None), size=(200, 200), size_hint_y=0.5,
                                       auto_dismiss=True)

            btn1.bind(on_press=self.go_to_mushroom_info)
            btn2.bind(on_press=self.popup_to_save.dismiss)
            self.popup_to_save.open()
        else:
            pop = Popup(title='Nie wykryto grzyba',
                        content=Label(text='Żaden grzyb nie został wykryty', text_size=(200, None), halign="center",
                                      valign="center"),
                        size_hint=(None, None), size=(200, 200))
            pop.open()
            return

    def go_to_mushroom_info(self, value):
        self.popup_to_save.dismiss()
        self.container.remove_widget(self.image)
        self.capture.release()
        cv2.destroyAllWindows()
        sm.current = "mushroom"
        sm.transition.direction = "left"
        return


class MapScreen(Screen):
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MapScreen, self).__init__(**kwargs)

    def on_start(self):
        cursor.execute(
            f"SELECT Name, Latitude, Longitude FROM bmqwq6xgokafzfwckzqj.Localizations WHERE id_user = {account_id}")
        locations = [n for n in cursor]
        for n in locations:
            self.marker = MapMarkerPopup(lat=float(n[1]), lon=float(n[2]), source="Images/marker.png")
            self.bubble = Bubble(background_color=(255, 255, 255))
            self.bubble.add_widget(MDLabel(
                text=n[0],  # 56 znaków
                halign="center",
                size_hint=(None, None),
                height=90,
                theme_text_color="Custom",
                text_color=(0, 0, 1, 1),
            ))
            self.marker.add_widget(self.bubble)
            self.container.add_marker(self.marker)

    def get_lat(self):
        g = geocoder.ip('me')
        return g.latlng[0]

    def get_lon(self):
        g = geocoder.ip('me')
        return g.latlng[1]

    def go_back(self):
        sm.current = "save_location"
        sm.transition.direction = "right"
        return


class SaveLocation(Screen):
    container = ObjectProperty(None)
    input1 = ObjectProperty(None)
    temp_btn1 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SaveLocation, self).__init__(**kwargs)
        self.save_manually_flag = False

    def set_default_values(self):
        self.temp_btn1.text = ""

    def initialize(self):
        self.input1.bind(text=self.on_text)

    def clear_widgets(self):
        self.input1.text = ""
        self.save_manually_flag = False
        try:
            self.container.remove_widget(self.temp_input1)
            self.container.remove_widget(self.temp_input2)
            self.container.remove_widget(self.temp_btn1)
        except:
            pass

    def on_text(self, instance, value):
        if len(value) > 56:
            self.input1.text = value[:56]

    def check_len(self, instance, value):
        if len(value) > 20:
            self.temp_input1.text = self.temp_input1.text[:20]
            self.temp_input2.text = self.temp_input2.text[:20]

    def save_location_automatically(self):
        self.value1 = self.get_lat()
        self.value2 = self.get_lon()
        box = BoxLayout(orientation='vertical', padding=(10))
        box.add_widget(Label(
            text=f"Czy napewno zapisać szerokość {self.value1} oraz długość {self.value2} pod nazwą {self.input1.text}?",
            text_size=(200, None), halign="center", valign="center"))
        btn1 = Button(text="Tak, zapisz", size_hint_y=0.3)
        btn2 = Button(text="Nie, powróć", size_hint_y=0.3)
        box.add_widget(btn1)
        box.add_widget(btn2)

        self.popup_to_save = Popup(title='Upewnij się', title_size=(16),
                                   title_align='center', content=box,
                                   size_hint=(None, None), size=(200, 200), size_hint_y=0.5,
                                   auto_dismiss=True)

        btn1.bind(on_press=self.save_to_database)
        btn2.bind(on_press=self.popup_to_save.dismiss)
        self.popup_to_save.open()

    def save_location_manually(self, value):
        try:
            self.value1 = float(self.temp_input1.text)
            self.value2 = float(self.temp_input2.text)
            if (self.value1 > 89.99 or self.value1 < -89.99) or (self.value2 > 179.99 or self.value2 < -179.99):
                raise Exception("Wprowadzono wartości powyżej 180 lub poniżej -180")
        except:
            pop = Popup(title='Błąd zapisu', size_hint=(None, None), size=(200, 200),
                        content=Label(text='Wprowadzono błędne wartości liczbowe', text_size=(200, None),
                                      halign="center", valign="center"))
            pop.open()
            return

        box = BoxLayout(orientation='vertical', padding=(10))
        box.add_widget(Label(
            text=f"Czy napewno zapisać szerokość {self.value1} oraz długość {self.value2} pod nazwą {self.input1.text}?",
            text_size=(200, None), halign="center", valign="center"))
        btn1 = Button(text="Tak, zapisz", size_hint_y=0.3)
        btn2 = Button(text="Nie, powróć", size_hint_y=0.3)
        box.add_widget(btn1)
        box.add_widget(btn2)

        self.popup_to_save = Popup(title='Upewnij się', title_size=(16),
                                   title_align='center', content=box,
                                   size_hint=(None, None), size=(200, 200), size_hint_y=0.5,
                                   auto_dismiss=True)

        btn1.bind(on_press=self.save_to_database)
        btn2.bind(on_press=self.popup_to_save.dismiss)
        self.popup_to_save.open()

    def save_to_database(self, value):
        global account_id
        self.popup_to_save.dismiss()
        if len(self.input1.text) == 0:
            pop = Popup(title='Błąd zapisu',
                        content=Label(text='Nazwa lokacji nie może być pusta', text_size=(200, None), halign="center",
                                      valign="center"),
                        size_hint=(None, None), size=(200, 200))
            pop.open()
            return
        try:
            cursor.execute(
                f"SELECT Name, Latitude, Longitude FROM bmqwq6xgokafzfwckzqj.Localizations WHERE id_user = {account_id}")
            locations = [n for n in cursor]
            for n in range(len(locations)):
                if locations[n][1] == str(self.value1) and locations[n][2] == str(self.value2):
                    pop = Popup(title='Błąd zapisu danych',
                                content=Label(text=f'To miejsce zostało już zapisane jako: {locations[n][0]}',
                                              text_size=(200, None), halign="center", valign="center"),
                                size_hint=(None, None), size=(200, 200))
                    pop.open()
                    return
            cursor.execute(
                f"INSERT INTO bmqwq6xgokafzfwckzqj.Localizations VALUES ('{self.input1.text}', '{self.value1}', '{self.value2}', {account_id});")
            connection.commit()
            pop = Popup(title='Zapis do bazy',
                        content=Label(text='Dane zostały poprawnie zapisane do bazy', text_size=(200, None),
                                      halign="center", valign="center"),
                        size_hint=(None, None), size=(200, 200))
            pop.open()
            self.clear_widgets()
        except Exception as e:
            pop = Popup(title='Błąd zapisu danych',
                        content=Label(text=f'Dane nie zostały zapisane. Wystąpił błąd: {e}', text_size=(200, None),
                                      halign="center", valign="center"),
                        size_hint=(None, None), size=(200, 200))
            pop.open()

    def save_manually(self):
        if self.save_manually_flag:
            return
        self.temp_input1 = TextInput(hint_text='Szerokosc geograficzna', multiline=False,
                                     pos_hint={"x": 0.27, "top": 0.5}, size_hint=(0.5, 0.05))
        self.temp_input2 = TextInput(hint_text='Dlugosc geograficzna', multiline=False,
                                     pos_hint={"x": 0.27, "top": 0.42}, size_hint=(0.5, 0.05))
        self.temp_input1.bind(text=self.check_len)
        self.temp_input2.bind(text=self.check_len)
        self.temp_btn1 = Button(text="Zapisz", size_hint=(0.3, 0.1), pos_hint={"x": 0.35, "top": 0.35}, bold=True,
                                background_color="#6d8b74", background_normal="", color="black",
                                on_release=self.save_location_manually)
        self.container.add_widget(self.temp_input1)
        self.container.add_widget(self.temp_input2)
        self.container.add_widget(self.temp_btn1)
        self.save_manually_flag = True

    def get_lat(self):
        g = geocoder.ip('me')
        return g.latlng[0]

    def get_lon(self):
        g = geocoder.ip('me')
        return g.latlng[1]

    def go_back(self):
        sm.current = "main"
        sm.transition.direction = "right"
        return

    def go_to_locations_list(self):
        sm.current = "locations_list"
        sm.transition.direction = "left"
        return

    def go_to_map(self):
        sm.current = "map_screen"
        sm.transition.direction = "left"
        return


class Login(Screen):
    login_input = ObjectProperty(None)
    password_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)

    def log_in(self):
        global account_id
        cursor.execute(
            f'Select id_user, login, password from bmqwq6xgokafzfwckzqj.Users where login = "{self.login_input.text}"')
        account = []
        for n in cursor:
            for elem in n:
                account.append(elem)
        if len(account) == 0:
            pop = Popup(title='Błąd logowania',
                        content=Label(text='Błędne dane logowania', text_size=(200, None), halign="center",
                                      valign="center"),
                        size_hint=(None, None), size=(200, 200))
            pop.open()
            return
        password = bytes(self.password_input.text, encoding='utf-8')
        code = hashlib.sha512()
        code.update(password)
        code = code.hexdigest()
        if str(code) == account[2]:
            account_id = account[0]
            pop = Popup(title='Logowanie',
                        content=Label(text='Zalogowano do systemu', text_size=(200, None), halign="center",
                                      valign="center"),
                        size_hint=(None, None), size=(200, 200))
            pop.open()
            self.login_input.text = ""
            self.password_input.text = ""
            sm.current = "main"
            sm.transition.direction = "left"
            return
        else:
            pop = Popup(title='Błąd logowania',
                        content=Label(text='Błędne dane logowania', text_size=(200, None), halign="center",
                                      valign="center"),
                        size_hint=(None, None), size=(200, 200))
            pop.open()
            return

    def go_to_registration(self):
        self.login_input.text = ""
        self.password_input.text = ""
        sm.current = "register"
        sm.transition.direction = "left"
        return


class Register(Screen):
    login_input = ObjectProperty(None)
    password_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Register, self).__init__(**kwargs)

    def register_account(self):
        cursor.execute(f'Select login from bmqwq6xgokafzfwckzqj.Users')
        logins = [n[0] for n in cursor]
        if self.login_input.text in logins:
            pop = Popup(title='Błąd rejestracji',
                        content=Label(text='Takie konto już istnieje,\npodaj inny login', text_size=(200, None),
                                      halign="center", valign="center"),
                        size_hint=(None, None), size=(200, 200))
            pop.open()
        else:
            if len(self.password_input.text) < 3:
                pop = Popup(title='Błąd hasła',
                            content=Label(text='Hasło zbyt krótkie', text_size=(200, None), halign="center",
                                          valign="center"),
                            size_hint=(None, None), size=(200, 200))
                pop.open()
                return
            password = bytes(self.password_input.text, encoding='utf-8')
            #some_secrete_code
            code.update(password)
            code = code.hexdigest()
            try:
                cursor.execute(
                    f"INSERT INTO bmqwq6xgokafzfwckzqj.Users (login, password) VALUES ('{self.login_input.text}', '{str(code)}')")
                connection.commit()
            except Exception as e:
                pop = Popup(title='Błąd',
                            content=Label(text=f'{e}', text_size=(200, None), halign="center", valign="center"),
                            size_hint=(None, None), size=(200, 200))
                pop.open()
                return
            pop = Popup(title='Rejestracja',
                        content=Label(text='Konto zostało założone', text_size=(200, None), halign="center",
                                      valign="center"),
                        size_hint=(None, None), size=(200, 200))
            pop.open()
            self.go_back()

    def go_back(self):
        self.login_input.text = ""
        self.password_input.text = ""
        sm.current = "login"
        sm.transition.direction = "right"
        return


class LocationsList(Screen):
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(LocationsList, self).__init__(**kwargs)

    def clear_widgets(self):
        self.container.remove_widget(self.scroll)

    def add_buttons(self):
        self.scroll = ScrollView()
        list_view = MDList()
        cursor.execute(
            f"SELECT Name, Latitude, Longitude FROM bmqwq6xgokafzfwckzqj.Localizations WHERE id_user = {account_id}")
        self.locations = [n for n in cursor]
        for i in range(len(self.locations)):
            items = ThreeLineListItem(text=self.locations[i][0],
                                      secondary_text=f"Szerokość geograficzna: {self.locations[i][1]}",
                                      tertiary_text=f"Długość geograficzna: {self.locations[i][2]}",
                                      on_release=self.delete_location)
            list_view.add_widget(items)
        self.scroll.add_widget(list_view)
        self.container.add_widget(self.scroll)

    def delete_location(self, item):
        box = BoxLayout(orientation='vertical', padding=(10))
        box.add_widget(
            Label(text=f"Czy napewno chcesz usunąć lokalizację o nazwie: {item.text}?", text_size=(200, None),
                  halign="center", valign="center"))
        btn1 = Button(text="Tak, usuń", size_hint_y=0.3)
        btn2 = Button(text="Nie, powróć", size_hint_y=0.3)
        box.add_widget(btn1)
        box.add_widget(btn2)

        self.popup_to_save = Popup(title='Upewnij się', title_size=(16),
                                   title_align='center', content=box,
                                   size_hint=(None, None), size=(200, 200), size_hint_y=0.5,
                                   auto_dismiss=True)

        btn1.bind(on_press=lambda x: self.delete_location_from_database(item.text))
        btn2.bind(on_press=self.popup_to_save.dismiss)
        self.popup_to_save.open()

    def delete_location_from_database(self, text):
        global account_id
        self.popup_to_save.dismiss()
        to_delete = ()
        for n in self.locations:
            if text in n:
                to_delete = n
        try:
            cursor.execute(
                f"DELETE FROM bmqwq6xgokafzfwckzqj.Localizations WHERE Name = '{to_delete[0]}' and Latitude = '{to_delete[1]}' and Longitude = '{to_delete[2]}' and id_user = {account_id}")
            connection.commit()
        except Exception as e:
            pop = Popup(title='Błąd',
                        content=Label(text=f'{e}', text_size=(200, None), halign="center", valign="center"),
                        size_hint=(None, None), size=(200, 200))
            pop.open()
            return
        pop = Popup(title='Usunięto',
                    content=Label(text=f'Lokalizacja o nazwie: {to_delete[0]} została usunięta', text_size=(200, None),
                                  halign="center", valign="center"),
                    size_hint=(None, None), size=(200, 200))
        pop.open()
        self.go_back()

    def go_back(self):
        self.clear_widgets()
        sm.current = "save_location"
        sm.transition.direction = "right"
        return


class Mushroom(Screen):
    container = ObjectProperty(None)
    name_label = ObjectProperty(None)
    edible_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Mushroom, self).__init__(**kwargs)

    def clear_widgets(self):
        self.container.remove_widget(self.img)

    def add_background_features(self):
        global mushroom_id
        cursor.execute(
            f"Select nazwa_Polska, Trujacy_Jadalny from bmqwq6xgokafzfwckzqj.grzyby where id = {mushroom_id}")
        mushroom_data = [n for n in cursor]
        self.img = Image(source=f"Images/{mushroom_id}.jpg")
        self.img.pos = (Window.size[0] / 4.8, Window.size[1] / 4.92)
        self.img.size_hint = (0.6, 1.2)
        self.img.keep_ratio = True
        self.container.add_widget(self.img)
        self.name_label.text = mushroom_data[0][0]
        self.edible_label.text = mushroom_data[0][1]
        if mushroom_data[0][1] == "Jadalny":
            self.edible_label.color = "green"
        else:
            self.edible_label.color = "red"

    def go_to_description(self):
        self.clear_widgets()
        global current_info
        current_info = "opis"
        sm.current = "mushroom_info"
        sm.transition.direction = "left"
        return

    def go_to_mushroom_location(self):
        self.clear_widgets()
        global current_info
        current_info = "Wystepowanie"
        sm.current = "mushroom_info"
        sm.transition.direction = "left"
        return

    def go_to_classification(self):
        self.clear_widgets()
        global current_info
        current_info = "Klasyfikacja"
        sm.current = "mushroom_info"
        sm.transition.direction = "left"
        return

    def go_back(self):
        self.clear_widgets()
        sm.current = "encyclopedia"
        sm.transition.direction = "right"
        return


class MushroomInfo(Screen):
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MushroomInfo, self).__init__(**kwargs)

    def clear_widgets(self):
        self.container.remove_widget(self.scroll)

    def add_background_features(self):
        global current_info, mushroom_id
        cursor.execute(f"Select {current_info} from bmqwq6xgokafzfwckzqj.grzyby where id = {mushroom_id}")
        info = [n[0] for n in cursor]
        self.scroll = ScrollView()
        self.label = Label(text=f"{info[0]}")
        self.label._label.refresh()
        self.label.font_size = 20
        self.label.size_hint = (1, len(info[0]) / (len(info[0]) + len(info[0]) * 0.01))
        self.label.size = self.label.texture_size
        self.label.color = "black"
        self.label.text_size = (250, None)
        self.label.halign = "center"
        self.label.valign = "center"
        self.scroll.add_widget(self.label)
        self.container.add_widget(self.scroll)

    def go_back(self):
        self.clear_widgets()
        sm.current = "mushroom"
        sm.transition.direction = "right"
        return

class FileManager(Screen):
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        Clock.schedule_once(self.init_widget, 0)
        super(FileManager, self).__init__(**kwargs)
        self.flag = False

    def init_widget(self, *args):
        if self.flag:
            return
        fc = self.ids['file_chooser']
        fc.bind(on_entry_added=self.update_file_list_entry)
        fc.bind(on_subentry_to_entry=self.update_file_list_entry)

    def update_file_list_entry(self, file_chooser, file_list_entry, *args):
        file_list_entry.children[0].color = (0.0, 0.0, 0.0, 1.0)  # File Names
        file_list_entry.children[1].color = (0.0, 0.0, 0.0, 1.0)  # Dir Names`

    def go_back(self):
        self.flag = True
        sm.current = "camera_screen"
        sm.transition.direction = "right"
        return
    
    def selected(self, filename):
        filename = str(filename).replace('\\\\','\\')[2:-2]
        try:
            self.taken_photo = im = pil.open(rf"{filename}")
            self.taken_photo = self.taken_photo.save('grzyb.jpg')
        except:
            pass
        form = MultipartEncoder(
            fields={
                'box_threshold': '0.5',
                'number_threshold': '0.3',
                'file': ('grzyb.jpg', open('grzyb.jpg', 'rb'), 'image/jpg')
            }
        )
        #http://127.0.0.1:5000/ - for localhost
        #http://172.105.71.50:5000/images - for server
        self.response = requests.post('http://127.0.0.1:5000/images', data=form,
                                      headers={'Content-Type': form.content_type})
        response_dict = json.loads(self.response.text)
        if len(response_dict['grzyb']) != 0:
            global mushroom_id
            cursor.execute(
                f"Select id, nazwa_Polska from bmqwq6xgokafzfwckzqj.grzyby where nazwa_Lacinska = '{response_dict['grzyb']}'")
            mushroom_info = [n for n in cursor]
            mushroom_id = int(mushroom_info[0][0])
            mushroom_name = mushroom_info[0][1]
            confidence = round(float(response_dict['confidence']) * 100, 2)
            box = BoxLayout(orientation='vertical', padding=(10))
            box.add_widget(Label(
                text=f"Wykryto grzyba:\n{mushroom_name}\nPrawdopodobieństwo: {confidence}%\nCzy pokazać informacje na temat tego grzyba?",
                text_size=(200, None), halign="center", valign="center"))
            btn1 = Button(text="Tak, pokaż", size_hint_y=0.3)
            btn2 = Button(text="Nie, powróć", size_hint_y=0.3)
            box.add_widget(btn1)
            box.add_widget(btn2)

            self.popup_to_save = Popup(title='Wykryto grzyba', title_size=(16),
                                       title_align='center', content=box,
                                       size_hint=(None, None), size=(200, 200), size_hint_y=0.5,
                                       auto_dismiss=True)

            btn1.bind(on_press=self.go_to_mushroom_info)
            btn2.bind(on_press=self.popup_to_save.dismiss)
            self.popup_to_save.open()
        else:
            pop = Popup(title='Nie wykryto grzyba',
                        content=Label(text='Żaden grzyb nie został wykryty', text_size=(200, None), halign="center",
                                      valign="center"),
                        size_hint=(None, None), size=(200, 200))
            pop.open()
            return

    def go_to_mushroom_info(self, value):
        self.popup_to_save.dismiss()
        self.flag = True
        sm.current = "mushroom"
        sm.transition.direction = "left"
        return


class RunApp(MDApp):
    def stop(self, *args):
        items = os.listdir("cache")
        for item in items:
            os.remove(f"cache/{item}")

    def close_app(self, *args):   
        super(RunApp, self).stop(*args)

    def build(self):
        return sm


if __name__ == "__main__":
    app = RunApp()
    kv = Builder.load_file("my.kv")
    sm = WindowManager()
    screens = [Login(name="login"), Register(name="register"), MainWindow(name="main"), Quiz(name="quiz"),
               Encyclopedia(name="encyclopedia"),
               CameraScreen(name="camera_screen"), MapScreen(name="map_screen"), SaveLocation(name="save_location"),
               LocationsList(name="locations_list"), Mushroom(name="mushroom"), MushroomInfo(name="mushroom_info"),
               FileManager(name="file_manager")]
    for screen in screens:
        sm.add_widget(screen)
    app.run()