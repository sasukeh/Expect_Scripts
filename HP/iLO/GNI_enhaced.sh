#!/bin/bash
#
#  ip aadress list should be in list.csv
#    1.1.1.1
#    2.2.2.2
#    3.3.3.3
#

oldifs=$ifs
ifs=,
[ ! -f $input ] && { echo "$input file not found"; exit 99;}

if [ $# -ne 3 ];then
  echo "Usage: scriptname listfile username password"
  exit 1
fi

input=$1
user=$2
password=$3

while read line
do
eval $(echo "$line" | awk -F';' '{print "ip="$1}')
echo $ip
echo $password
/usr/bin/expect - << EndMark
set timeout 20
set prompt "*</>hpiLO->"

spawn ssh "$user\@$ip" show system1/network1/Integrated_NICs 

expect "(yes/no)" {send "yes\r"}

expect "password:"
send "$password\r";

expect eof

EndMark

done < $input

