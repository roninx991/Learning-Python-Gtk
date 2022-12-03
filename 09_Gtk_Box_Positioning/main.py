#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_border_width(10)
        self.set_default_size(500, 300)

        # Boxes
        hbox = Gtk.Box(spacing=20)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox_right.set_homogeneous(False)

        # Pack the 2 columns
        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        label = Gtk.Label("This is a main label")
        vbox_left.pack_start(label, True, True, 0)

        # Left Aligned
        label = Gtk.Label()
        label.set_text("This is left aligned text.\nOH WOW multiple lines sooooo cool")
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.pack_start(label, True, True, 0)

        # Right Aligned
        label = Gtk.Label()
        label.set_text("This is right aligned text.\nMultiple lines")
        label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.pack_start(label, True, True, 0)

        # Line wrap
        label = Gtk.Label("Hi my name is Sangat\nHi my name is Sangat\nHi my name is Sangat\n")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        vbox_right.pack_start(label, True, True, 0)

        # Markup
        label = Gtk.Label()
        label.set_markup("<small>Small Text</small>\n"
                         "<big>Big Text</big>\n"
                         "<b>Bold Text</b>\n"
                         "<a href=\"https://www.google.com\">Visit Google</a>\n")
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)
        self.add(hbox)


window = MainWindow()

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
