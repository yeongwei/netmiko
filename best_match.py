from netmiko import SSHDetect

device = {
    "device_type":  "autodetect",
    "host":         "XX.XX.X.XXX",
    "username":     "Xxxxxxxxxxx",
    "password":     "XXXXXX",
    "secret":       "XXXXXX"
}

best_match = SSHDetect(**device).autodetect()

print(f"{best_match}")