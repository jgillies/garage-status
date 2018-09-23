from flask import Flask, render_template
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
PIN = 15


app = Flask(__name__)


@app.route('/garage')
def garage():
    try:
        GPIO.setup(PIN, GPIO.IN)
        if GPIO.input(PIN):
            response = 'open'
        else:
            response = 'closed'
    except BaseException:
        response = 'unknown'

    return render_template('page.html', status=response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
