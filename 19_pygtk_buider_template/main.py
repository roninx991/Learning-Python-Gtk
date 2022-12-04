#!/usr/bin/env python3
# FILE: menu.py
# RUN : python3 main.py
# Edited : 3.12.2022

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import sys

class Handler:
    def on_button_clicked(self, button):
        print("Button clicked!")

    def on_togglebutton_toggled(self, togglebutton):
        print("ToggleButton toggled!")

    def on_exit_application(self, *args):
        Gtk.main_quit()

    def on_close_btn_clicked(self, close_btn):
        sys.exit()

builder = Gtk.Builder()
builder.add_from_file("builder.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
