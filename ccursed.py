
from cursed import CursedApp, CursedWindow

app = CursedApp()


class MainWindow(CursedWindow):
    X, Y = (0, 0)
    WIDTH, HEIGHT = ('max', 'max')

    BORDERED=True

    @classmethod
    def update(cls):
        cls.addstr('hello', 0, 0)
        if cls.getch() == 27:
            cls.trigger('quit')


result = app.run()
if result.interrupted():
    print('quit!')
else:
    result.unwrap()
