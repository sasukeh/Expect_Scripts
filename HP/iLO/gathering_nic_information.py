#!/usr/bin/python
__author__ = 'sasukeh'

#
#  USAGE:
#    python gather__.py <ip_address> <User> <Pass>
#

import pexpect
import sys

#print sys.platform

# follow the USAGE
if len(sys.argv) < 4:
    print "USAGE:\n\t python gatherring_nic_information.py <ip_address> <User> <Pass>"
    exit(1)

HOST = sys.argv[1]
USER = sys.argv[2]
PASSWD = sys.argv[3]

print HOST
print USER
print PASSWD


COMMAND='ssh %s@%s' % (USER, HOST)
REMOTE_COMMAND="show system1/network1/Integrated_NICs"

print COMMAND

ilo = pexpect.spawn(COMMAND)
ilo.expect('.*ssword:',timeout=5)
ilo.sendline(PASSWD)
ilo.expect("</>hpiLO->")
ilo.sendline(REMOTE_COMMAND)
ilo.expect("</>hpiLO->")
ilo.sendline("quit")
print ilo.before

"""
REMOTE_COMMAND="show system1/"
USER="admin"
HOST=""
PASS="helion123!"
COMMAND="ssh  %s@%s %s" % (USER, HOST, REMOTE_COMMAND)
child = pexpect.spawn(COMMAND)
child.expect('password:')
child.sendline(PASS)
child.expect(pexpect.EOF)
print child.before
"""