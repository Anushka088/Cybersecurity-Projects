import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
    except Exception as e:
        print(f"Could not scan port {port}: {e}")

def scan_ports(host, start_port, end_port):
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda p: scan_port(host, p), range(start_port, end_port + 1))

if __name__ == "__main__":
    host = input("Enter the host to scan: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    scan_ports(host, start_port, end_port)