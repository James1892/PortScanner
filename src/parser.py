import argparse

def createParser():
    """
    Initialises an argument parser for a port scanner, configuring mandatory and optional arguments.
    Users can specify a single target host or a file with multiple hosts, along with the required target ports.
    An optional log file argument is also available.

    Returns:
        argparse.ArgumentParser: Configured parser for command-line input.
    """
    parser = argparse.ArgumentParser(prog="Port Scanner",
                                    description="A basic Python port scanner.")
    
    group = parser.add_mutually_exclusive_group(required=True)
    optional = parser.add_argument_group("Optional")

    group.add_argument("-H", "--host",
                       dest="TargetHost",
                       help="Specify a single target IP address to scan.",
                       metavar="")
    
    group.add_argument("-t", "--targets",
                       dest="TargetFile",
                       help="Specify a file path that contains a list of target hosts (one per line) to be scanned.",
                       metavar="")
    
    parser.add_argument("-p", "--port",
                        required=True,
                        dest="TargetPort",
                        help="Specify the target port(s) for scanning. Accepts single ports (80), ranges (80-100), or comma-separated lists (22,80,443).",
                        metavar="")
    
    optional.add_argument("-L", "--log",
                          dest="LogFile",
                          help="Specify the file path for logging the scan results. If the file does not exist, it will be created.",
                          metavar="")
 
    optional.add_argument("-v", "--verbose",
                          dest="Verbose",
                          action="store_true",
                          default=False,
                          help="Show closed ports in addition to open ones.")

    optional.add_argument("--timeout",
                          dest="Timeout",
                          type=int,
                          default=4,
                          help="Set a timeout between scanned ports. (default: 4)",
                          metavar="")

    return parser
