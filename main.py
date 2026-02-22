from src.parser import createParser
from src.validation import hostValidation, portValidation
from src.utils import createBanner, output, logsToFile
from src.scanner import scanHost
from src.utils import colours

def main():
    """
    This function handles the command-line inputs for host and port specifications, with optional logging.
    Supports single or multiple hosts and individual, range, or list of ports. Scanning results can be logged.

    Steps:
    1. Parses command-line arguments for hosts, ports, and log file.
    2. Validates ports (individual, range, or list) and hosts (single or file-based list).
    3. Log the initial banner if a log file is specified.
    4. For file-based hosts, it reads, validates, and scans each. For single hosts, it validates and scans directly.
    """
    parser = createParser()
    args = parser.parse_args()
    ports = []
    banner = createBanner()
    print(banner)

    # Port parsing and validation
    try:
        target = args.TargetPort

        if "-" in target:
            start, end = map(int, target.split("-"))
            if start > end:
                raise ValueError()
            portList = range(start, end + 1)

        elif "," in target:
            portList = map(int, target.split(","))
        
        else:
            portList = [int(target)]

        for port in portList:
            if portValidation(port):
                ports.append(port)

    except ValueError:
        print(f"{colours['errorRed']}Error: Invalid port{colours['default']}")

    if args.LogFile:
        logsToFile(args.LogFile, banner)
    
    if args.TargetFile:
        with open(args.TargetFile, "r") as logFile:
            for lines in logFile:
                host = lines.strip()
                if hostValidation(host):
                    output(ports, host, args.TargetPort)
                    scanHost(host, ports, args, args.LogFile)
                    print("\n")
    
    if args.TargetHost:
        if hostValidation(args.TargetHost):
            output(ports, args.TargetHost, args.TargetPort)
            scanHost(args.TargetHost, ports, args, args.LogFile)

if __name__ == "__main__":
    main()
