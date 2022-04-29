music.play_melody("- - - B F A - - ", 120)
basic.show_leds("""
    # # # # .
        # . . . .
        # # # # .
        # . . . .
        # . . . .
""")
basic.show_leds("""
    # . . . #
        # . . . #
        # . . . #
        . # . # .
        . . # . .
""")
basic.show_leds("""
    . . # # .
        . # . . #
        # . . . .
        . # . . #
        . . # # .
""")
basic.show_leds("""
    . # . . #
        . # . # .
        . # # . .
        . # . # .
        . # . . #
""")

def on_forever():
    for index in range(4):
        pass
basic.forever(on_forever)
