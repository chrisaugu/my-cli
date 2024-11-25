from paramiko import SSHClient, AutoAddPolicy

# router_ip = "127.0.0.15"
# router_username = "kitten"
# router_password = "secret"

ssh = SSHClient()

def run_command_on_device(ip_address, username, password, command):
    """ Connect to a device, run a command, and return the output."""

    # Load SSH host keys.
    ssh.load_system_host_keys()
    # Add SSH host key when missing.
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    
    total_attempts = 3
    for attempt in range(total_attempts):
        try:
            print("Attempt to connect: %s" % attempt)
            # Connect to router using username/password authentication.
            ssh.connect(ip_address, 
                        username=username, 
                        password=password,
                        look_for_keys=False )
            # Run command.
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            # Read output from command.
            output = ssh_stdout.readlines()
            # Close connection.
            ssh.close()
            return output

        except Exception as error_message:
            print("Unable to connect")
            print(error_message)


# Run function
# router_output = run_command_on_device(router_ip, router_username, router_password, "df -h")

# print(router_output)

# https://medium.com/featurepreneur/ssh-in-python-using-paramiko-e08fd8a039f7
# Analyze show ip route output
# Make sure we didn't receive empty output.
# if router_output != None:
#     for line in router_output:
#         if "/dev/sda2" in line:
#             print("Found default route:")
#             s = line.split('\n')
#             print(s)