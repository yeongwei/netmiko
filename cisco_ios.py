from netmiko import SSHDetect, ConnectHandler
from datetime import datetime
import logging

device = {
    "device_type":  "autodetect",
    "host":         "XX.XX.X.XXX",
    "username":     "Xxxxxxxxxxx",
    "password":     "XXXXXX",
    "secret":       "XXXXXX"
}

now = datetime.now()
dte_string = now.strftime("%d.%m.%Y-%H.%M.%S")

logging.basicConfig(filename=f"log/cisco_ios_{dte_string}.log", level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())
logger = logging.getLogger("netmiko")

show_command = ""
config_commands = []

net_connect = ConnectHandler(**device)
prompt = net_connect.find_prompt()

logger.info(f"prompt: {prompt}")

logger.info(f"Switch into Enable Mode")
net_connect.enable()
enabled = net_connect.check_enable_mode()

logger.info(f"enabled: {enabled}")

logger.info(f"About to execute show_command")
if show_command == "":
    logger.info(f"show_command is empty")
else:
    logger.info(f"show_command: {show_command}")
    output = net_connect.send_command(show_command)
    logger.info(f"output: {output}")

print(f"About to execute config_commands")
if len(config_commands) == 0:
    logger.info(f"config_commands is empty")
else:
    logger.info(f"config_commands: {config_commands}")
    output = net_connect.send_config_set(config_commands)
    logger.info(f"output: {output}")
