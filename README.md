XInput to Home Assitant bridge
==============================

Use an XInput to expose some events to Home Assistant via webhook.

Setup:
---
1. Create Home Assistant automation (use `home_assistant_automation_example.yaml` as the example)
1. Run `pip install pyglet` 
1. Run `pip install requests` 
1. Copy `config.ini.example` to `config.ini`
	1. Update values in `config.ini`

Usage:
---
1. Connect XInput device
1. Run `python bridge.py`
1. Hold "Left Shoulder" and "Menu" buttons and press "Directional Pad Up" button - you should see a notification in Home Asssistant

Result:
---

![Notificatons in Home Assitant](home_assistant_notifications.png "Notificatons in Home Assitant")

Related video demo:
---
Adjusting TV volume without leaving the game - more details in the video description.

[![Video Demo Adjusting TV volume that uses this script](https://img.youtube.com/vi/1Z0PqS0FhlM/0.jpg)](https://www.youtube.com/watch?v=1Z0PqS0FhlM)