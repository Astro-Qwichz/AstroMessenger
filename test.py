from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class AppMessenger(App):

    def build(self):
        self.layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        self.title_label = Label(
            text="AstroVR",
            font_size=32
        )

        self.login = TextInput(
            hint_text="Логин",
            multiline=False
        )

        self.password = TextInput(
            hint_text="Пароль",
            password=True,
            multiline=False
        )

        self.confirm = TextInput(
            hint_text="Повторите пароль",
            password=True,
            multiline=False
        )

        self.show_password = Button(
            text="👁 Показать пароль",
            size_hint_y=None,
            height=50
        )
        self.show_password.bind(on_press=self.toggle_password)

        self.continue_button = Button(
            text="Продолжить",
            size_hint_y=None,
            height=55
        )
        self.continue_button.bind(on_press=self.register)

        self.message = Label(text="")

        for widget in [
            self.title_label,
            self.login,
            self.password,
            self.confirm,
            self.show_password,
            self.continue_button,
            self.message
        ]:
            self.layout.add_widget(widget)

        return self.layout

    def toggle_password(self, button):
        self.password.password = not self.password.password
        self.confirm.password = not self.confirm.password

    def register(self, button):
        if not self.login.text or not self.password.text:
            self.message.text = "Заполни все поля!"
            return

        if self.password.text != self.confirm.text:
            self.message.text = "Пароли не совпадают!"
            return

        self.main_menu()

    def main_menu(self):
        self.layout.clear_widgets()

        self.layout.add_widget(
            Label(
                text=f"Добро пожаловать, {self.login.text}!",
                font_size=25
            )
        )

        self.layout.add_widget(
            Button(text="💬 Чаты")
        )

        self.layout.add_widget(
            Button(text="⭐ Избранное")
        )

        self.layout.add_widget(
            Button(text="⚙ Настройки")
        )


AppMessenger().run()