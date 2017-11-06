# Network diagnostic scripts

A handy script or two to watch network traffic, which can assist in working out what the controller *thinks* should be happening, particularly when it doesn't.

## mqttsub.py

Execute as:

    python mqttsub.py

Connects to the MQTT broker, subscribes to all channels, and outputs any message sent. You should see individual players announce themselves when they connect (which isn't terribly useful, as they can't also announce when they fall offline...), and messages to the topic `orchestra/playset` with the payload of a set of beat cues.