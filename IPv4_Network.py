>>> my_net.network_address
IPv4Address(u'10.220.192.192')
>>> my_net.broadcast_address
IPv4Address(u'10.220.192.199')

>>> my_net.hostmask
IPv4Address(u'0.0.0.7')
>>> my_net.netmask
IPv4Address(u'255.255.255.248')

>>> my_net.with_netmask
u'10.220.192.192/255.255.255.248'
>>> my_net.with_hostmask
u'10.220.192.192/0.0.0.7'

>>> my_net.with_prefixlen
u'10.220.192.192/29'
>>> my_net.prefixlen
29

>>> my_net.num_addresses
8
