#!/usr/bin/env python3
# FILE: menu.py
# RUN : python3 main.py
# Edited : 3.12.2022
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_size_request(250,250)
        self.set_border_width(10)

        self.menu_bar = Gtk.MenuBar()
        
        self.file_menu = Gtk.Menu()
        
        self.file_item = Gtk.MenuItem(label="File")
        self.file_item.set_submenu(self.file_menu)

        self.exit_item = Gtk.MenuItem(label="Exit")
        self.exit_item.connect("activate", self.on_close_bt)
        self.file_menu.append(self.exit_item)
        #self.file_item.show()
        #self.file_item.set_submenu(self.file_menu)

        self.file_menu.append(self.exit_item)
        self.menu_bar.append(self.file_item)
        
        self.vbox = Gtk.VBox(False, 2)
        self.vbox.pack_start(self.menu_bar, False, False,0)

        self.add(self.vbox)

        self.close_bt = Gtk.Button(label="Close")
        self.close_bt.connect("clicked", self.on_close_bt)
        self.add(self.close_bt)

        self.show_all()

    def on_close_bt(self, widget):
        print("Bye!")
        self.close()


window = MainWindow()

window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
