import wmi

ip = "148.147.175.217"
username = "admim"
password = "avaya"
from socket import *
try:
    print "Establishing connection to %s" %ip
    connection = wmi.WMI(ip, user=username, password=password)
    print "Connection established"
except wmi.x_wmi:
    print "Your Username and Password of "+getfqdn(ip)+" are wrong."
    
