# from window.kalkulatorgui import KalkulatorGUI
from graph import Graph
# File: main.py
# from window.hellogui import HelloGUI


class Main:
    @staticmethod
    def main():
        # main_window = HelloGUI()
        # main_window = KalkulatorGUI()
        main_window = Graph()
        main_window.show()


Main.main()
