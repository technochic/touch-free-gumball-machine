input.onButtonPressed(Button.A, function () {
    angle = Math.max(0, angle - 5)
    pins.servoWritePin(AnalogPin.P13, angle)
    led.stopAnimation()
})
input.onButtonPressed(Button.B, function () {
    angle = Math.min(180, angle + 5)
    pins.servoWritePin(AnalogPin.P13, angle)
    led.stopAnimation()
})
let Distance = 0
let angle = 0
angle = 90
pins.servoWritePin(AnalogPin.P13, angle)
basic.forever(function () {
    Distance = sonar.ping(
    DigitalPin.P0,
    DigitalPin.P1,
    PingUnit.Centimeters
    )
    if (Distance <= 2) {
        pins.servoWritePin(AnalogPin.P13, 70)
        basic.pause(200)
        pins.servoWritePin(AnalogPin.P13, 90)
        basic.showLeds(`
            . # # # .
            # # # # #
            # # . # #
            # # # # #
            . # # # .
            `)
        basic.pause(200)
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
        basic.pause(5000)
    } else {
        pins.servoWritePin(AnalogPin.P13, 90)
        basic.showIcon(IconNames.Happy)
    }
})
