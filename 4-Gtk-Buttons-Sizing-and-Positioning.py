from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_border_width(10)

        grid = Gtk.Grid()
        self.add(grid)

        # Create a bunch of buttons

        button1 = Gtk.Button("Button1")
        button2 = Gtk.Button("Button2")
        button3 = Gtk.Button("Button3")
        button4 = Gtk.Button("Button4")
        button5 = Gtk.Button("Button5")
        button6 = Gtk.Button("Button6")

        grid.add(button1)

        grid.attach(button2, 1, 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)


window = MainWindow()

window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()