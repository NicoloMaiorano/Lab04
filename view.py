from cProfile import label

import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.__btnCheck = None
        self.txtOut = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        row1 = ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)

        # Add your stuff here
        self.__ddLingua = ft.Dropdown(label="Language", width=600,options=[ft.dropdown.Option("Italian"), ft.dropdown.Option("English"), ft.dropdown.Option("Spanish")])

        row2 = ft.Row([self.__ddLingua])

        self.__ddRicerca = ft.Dropdown(label="Language", width=200,
                                      options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"),
                                               ft.dropdown.Option("Dichotomic")])

        self.txtIn = ft.TextField(label="Add your sentence here", width=400)
        self.__btnCheck = ft.ElevatedButton("Spell check", on_click=self.__controller.handleSentence)

        row3 = ft.Row([self.__ddRicerca, self.txtIn, self.__btnCheck])
        self.txtOut = ft.ListView(expand=True)
        row4 = ft.Row([self.txtOut])
        self.page.add(row1, row2, row3, row4)
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

    def getDDRicerca(self):
        return self.__ddRicerca.value

    def getDDLingua(self):
        return self.__ddLingua.value