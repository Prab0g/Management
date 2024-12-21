from time import sleep
from ipaddress import IPv4Address, IPv4Network
from rich.console import Console
from rich.traceback import install
install()

console = Console()

def update_configuration(user_values: dict) -> str:
    with open("configuration.txt", "r") as configuration_file:
        configuration = configuration_file.read()
    
    for placeholder, user_input in user_values.items():

       configuration = configuration.replace(f"<{placeholder}>", user_input)
    return configuration

def query_user(ip_address: IPv4Address, subnet_mask: str) -> dict:
    user_values = {}

    hostname = input("Enter the hostname: ")
    user_values["hostname"] = hostname

    interface = input(f"Enter the management interface for {hostname}: ")
    user_values["interface"] = interface

    user_values["ip address"] = str(ip_address)
    user_values["subnet mask"] = subnet_mask

    return user_values

if __name__ == "__main__":
    num_devices = int(input("Provide the number of devices (1 - 9): "))
    
    network = IPv4Network(input("Provide the network address (x.x.x.x/x): "))
    network_address, subnet_mask = network.with_netmask.split("/")
    
    sleep(0.2), print()

    for device_index in range(num_devices):
        console.print(f"=== [bold]Device Configuration[/] {device_index + 1} ===", style="underline blue")
        user_values = query_user(IPv4Address(network_address) + (device_index + 1), subnet_mask)

        updated_configuration = update_configuration(user_values)

        sleep(0.2), print()
        print(updated_configuration)
        sleep(0.2), print()