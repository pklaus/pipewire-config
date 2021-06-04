"""
The contexts to render the PipeWire alsa-monitor.conf template using https://github.com/pklaus/jinja2-render:

    jinja2-render default -f alsa-monitor.conf.jinja2 -o alsa-monitor.conf

"""

CONTEXTS = {
    "default": {
        "rename_devices": [
            {
                "id": "~^alsa_output.pci-0000_0d_00.4.analog-stereo$",
                "desc": "Headphones (Front-Audio)",
                "upd": ['audio.format = "S24_3LE"', "audio.rate = 192000"],
                # can it do 32bit float??? check aplay -D hw:1,0 -r 192000 -f FLOAT_LE ~/Desktop/file_example_WAV_2MG.wav
            },
            {
                "id": "~^alsa_input.pci-0000_0d_00.4.analog-stereo$",
                "desc": "Microphone (Front-Audio)",
                "upd": ['audio.format = "S24_3LE"', "audio.rate = 192000"],
            },
            {
                "id": "~^alsa_output.pci-0000_0d_00.4.iec958-stereo$",
                "desc": "n.c. (ALC1220 S/PDIF)",
            },
            {
                "id": "~^alsa_output.pci-0000_0a_00.1.hdmi-stereo-extra1$",
                "desc": "HDMI Ausgang",
            },
            {
                "id": "~^alsa_output.usb-Logitech_G935_Gaming_Headset-00.analog-stereo$",
                "desc": "Funkheadset (G935)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_input.usb-Logitech_G935_Gaming_Headset-00.mono-fallback$",
                "desc": "Funkmikro (G935)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.mono-fallback$",
                "desc": "Mini USB Microphone (CM108)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_input.usb-046d_Logitech_BRIO_BD59FA48-03.analog-stereo$",
                "desc": "Webcam (Logitech BRIO)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_input.usb-Samson_Technologies_Samson_Go_Mic_Direct-00.analog-stereo$",
                "desc": "Microphone (Samson Go Mic Direct)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_output.usb-Burr-Brown_from_TI_USB_Audio_CODEC-00.analog-stereo-output$",
                "desc": "Ausgang (Behringer UCA202)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_input.usb-Burr-Brown_from_TI_USB_Audio_CODEC-00.analog-stereo-input$",
                "desc": "Microphone (Behringer UCA202)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_output.usb-M-Audio_Transit_USB-00.analog-stereo$",
                "desc": "Headphones (M-Audio Transit USB)",
                "upd": ['audio.format = "S24_3LE"', "audio.rate = 96000"],
            },
            {
                "id": "~^alsa_input.usb-M-Audio_Transit_USB-00.analog-stereo$",
                "desc": "Microphone (M-Audio Transit USB)",
                "upd": ['audio.format = "S24_3LE"', "audio.rate = 96000"],
            },
            {
                "id": "~^alsa_output.usb-Generic_Sound_Blaster_Play__4_WWSB1860104004939B-00.analog-stereo$",
                "desc": "Headphones (SB P!4)",
                "upd": ['audio.format = "S24_3LE"', "audio.rate = 192000"],
            },
            {
                "id": "~^alsa_input.usb-Generic_Sound_Blaster_Play__4_WWSB1860104004939B-00.analog-stereo$",
                "desc": "Microphone (SB P!4)",
                "upd": ['audio.format = "S24_3LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_input.usb-Logitech_Logitech_G430_Gaming_Headset-00.mono-fallback$",
                "desc": "Microphone (G430)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_output.usb-Logitech_Logitech_G430_Gaming_Headset-00.analog-stereo$",
                "desc": "Headphones (G430)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_output.usb-0d8c_Generic_USB_Audio_Device-00.analog-stereo$",
                "desc": "Headphones (Generic Compact USB UP-100)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_input.usb-0d8c_Generic_USB_Audio_Device-00.mono-fallback$",
                "desc": "Microphone (Generic Compact USB UP-100)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
            {
                "id": "~^alsa_input.usb-MICE_MICROPHONE_USB_MICROPHONE_201308-00.mono-fallback$",
                "desc": "Microphone (Marantz MPM-2000)",
                "upd": ['audio.format = "S16_LE"', "audio.rate = 48000"],
            },
        ]
    }
}
