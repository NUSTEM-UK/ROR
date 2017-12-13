# Channel correspondence

Piano Channel is (key - 1): on a standard piano keyboard, A440 is key 49: plays as 'channel 48' (ie. we're zero-ordinal here).

Pimoroni's code has a three-note offset

| Piano Channel | Note   | Octave | Hz    | MQTT Channel |
|---------------|--------|--------|-------|--------------|
| 36            | C      | 4      | 261.6 | 0            |
| 37            | C#     | 4      | 277.2 |              |
| 38            | D      | 4      | 293.7 | 1            |
| 39            | D#     | 4      | 311.1 |              |
| 40            | E      | 4      | 329.6 | 2            |
| 41            | F      | 4      | 349.2 | 3            |
| 42            | F#     | 4      | 370.0 |              |
| 43            | G      | 4      | 392.0 | 4            |
| 44            | G#     | 4      | 415.3 |              |
| 45            | A      | 4      | 440.0 | 5            |
| 46            | A#     | 4      | 466.2 |              |
| 47            | B      | 4      | 493.9 | 6            |
| 48            | C      | 5      | 523.2 | 7            |