def on_button_pressed_a():
    global angle
    angle = 90
    pins.servo_write_pin(AnalogPin.P13, angle)
    led.stop_animation()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global angle
    angle = min(180, angle + 5)
    pins.servo_write_pin(AnalogPin.P13, angle)
    led.stop_animation()
input.on_button_pressed(Button.B, on_button_pressed_b)

Distance = 0
angle = 0
angle = 90
pins.servo_write_pin(AnalogPin.P13, angle)

def on_forever():
    global Distance
    Distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    if Distance <= 2:
        pins.servo_write_pin(AnalogPin.P13, 70)
        basic.pause(200)
        pins.servo_write_pin(AnalogPin.P13, 90)
        basic.show_leds("""
            . # # # .
            # # # # #
            # # . # #
            # # # # #
            . # # # .
            """)
        basic.pause(200)
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            """)
        basic.pause(5000)
    else:
        pins.servo_write_pin(AnalogPin.P13, 90)
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
