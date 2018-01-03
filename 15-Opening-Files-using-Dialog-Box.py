from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_border_width(30)
        layout = Gtk.Box(spacing=6)
        self.add(layout)

        button = Gtk.Button("Choose File")
        button.connect("clicked", self.on_file_clicked)
        layout.add(button)

    # User clicked the choose file button
    def on_file_clicked(self, widget):

        dialog = Gtk.FileChooserDialog("Select a file", self, Gtk.FileChooserAction.OPEN,
                                      ("Cancel", Gtk.ResponseType.CANCEL,
                                       "OK", Gtk.ResponseType.OK))
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print "You clicked the OK button"
            print "File selected " + dialog.get_filename()

        elif response == Gtk.ResponseType.CANCEL:
            print "User didn't choose any file"

        dialog.destroy()

window = MainWindow()

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
