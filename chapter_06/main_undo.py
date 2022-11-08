from ceiling import *
from garage import *
from tv import *
from hottub import *
from light import *
from stereo import *
from remote import RemoteControl


def main() -> None:
    remote_control = RemoteControl()
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    ceiling_fan = CeilingFan("Living Room")
    garage_door = GarageDoor("")
    stereo = Stereo("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_med = CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_low = CeilingFanLowCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    garage_door_up = GarageDoorUpCommand(garage_door)
    garage_door_down = GarageDoorDownCommand(garage_door)

    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_med, ceiling_fan_off)
    remote_control.set_command(3, ceiling_fan_high, ceiling_fan_off)
    remote_control.set_command(4, stereo_on_with_cd, stereo_off)

    print(f"[slot 0] test ----")
    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    print(str(remote_control))

    remote_control.undo_button_was_pushed()

    print(f"\n[slot 1] test ----")
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)

    print(f"\n[slot 2] test ----")
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    print(str(remote_control))
    remote_control.undo_button_was_pushed()

    print(f"\n[slot 3] test ----")
    remote_control.on_button_was_pushed(3)
    print(str(remote_control))
    remote_control.undo_button_was_pushed()

    print(f"\n[slot 4] test ----")
    remote_control.on_button_was_pushed(4)
    remote_control.off_button_was_pushed(4)
    remote_control.undo_button_was_pushed()
    remote_control.undo_button_was_pushed()


if __name__ == "__main__":
    main()
