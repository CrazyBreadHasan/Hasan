import RPi.GPIO as GPIO

class RotaryEncoder:

    CLOCKWISE = 1
    ANTICLOCKWISE = 2
    BUTTONDOWN = 3
    BUTTONUP = 4

    rotary_a = 0
    rotary_b = 0
    rotary_c = 0
    last_state = 0
    direction = 0

    # Initialise rotary encoder object
    def __init__(self, pinA, pinB, button, callback):
        self.pinA = pinA
        self.pinB = pinB
        self.button = button
        self.callback = callback
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Add event detection to the GPIO inputs
        GPIO.add_event_detect(self.pinA, GPIO.BOTH, callback=self._switch_event_wrapper)
        GPIO.add_event_detect(self.pinB, GPIO.BOTH, callback=self._switch_event_wrapper)
        GPIO.add_event_detect(self.button, GPIO.BOTH, callback=self.button_event)

    # Wrapper for switch_event to handle instance method callback
    def _switch_event_wrapper(self, channel):
        self.switch_event(channel)

    # Call back routine called by switch events
    def switch_event(self, channel):
        if GPIO.input(self.pinA):
            self.rotary_a = 1
        else:
            self.rotary_a = 0

        if GPIO.input(self.pinB):
            self.rotary_b = 1
        else:
            self.rotary_b = 0

        # print(str(self.rotary_a) + str(self.rotary_b))
        self.rotary_c = self.rotary_a ^ self.rotary_b
        new_state = self.rotary_a * 4 + self.rotary_b * 2 + self.rotary_c * 1
        delta = (new_state - self.last_state) % 4
        self.last_state = new_state
        event = 0

        if delta == 1:
            if self.direction == self.CLOCKWISE:
                # print "Clockwise"
                event = self.CLOCKWISE
            else:
                self.direction = self.CLOCKWISE
        elif delta == 3:
            if self.direction == self.ANTICLOCKWISE:
                # print "Anticlockwise"
                event = self.ANTICLOCKWISE
            else:
                self.direction = self.ANTICLOCKWISE

        if event > 0:
            self.callback(event)

    def button_event(self, channel):
        if GPIO.input(channel):
            event = self.BUTTONUP
        else:
            event = self.BUTTONDOWN
            self.callback(event)

    def getSwitchState(self, switch):
        return GPIO.input(switch)