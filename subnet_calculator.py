#!/usr/bin/python3

def bin_string_to_ipv4(bin_str):
    new_str = ""
    for i in range(0,32,8):
        new_str = new_str + str(int(bin_str[i:i+8],2))
        if i != 24:
            new_str += "."
    return new_str

def get_binary_ip_submask_netwrk_brdcast(ip, sub_mask):
    ip_lst = ip.strip().split(".")
    bin_ip = "".join(["{:0>8b}".format(int(x)) for x in ip_lst])
    bin_sub_mask = "".join(['1' if i < sub_mask else '0' for i in range(32)])
    bin_net_addr = int(bin_ip,2) & int(bin_sub_mask,2)
    bin_net_addr = "{:0>32b}".format(int(bin_net_addr))
    bin_broad_addr = "".join([bin_net_addr[i] if i < sub_mask else '1' for i in range(32)])
    return bin_ip, bin_sub_mask, bin_net_addr, bin_broad_addr


def get_subnet_mask(ip,sub_mask):
    bin_sub_mask = "".join(['1' if i < sub_mask else '0' for i in range(32)])
    return bin_string_to_ipv4(bin_sub_mask)


def get_network_addr(ip, sub_mask):
    bin_ip, bin_sub_mask, bin_net_addr, bin_broad_addr = (get_binary_ip_submask_netwrk_brdcast(ip, sub_mask))
    net_addr = bin_string_to_ipv4(bin_net_addr)
    return net_addr


def get_broadcast_addr(ip, sub_mask):
    bin_ip, bin_sub_mask, bin_net_addr, bin_broad_addr = (get_binary_ip_submask_netwrk_brdcast(ip, sub_mask))
    bin_broad_addr = "".join([bin_net_addr[i] if i < sub_mask else '1' for i in range(32)])
    return bin_string_to_ipv4(bin_broad_addr)


def get_available_hosts_count(ip,sub_mask):
    hosts_count = 2**(32-sub_mask) - 2
    return hosts_count


def get_ip_addr_range(ip,sub_mask):
    bin_ip, bin_sub_mask, bin_net_addr, bin_broad_addr = (get_binary_ip_submask_netwrk_brdcast(ip, sub_mask))
    bin_ip_addr_start = "{:0>32b}".format(int(bin_net_addr,2) + int("1"))
    bin_ip_addr_end = "{:0>32b}".format(int(bin_broad_addr,2) - int("1"))
    ip_addr_range = f"{bin_string_to_ipv4(bin_ip_addr_start)} - {bin_string_to_ipv4(bin_ip_addr_end)}"
    return ip_addr_range


if __name__ == "__main__":

    ip = input("Enter ip: ")
    ip_lst = ip.strip().split(".")
    sub_mask = int(input("Enter subnet mask: "))
    print(f"IP address: {ip}")
    print(f"Subnet mask: {get_subnet_mask(ip, sub_mask)}")
    print(f"Network address: {get_network_addr(ip, sub_mask)}")
    print(f"Broadcast address: {get_broadcast_addr(ip, sub_mask)}")
    print(f"Available hosts: {get_available_hosts_count(ip, sub_mask)}")
    print(f"Ip address range: {get_ip_addr_range(ip, sub_mask)}")


'''
ip_lst = ip.strip().split()
bin_ip = "".join(["{:0>8b}".format(int(x)) for x in ip_lst])
bin_sub_mask = "".join(['1' if i < sub_mask else '0' for i in range(32)])
bin_net_addr = int(bin_ip,2) & int(bin_sub_mask,2)
bin_net_addr = "{:0>8b}".format(int(bin_net_addr))
bin_broad_addr = "".join([bin_net_addr[i] if i < sub_mask else '1' for i in range(32)])
net_addr = bin_string_to_ipv4(bin_net_addr)
hosts_count = 2**(32-sub_mask) - 2
bin_ip_addr_start = "{:0>8b}".format(int(bin_net_addr,2) + int("1"))
bin_ip_addr_end = "{:0>8b}".format(int(bin_broad_addr,2) - int("1"))
ip_addr_range = f"{bin_string_to_ipv4(bin_ip_addr_start)} - {bin_string_to_ipv4(bin_ip_addr_end)}"


if __name__ == "__main__"

    ip_lst = input("Enter ip: ").strip().split(".")
    sub_mask = int(input("Enter subnet mask: "))
    print(f"IP address: {bin_string_to_ipv4(bin_ip)}")
    print(f"Subnet mask: {bin_string_to_ipv4(bin_sub_mask)}")
    print(f"Network address: {net_addr}")
    print(f"Broadcast address: {bin_string_to_ipv4(bin_broad_addr)}")
    print(f"Available hosts: {hosts_count}")
    print(f"Ip address range: {ip_addr_range}")
'''


