import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import sys

class Handler:
    
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        print("Hello World!")
    def on_close_btn_clicked(self, button):
        sys.exit()

    def on_calc_btn_clicked(self, button):
        mile = float(mile_ent.get_text())
        km = mile * 1.60944
        calc_ent.set_text(str(km))

builder = Gtk.Builder()
builder.add_from_file("21_pygtk_cambalache.ui")
builder.connect_signals(Handler())

mile_ent = builder.get_object("mile_ent")
calc_ent = builder.get_object("calc_ent")

window = builder.get_object("window1")
window.show_all()

Gtk.main()
