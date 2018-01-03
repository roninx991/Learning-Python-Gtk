from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_border_width(10)

window = MainWindow()

window = Gtk.Window()

label = Gtk.Label()
label.set_label("OMG I think I am awesome")
label.set_angle(30)
label.set_halign(Gtk.Align.END)
window.add(label)

print label.get_properties("angle")

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()