# Cybersecurity-Projects

##**Beginner Level**
##1. Password Checker (password_checker.py)
   
   Typical checks include:
   1. Length: Passwords should be at least 8 characters long.
   2. Character Diversity:
      •	Lowercase letters
      •	Uppercase letters
      •	Numbers
      •	Special characters (e.g., @#$%)
   4. No Common Patterns: Avoid 1234, password, etc.
  
##2. Port Scanner (port_scanner.py)
   • Import Libraries: The script imports the necessary libraries: 'socket' for network connections and 'ThreadPoolExecutor' for concurrent execution.
   • scan_port Function: This function attempts to connect to a specific port on the given host. If the connection is successful (ie, the port is open), it prints a message indicating the port is open. Otherwise, 
     it prints that the port is closed. 
   • scan_ports Function: This function uses a 'ThreadPoolExecutor' to scan a range of ports concurrently. It maps the 'scan_port' function to each port in the specific range.
   • Main Block: The script prompts the user to enter the host, start port, and the end port, and then calls the 'scan_ports' function to perform the scan.
   
