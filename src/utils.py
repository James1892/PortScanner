from datetime import datetime

colours = {
 "green": "\x1b[38;5;190m",
 "red": "\x1b[38;5;196m",
 "errorRed": "\x1b[1;31m",
 "default": "\x1b[0;0m"
}

def createBanner():
    from datetime import datetime

    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M")

    banner = f"""
=========================================
           PORT SCANNER
=========================================
    Started: {date} at {time}
=========================================
"""
    return banner

def output(ports, host, originalPort):
    """
    Prints the scanning target and port information for a host. It formats the output to include the host being scanned,
    the specified ports (either as a single port, a range, or a list), and a header for port scanning results.
    
    Parameters:
    - ports (list[int]): Scanned ports.
    - host (str): Target host's IP address.
    - originalPort (str): User-specified ports as a string (single, range '-', or list ',').
    """

    print(f"{colours['green']}Scanning target: {colours['default']}{host}")
    
    if "," in originalPort:
        port_display = ",".join(map(str, ports))
    else:
        port_display = originalPort
    
    print(f"{colours['green']}Ports: {colours['default']}{port_display}")
    print("-" * 60)
    print(f"{colours['red']}{'Port':<6}{'Status':<8}{'Service':<10}{'Banner'}{colours['default']}")

def logsToFile(logFile, contents):
    with open(logFile, "a") as file:
        file.write(f"{contents}\n")
