import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class RunamatchApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))
        start_button = toga.Button(
            "Iniciar Juego",
            on_press=self.start_game,
            style=Pack(padding=10)
        )
        main_box.add(start_button)
        self.main_window = toga.MainWindow(title=self.name)
        self.main_window.content = main_box
        self.main_window.show()

    def start_game(self, widget):
        # Aquí iría tu lógica del juego
        print("Juego iniciado")

def main():
    return RunamatchApp("Runamatch", "org.example.runamatch")
