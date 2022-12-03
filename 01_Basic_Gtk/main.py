#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_border_width(10)

        self.close_bt = Gtk.Button(label="Close")
        self.close_bt.connect("clicked", self.on_close_bt)
        self.add(self.close_bt)

    def on_close_bt(self, widget):
        print("Bye!")
        self.close()


window = MainWindow()

window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
