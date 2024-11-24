import xinput
import configparser
import requests

chord_button_1_pressed = 0
chord_button_2_pressed = 0

def load_config():
	config = configparser.ConfigParser()
	config.read('config.ini')
	d = dict()
	d['home_assistant_url'] = config.get('General', 'home_assistant_url')
	d['webhook_id'] = config.get('General', 'webhook_id')
	d['chord_button_1'] = config.get('General', 'chord_button_1')
	d['chord_button_2'] = config.get('General', 'chord_button_2')

	return d

def sample_first_joystick(config):
    """
    Grab 1st available gamepad, logging changes to the screen.
    """
    joysticks = xinput.XInputJoystick.enumerate_devices()
    device_numbers = list(map(xinput.attrgetter('device_number'), joysticks))

    print('found %d devices: %s' % (len(joysticks), device_numbers))

    if not joysticks:
        xinput.sys.exit(0)

    j = joysticks[0]
    print('using %d' % j.device_number)

    battery = j.get_battery_information()
    print(battery)

    @j.event
    def on_button(button, pressed):
        global chord_button_1_pressed
        global chord_button_2_pressed

        base_url = config['home_assistant_url']+"/api/webhook/"+config['webhook_id']
        print('button', button, pressed)

        if button == int(config['chord_button_1']):
            chord_button_1_pressed = pressed
        if button == int(config['chord_button_2']):
            chord_button_2_pressed = pressed
        if chord_button_1_pressed and chord_button_2_pressed:
            if button != int(config['chord_button_1']) and button != int(config['chord_button_2']):
                print ("2 buttons down, something else pressed")
                print (requests.post(base_url, json={"button":button, "state":pressed}))

    while True:
        j.dispatch_events()
        xinput.time.sleep(.01)

if __name__ == "__main__":
	config = load_config()
	sample_first_joystick(config)