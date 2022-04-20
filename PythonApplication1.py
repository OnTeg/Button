from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
<ContentNavigationDrawer>

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Introducion"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "First App"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"

            OneLineListItem:
                text: "Second App"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Applications"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"
                MDLabel:
                    text: "Hello! Here you can open some pre-installed applications. Use menu to choose app."
                    halign: "center"

            MDScreen:
                name: "scr 2"
                MDIconButton:
                    icon: "apps"
                    pos_hint: {"center_x": .5, "center_y": .2}
                    on_press: 
                        self.icon = "android"
                    on_release:
                        self.icon = "apps"
                MDLabel:
                    text: "Description..."
                    halign: "center"

            MDScreen:
                name: "scr 3"
                MDIconButton:
                    icon: "android"
                    pos_hint: {"center_x": .5, "center_y": .2}
                    on_press: 
                        self.icon = "apps"
                    on_release:
                        self.icon = "android"
                MDLabel:
                    text: "Description..."
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Btn(MDApp):
    def build(self):
        return Builder.load_string(KV)


Btn().run()