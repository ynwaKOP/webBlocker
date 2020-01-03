# webBlocker

This is a python practise application -- Web Blocker

program background

The purpose is to design a pyhton program that could block certain distracting entertainment websites,
such as facebook, youtube. Because I do not want to distract by those websites during my study hours or working hour,
but sometimes people cannot stop visiting them. 

program details

use datetime to set up the working hours, and the program will automatically write www.facebook.com, facebook.com 
and any other desired websites into the system file look like below:

##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1	localhost
255.255.255.255	broadcasthost
::1             localhost
www.facebook.com
facebook.com


while we are not in working hours, it could defined as happy hours. 
The program will automatical remove the blocked websites.(The program actually delete everything in the system file and 
re-write it to the default as below).
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1	localhost
255.255.255.255	broadcasthost
::1             localhost

