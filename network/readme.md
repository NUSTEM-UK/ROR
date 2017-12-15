# Network diagnostic scripts

A handy script or two to watch network traffic, which can assist in working out what the controller *thinks* should be happening, particularly when it doesn't.

The various parts of the system are connected via MQTT messaging; these tools report what's happening via those channels, and allow direct interaction with the behind-the-scenes messaging.

## mqttsub.py

Connects to the MQTT broker, subscribes to all channels, and outputs any message sent. You should see individual players announce themselves when they connect (which isn't terribly useful, as they can't also announce when they fall offline...), and messages to the topic `orchestra/playset` with the payload of a set of beat cues.

At some point we should update this to clean UTF-8 text, the current output is a bit scrappy.

## mqtt-test.py

Fires commands across the network to test different behaviours. See internal comments for details.