#!/usr/bin/env python3
# FILE: menu.py
# RUN : python3 main.py
# Edited : 3.12.2022

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
import sys

class ApplicationWindow(Gtk.ApplicationWindow):
    def __init__(self, application):
        Gtk.Window.__init__(self, application=application)
        self.set_title("Application")
        self.set_default_size(200, 200)

        grid = Gtk.Grid()
        self.add(grid)

        menubutton = Gtk.MenuButton()
        grid.attach(menubutton, 0, 0, 1, 1)

        menumodel = Gio.Menu()
        menubutton.set_menu_model(menumodel)
        menumodel.append("New", "app.new")
        menumodel.append("Quit", "app.quit")

class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        window = ApplicationWindow(self)
        window.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        new_action = Gio.SimpleAction.new("new", None)
        new_action.connect("activate", self.new_callback)
        self.add_action(new_action)

        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_callback)
        self.add_action(quit_action)

    def new_callback(self, action, parameter):
        print("You clicked New")

    def quit_callback(self, action, parameter):
        print("You clicked Quit")
        #self.quit()
        sys.exit()

application = Application()
exit_status = application.run(sys.argv)
sys.exit(exit_status)
