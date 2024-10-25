from netmiko import ConnectHandler
from pprint import pprint

device_ip = "10.0.15.182"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "ip": device_ip,
    "username": username,
    "password": password,
}


def gigabit_status():
    ans = "show ip interface brief"
    with ConnectHandler(**device_params) as ssh:
        up = 0
        down = 0
        admin_down = 0
        
        result = ssh.send_command(ans, use_textfsm=True)
        
        interface_status = []
        
        for interface in result:
            interface_name = interface['intf']
            status = interface['status']
            
            interface_status.append(f"{interface_name} {status}")
            
            if status == "up":
                up += 1
            elif status == "down":
                down += 1
            elif status == "administratively down":
                admin_down += 1
        

        ans = ', '.join(interface_status) + f" -> {up} up, {down} down, {admin_down} administratively down"
        pprint(ans)
        return ans
