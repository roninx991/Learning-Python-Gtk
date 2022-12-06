#!/usr/bin/env python3
# FILE: menu.py
# RUN : python3 main.py
# Edited : 3.12.2022
Title   = "Calculator Dobanda"
Version = "Version 4.12.2022"
Authors = ["Mihai Cornel"]
Website = "https://github.com/mhcrnl/Learning-Python-Gtk"

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

    def on_calc_btn_clicked(self, button):
        dobanda = float(vn_ent.get_text())*float(rd_ent.get_text())/100*1/float(nl_ent.get_text())

        do_ent.set_text(str(dobanda))

    def on_desp_btn_clicked(self, button):
        desp = Gtk.AboutDialog()
        desp.set_program_name(Title)
        desp.set_version(Version)
        desp.set_authors(Authors)
        desp.set_website(Website)
        desp.present()

builder = Gtk.Builder()
builder.add_from_file("builder.glade")
builder.connect_signals(Handler())

vn_ent = builder.get_object("vn_ent")
do_ent = builder.get_object("do_ent")
rd_ent = builder.get_object("rd_ent")
nl_ent = builder.get_object("nl_ent")

window = builder.get_object("window1")
window.show_all()

Gtk.main()
