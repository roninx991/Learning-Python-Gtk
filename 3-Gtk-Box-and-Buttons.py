from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_border_width(10)

        # Box
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        self.bacon_button = Gtk.Button(label="Bacon")
        self.bacon_button.connect("clicked",self.bacon_clicked)
        self.box.pack_start(self.bacon_button, True, True, 0)

        self.spinach_button = Gtk.Button(label="Spinach")
        self.spinach_button.connect("clicked",self.spinach_clicked)
        self.box.pack_start(self.spinach_button, True, True, 0)

    def bacon_clicked(self, widget):
        print "Bacon is not healthy"

    def spinach_clicked(self, widget):
        print "Spinach is healthy"


window = MainWindow()

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()