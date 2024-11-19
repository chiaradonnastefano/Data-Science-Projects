import socket
import re
import json
from typing import List, Tuple, Union

# Load port-to-service mapping from the JSON file
def load_ports_and_services() -> dict:
    try:
        with open('ports_and_services.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def get_open_ports(target: str, port_range: Tuple[int, int], verbose: bool = False) -> Union[List[int], str]:
    """
    Scans the specified range of ports on a target to check for open ports.

    :param target: The target IP or hostname to scan.
    :param port_range: A tuple specifying the range of ports (start_port, end_port).
    :param verbose: If True, provides additional details about the scan.
    :return: A list of open ports or an error message string.
    """
    open_ports = []
    ports_and_services = load_ports_and_services()  # Load port-to-service mapping

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        return "Error: Invalid hostname or IP address"
    except socket.error:
        return "Error: Unable to resolve target"

    # Scan ports
    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)

    # Verbose Output Preparation
    if verbose:
        try:
            host = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            host = None
        
        output = f"Open ports for {host or ip} ({ip})\n"
        output += "PORT     SERVICE\n"
        for port in open_ports:
            service = ports_and_services.get(str(port), "Unknown")  # Get service from JSON
            output += f"{port:<9}{service}\n"
        return output.strip()

    return open_ports
