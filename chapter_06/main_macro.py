from ceiling import *
from garage import *
from tv import *
from hottub import *
from light import *
from stereo import *
from remote import RemoteControl
from command import MacroCommand


def main() -> None:
    remote_control = RemoteControl()
    light = Light("Living Room")
    tv = TV("Living Room")
    stereo = Stereo("Living Room")
    hottub = Hottub()

    light_on = LightOnCommand(light)
    stereo_on = StereoOnWithCDCommand(stereo)
    tv_on = TVOnCommand(tv)
    hottub_on = HottubOnCommand(hottub)
    light_off = LightOffCommand(light)
    stereo_off = StereoOffCommand(stereo)
    tv_off = TVOffCommand(tv)
    hottub_off = HottubOffCommand(hottub)

    party_on = [light_on, stereo_on, tv_on, hottub_on]
    party_off = [light_off, stereo_off, tv_off, hottub_off]

    party_on_macro = MacroCommand(party_on)
    party_off_macro = MacroCommand(party_off)
    remote_control.set_command(0, party_on_macro, party_off_macro)

    print(remote_control)
    print("--- Pushing Macro On---")
    remote_control.on_button_was_pushed(0)
    print("--- Pushing Macro Off---")
    remote_control.off_button_was_pushed(0)
    print("--- Pushing Macro Undo---")
    remote_control.undo_button_was_pushed()


if __name__ == "__main__":
    main()
