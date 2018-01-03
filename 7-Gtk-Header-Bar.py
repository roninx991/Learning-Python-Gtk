from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_border_width(10)

        self.set_default_size(500, 400)

        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Rippin Music Player"
        self.set_titlebar(header_bar)

        # Audio button on right
        audio_button = Gtk.Button()
        cd_icon = Gio.ThemedIcon(name="gnome-dev-cdrom-audio")
        image = Gtk.Image.new_from_gicon(cd_icon, Gtk.IconSize.BUTTON)
        audio_button.add(image)
        header_bar.pack_end(audio_button)

        # Create box of linked items
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        # Left Arrow
        left_arrow = Gtk.Button()
        left_arrow.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(left_arrow)

        # Right Arrow
        right_arrow = Gtk.Button()
        right_arrow.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(right_arrow)

        header_bar.pack_start(box)
        self.add(Gtk.TextView())


window = MainWindow()

window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()