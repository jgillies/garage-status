from flask import Flask, render_template
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PIN = 15


def get_garage_door_state(pin):
    '''Returns the state of the garage door on the specified pin as a string

        Args:
            pin: GPIO pin number.
    '''
    if GPIO.input(PIN):  # pylint: disable=no-member
        state = 'open'
    else:
        state = 'closed'
    return state


app = Flask(__name__)


@app.route('/garage')
def garage():
    try:
        GPIO.setup(15, GPIO.IN)
        if GPIO.input(PIN):
            response = 'open'
        else:
            response = 'closed'
    except BaseException:
        response = 'unknown'

    return render_template('page.html', status=response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
