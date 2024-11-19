import port_scanner  # Custom module to scan ports
from unittest import main  # Used for running unit tests

# Function to test the port scanner functionality
def run_scanner():
    """
    Runs various test cases using the port scanner.
    Demonstrates scanning ports on URLs and IP addresses with and without verbose output.
    """
    # Scan ports on a URL (basic mode)
    ports = port_scanner.get_open_ports("www.freecodecamp.org", [75, 85])
    print("Open ports:", ports, "\n")

    # Scan ports on an IP address (basic mode)
    ports = port_scanner.get_open_ports("104.26.10.78", [8079, 8090])
    print("Open ports:", ports, "\n")

    # Scan ports on an IP address with verbose mode
    ports = port_scanner.get_open_ports("104.26.10.78", [440, 450], verbose=True)
    print(ports, "\n")

    # Scan ports on an IP address with verbose mode
    ports = port_scanner.get_open_ports("137.74.187.104", [440, 450], verbose=True)
    print(ports, "\n")

    # Scan ports on a hostname with verbose mode
    ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], verbose=True)
    print(ports, "\n")

# Main execution point
if __name__ == "__main__":
    # Run the test cases for the port scanner
    run_scanner()

    # Automatically run unit tests from test_module
    main(module="test_module", exit=False)
