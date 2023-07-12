# In this program, the `subnetting` function takes two parameters: `network` (a tuple representing the four digits of the network) 
# and `mask` (the network mask expressed in CIDR notation). The function converts the `network` and `mask` to binary strings and 
# performs a bitwise AND operation between them. The resulting binary string represents the subnet.

# The function then divides the binary string into four octets and converts them back to decimal format. Finally, it returns the `subnet`, 
# which is a list of the four subnet digits.

# In the example usage, we provide a sample network `(192, 168, 0, 100)` and a mask of `24`. The program then calls the `subnetting` 
# function and prints the resulting subnet.

# Please note that this is a basic implementation and doesn't handle all possible edge cases. It serves as a starting point for 
# understanding subnetting in Python.

def subnetting(network, mask):
    # Converting network and mask to binary strings
    network_binary = "{0:08b}.{1:08b}.{2:08b}.{3:08b}".format(*network)
    mask_binary = "1" * mask + "0" * (32 - mask)

    # Performing bitwise AND operation between network and mask
    subnet_binary = ""
    for i in range(32):
        if network_binary[i] == "1" and mask_binary[i] == "1":
            subnet_binary += "1"
        else:
            subnet_binary += "0"

    # Dividing the subnet into four octets
    subnet = []
    for i in range(0, 32, 8):
        octet = int(subnet_binary[i:i+8], 2)
        subnet.append(octet)

    return subnet

# Example usage
network = (192, 168, 0, 0)  # Network digits (e.g., IP address)
mask = 24                   # Network mask (e.g., CIDR notation)

# -----------------------------------------------------------------------------------------------------
# Subnetting is the process of dividing a larger network into smaller subnetworks, or subnets. 
# This can help improve network efficiency and security by allowing for better management of IP addresses 
# and controlling traffic flow between different parts of the network.

# To practice subnetting, here is a brief exercise:

# Assume you have been given the IP address block 192.168.0.0/24 and need to divide it into four equal subnets.

# 1. Start by determining how many bits are needed to create four subnets - in this case, two additional bits are needed (2^2 = 4).
# 2. Create a subnet mask by adding the two additional bits to the original mask - in this case, /26 (24 + 2 = 26).
# 3. Divide the original address space into four equal parts based on the new subnet mask:
# - Subnet 1: 192.168.0.0/26
# - Subnet 2: 192.168.0.64/26
# - Subnet 3: 192.168.0.128/26
# - Subnet 4: 192.168.0.192/26

subnet = subnetting(network, mask)
print(subnet)

from ipaddress import ip_network, IPv4Network
import math

def create_subnets(ip_block, subnet_mask, num_subnets):
    # Calculate the number of bits needed to create the desired number of subnets
    bits_needed = math.ceil(math.log2(num_subnets))
    
    # Calculate the new subnet mask by adding the bits needed to the original mask
    new_subnet_mask = subnet_mask + bits_needed
    
    # Convert the IP block to a network address and convert it to an integer
    network_address = int(IPv4Network(ip_block).network_address)
    
    subnets = []
    
    for i in range(num_subnets):
        # Calculate the size of each subnet based on the new subnet mask
        subnet_size = 2 ** (32 - new_subnet_mask)
        
        # Generate the network address for each subnet and append it to the list of subnets
        subnet_network = IPv4Network(network_address + (i * subnet_size), strict=False)
        subnets.append(subnet_network)
        
        # Print out the subnet information
        print(f"Subnet {i+1}: {subnet_network}/{new_subnet_mask}")
    
    return subnets

# Example usage, ie:192.168.0.0/24 :
create_subnets("192.168.0.0", 16, 300)