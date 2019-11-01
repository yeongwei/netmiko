from netmiko import SSHDetect, ConnectHandler

device = {
    "device_type":  "autodetect",
    "host":         "10.79.0.225",
    "username":     "Malaysia",
    "password":     "Cisco123"
}

best_match = SSHDetect(**device).autodetect()

print(f"Hello {best_match}!")

device["device_type"] = best_match
net_connect = ConnectHandler(**device)
prompt = net_connect.find_prompt()

print(f"prompt: {prompt}")

if prompt == None:
    raise Exception(f"{device}")

output = net_connect.send_command("show interface Fa0/0")
print(f"output: {output}")

