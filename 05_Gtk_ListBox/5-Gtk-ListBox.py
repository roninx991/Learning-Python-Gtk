#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_border_width(10)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)

        # Check box
        row1 = Gtk.ListBoxRow()
        box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row1.add(box1)
        label = Gtk.Label("Chekc if you love cheese burgers")
        check = Gtk.CheckButton()
        box1.pack_start(label, True, True, 0)
        box1.pack_start(check, True, True, 0)
        listbox.add(row1)

        # Toggle Switch
        row2 = Gtk.ListBoxRow()
        box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row2.add(box2)
        label = Gtk.Label("Burger Making Machine")
        switch = Gtk.Switch()
        box2.pack_start(label, True, True, 0)
        box2.pack_start(switch, True, True, 0)
        listbox.add(row2)

window = MainWindow()

window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
