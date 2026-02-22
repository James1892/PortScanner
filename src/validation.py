import ipaddress
from src.utils import colours

def portValidation(port):
    """
    The function converts the input to an integer and checks if it is within the valid range for port numbers.
    If the input is not a valid integer or is outside the valid range, it returns False.

    Parameters:
    - port (str or int): The port number to validate. It is expected to be a string that can be converted to an integer.

    Returns:
    - bool: True if the port is a valid integer else return an error message.
    """
    try:
        if int(port) in range(0, 65536):
            return True
        else:
            return f"{colours['errorRed']}[-]Invalid port{colours['default']}" 
    except ValueError:
        return "Invalid port - must be a number."

def hostValidation(host):
    """
    Validates if the provided string is a valid IPv4 address using the ipaddress library.

    Parameters:
    - host (str): The string of the host IP address to validate.

    Returns:
    - bool: True if the host is a valid IP address; otherwise, false.
    """
    try:
        ipaddress.IPv4Address(host)
        return True
    except ValueError:
        print(f"{colours['errorRed']}Error: Host {host} is not a valid IP address{colours['default']}")
        return False
