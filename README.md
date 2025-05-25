## wake-up-tone-generator
A python script that keeps your sound device awake. Tested using the following device setup:
 - Logitech Z207
 - Stereo Mix (Realtek(R) Audio)

### Problem
Some sound devices may switch to sleep mode or something after several seconds of quiet sound. You have to keep your sound loud to maintain the awake mode, making it unable to listen to quiet music.

### Solution
The script emits a continuous 25 KHz sound, which is inaudible to the human ear, keeping the sound device awake. ChatGPT helped to create this script
