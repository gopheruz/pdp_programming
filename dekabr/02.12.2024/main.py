import os
import platform

def block_website(website, redirect_ip="127.0.0.1"):
    # Path to the hosts file
    hosts_file = {
        "Windows": r"C:\Windows\System32\drivers\etc\hosts",
        "Linux": "/etc/hosts",
        "Darwin": "/etc/hosts"
    }.get(platform.system())

    if not hosts_file:
        print("Unsupported operating system!")
        return

    try:
        # Check if the script has administrator/root privileges
        if not os.access(hosts_file, os.W_OK):
            print("Run the script with administrator/root privileges.")
            return

        with open(hosts_file, "r+") as file:
            content = file.read()
            entry = f"{redirect_ip} {website}\n"
            if entry in content:
                print(f"{website} is already blocked.")
            else:
                file.write(entry)
                print(f"{website} has been blocked.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
block_website("chatgpt.com")
