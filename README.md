XInput to Home Assitant bridge
==============================

Use an XInput to expose some events to Home Assistant via webhook.

Setup:
1. Create Home Assistant automation (use `home_assistant_automation_example.yaml` as the example)
1. Run `pip install pyglet` 
1. Run `pip install requests` 
1. Copy `config.ini.example` to `config.ini`
	1. Update values in `config.ini`

Usage:
1. Connect XInput device
1. Run `python bridge.py`
1. Hold "Left Shoulder" and "Menu" buttons and press "Directional Pad Up" button - you should see a notification in Home Asssistant

Video demo:
<iframe width="315" height="560" src="https://www.youtube.com/shorts/1Z0PqS0FhlM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen ></iframe>