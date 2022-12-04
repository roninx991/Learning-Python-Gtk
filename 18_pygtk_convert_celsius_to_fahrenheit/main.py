#!/usr/bin/env python
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):

        super().__init__(title="Grid Example")

        celsius_lb = Gtk.Label(label="Celsius")
        self.cels_ent = Gtk.Entry()

        calc_but = Gtk.Button(label="Calculeaza")
        calc_but.connect("clicked", self.on_calc_but)

        fahr_lb = Gtk.Label(label="Fahrenheit: ")
        self.fahr_ent = Gtk.Entry()
        
        close_but = Gtk.Button(label="Close")
        close_but.connect("clicked", self.on_close_but)
        
        #button3 = Gtk.Button(label="Button 3")
        #button4 = Gtk.Button(label="Button 4")
        #button5 = Gtk.Button(label="Button 5")
        #button6 = Gtk.Button(label="Button 6")

        grid = Gtk.Grid()
        grid.add(celsius_lb)
        
        grid.attach(self.cels_ent, 1, 0, 2, 1)
        
        grid.attach(calc_but, 3, 0, 2, 1)
        
        grid.attach(fahr_lb, 0, 1, 1, 1)
        
        grid.attach(self.fahr_ent, 1, 1, 2, 1)
        
        grid.attach(close_but, 3, 1, 2, 1)

        self.add(grid)

    def on_close_but(self, widget):
        print("Inchiderea aplicatiei.")
        self.close()

    def on_calc_but(self, calc_but):
        print(self.cels_ent.get_text())
        cels = float(self.cels_ent.get_text())
        fahr = (cels * 9/5) + 32
        self.fahr_ent.set_text(str(fahr))


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
