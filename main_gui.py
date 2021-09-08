#!/usr/bin/python3

import tkinter as tk
import subnet_calculator as sc

win = tk.Tk()
win.title("Subnet Calculator")
win.geometry("400x250")
'''
l_frame = tk.Frame(win)
l_frame.grid(row = 0, column = 0)
r_frame = tk.Frame(win)
r_frame.grid(row = 0, column = 1)
'''
# Variables
ip_addr = tk.StringVar(win)
sub_mask = tk.StringVar(win)
net_addr = tk.StringVar(win)
broad_addr = tk.StringVar(win)
hosts_count = tk.StringVar(win)
ip_range = tk.StringVar(win) 

# Function to calculate the values
def calculate():
    ip = ip_addr.get()
    mask = int(sub_mask.get())
    sub_mask.set(sc.get_subnet_mask(ip, mask))
    net_addr.set(sc.get_network_addr(ip, mask))
    broad_addr.set(sc.get_broadcast_addr(ip, mask))
    hosts_count.set(sc.get_available_hosts_count(ip, mask))
    ip_range.set(sc.get_ip_addr_range(ip, mask))


def clear():
    ip_addr.set("")
    sub_mask.set("")
    net_addr.set("")
    broad_addr.set("")
    hosts_count.set("")
    ip_range.set("")


tk.Label(win,text = "IP Address").grid(row=3,column=0)
fr_ip_addr = tk.Entry(win,textvariable=ip_addr)
fr_ip_addr.grid(row=3,column=1)

tk.Label(win,text = "Subnet Mask").grid(row=4,column=0)
fr_sub_mask = tk.Entry(win,textvariable=sub_mask)
fr_sub_mask.grid(row=4,column=1)

tk.Label(win,text = "Network Address").grid(row=5,column=0)
fr_net_addr = tk.Entry(win,textvariable=net_addr)
fr_net_addr.grid(row=5,column=1)

tk.Label(win,text = "Broadcast Address").grid(row=6,column=0)
fr_broad_addr = tk.Entry(win,textvariable=broad_addr)
fr_broad_addr.grid(row=6,column=1)

tk.Label(win,text = "Available Hosts").grid(row=7,column=0)
fr_hosts_count = tk.Entry(win,textvariable=hosts_count)
fr_hosts_count.grid(row=7,column=1)

tk.Label(win,text = "IP Range").grid(row=8,column=0)
fr_ip_range = tk.Entry(win,textvariable=ip_range)
fr_ip_range.grid(row=8,column=1)

tk.Button(win,text="Submit",command = calculate).grid(row=15,column=0)
tk.Button(win,text="Clear",command = clear).grid(row=15,column=1)

tk.Label(win,text = "IP Address format: 192.168.1.4").grid(row=20,column=0)
tk.Label(win,text = "Subnet Mask format: 21").grid(row=22,column=0)

win.mainloop()


