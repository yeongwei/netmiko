from netmiko import SSHDetect, ConnectHandler
import logging

logging.basicConfig(filename="netmiko.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

device = {
    "device_type":  "autodetect",
    "host":         "10.79.0.225",
    "username":     "Malaysia",
    "password":     "Cisco123",
    "secret":       "Cisco123"
}

best_match = SSHDetect(**device).autodetect()

print(f"Hello {best_match}!")

device["device_type"] = best_match
net_connect = ConnectHandler(**device)
prompt = net_connect.find_prompt()

print(f"prompt: {prompt}")

# if prompt == None:
    # raise Exception(f"{device}")

# output = net_connect.send_command("show interfaces description")
# print(f"output: {output}")

print("Enable Mode")
net_connect.enable() # Works for Huawei too

# Not required to explicitly go into config mode
# print("Config mode")
# net_connect.config_mode()

print("About to configure Interface")
config_commands = [
    "interface Async0/0/0",
    "description Hello World!",
    "mtu 10000",
    "no shutdown"]

output = net_connect.send_config_set(config_commands)
print(f"output: {output}")
