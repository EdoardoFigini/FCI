# Laboratorio del 23 Maggio 2022

## Cisco Packet Tracer

### NAT
`esercizio5.5.pkt`

- Configurare NAT su un Router
        
        # conf t
        # interface <inside_interface_name>
        # ip nat inside

        # interface <outside_interface_name>
        # ip nat outside

- Creare lista di indirizzi per il NAT

        # conf t
        # access-list <list_index> permit <ip_addr> <wildcard>
    
    `wildcard` è il reciproco della `subnet_mask`

- Associare NAT alla lista

        # conf t
        # ip nat inside source list <list_index> interface <outside_interface_name> overload

### PORT FORWARDING
`esercizio6.1.pkt`

- Associare staticamente esterno a interno

        # conf t
        # ip nat inside source static tcp <private_ip> <port> <public_ip> <public_port>

- Configurazione completa 

        > enable
        # conf t
        # interface <inside_interface_name>
        # ip nat inside
        # exit
        # interface <outside_interface_name>
        # ip nat outside
        # exit
        # access-list <list_index> permit <ip_addr> <wildcard>
        # ip nat inside source list <list_index> interface <outside_interface_name> overload
        # ip nat inside source static tcp <private_ip> <port> <public_ip> <public_port>

### DHCP