from gi.repository import Gtk, Gio


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_border_width(10)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        # Stack
        main_area = Gtk.Stack()
        main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        main_area.set_transition_duration(1000)

        # Checkbox
        check_button = Gtk.CheckButton("Dont check me")
        main_area.add_titled(check_button, "check_name", "Check Box")

        # Label
        label = Gtk.Label()
        label.set_markup("<big>OMG this text is huge</big>")
        main_area.add_titled(label, "label_name", "Big label")

        # StackSwitcher
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(main_area)
        box.pack_start(stack_switcher,True,True,0)
        box.pack_start(main_area,True,True,0)


window = MainWindow()

window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()