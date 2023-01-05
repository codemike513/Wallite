import flet
from flet import Page
from app import App

def start(page: Page):
    page.title = 'Wallite'
    page.window_width = 450
    page.window_height = 790

    page.update()
    app = App()
    page.add(app)

if __name__ == "__main__":
    flet.app(target=start)