====


USAGE:
for i in 33 34 35 36 37 38 ; do ./gathering_nic_information.expect 192.168.33.$i admin helion123! ;sleep 1 ;done | grep Port1NIC

こうすると、NICの数がわかる
for i in 75 ; do ./gathering_nic_information.expect 192.168.33.$i admin helion123! ;sleep 1 ;done | grep NIC_MAC | wc -l
