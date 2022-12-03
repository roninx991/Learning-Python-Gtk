#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_default_size(200, 100)
        self.set_border_width(30)

        button = Gtk.Button("Pop-Up")
        button.connect("clicked", self.button_clicked)
        self.add(button)

    def button_clicked(self, widget):
        dialog = PopUp(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print ("You clicked the OK button")
        elif response == Gtk.ResponseType.CANCEL:
            print ("You clicked the CANCEL button")

        dialog.destroy()


class PopUp(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Popup Dialog", parent, Gtk.DialogFlags.MODAL, (
            "Custom cancel text", Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        ))
        self.set_default_size(200, 100)
        self.set_border_width(30)

        area = self.get_content_area()
        area.add(Gtk.Label("Wow this popup is amazing"))
        self.show_all()


window = MainWindow()

window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
