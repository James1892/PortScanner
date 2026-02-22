import socket
from src.utils import logsToFile, colours

def getServiceName(port):
    """
    Retrieves the service name associated with a given port using the socket library. If the service
    name for the port is not found; it returns unknown service.

    Parameters:
    - port (int): The port number for which to retrieve the service name.

    Returns:
    - str: The service name (e.g. 'http', 'ssh'), or a 'Unknown service' string if not found.
    """
    try: 
        return socket.getservbyport(port)
    except socket.error:
        return f"{colours['errorRed']}Unknown service{colours['default']}"


def grabBanner(sock, port):
    try:
        if port in (80, 8080, 8000):
            sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        else:
            sock.sendall(b"\r\n")

        banner = sock.recv(1024)
        return banner.decode(errors="ignore").strip().split("\n")[0]

    except socket.timeout:
        return "No banner (timeout)"
    except Exception:
        return "No banner"


def scanHost(host, ports, args, logFile=None):
    """
    Scans specified ports on a given host to check their status (open or closed) and the services running while grabbing the banner.
    Optionally, it logs the results to a specified file. Uses socket connections with a timeout to test port availability.

    Parameters:
    - host (str): The IP address of the target host to scan.
    - ports (list[int]): A list of port numbers to scan on the target host.
    - logFile (str, optional): The path to a file where scan results will be logged. If None, results are not logged.
    """
    results_lines = []

    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanSocket:
            scanSocket.settimeout(args.Timeout)
            result = scanSocket.connect_ex((host, port))
            service = getServiceName(port)

            if result == 0:
                status = "Open"
                banner = grabBanner(scanSocket, port)
                line = f"{port:<6}{status:<8}{service:<10}{banner}"
                results_lines.append(line)
                print(line)
            else:
                status = "Closed"
                line = f"{port:<6}{status:<8}{service:<10}"
                results_lines.append(line)
                if args.Verbose:
                    print(line)

    if logFile:
        block = f"\nScanned host: {host}\n"
        block += "Port  Status  Service       Banner\n"
        block += "-" * 60 + "\n"

        for line in results_lines:
            clean_line = line.replace("\t", "   ")
            block += clean_line + "\n"

        logsToFile(logFile, block)
