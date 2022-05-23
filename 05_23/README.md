# Laboratorio del 23 Maggio 2022

## Cisco Packet Tracer

### NAT

- Configurare NAT su un Router
        
        # conf-t
        # interface <interface_name>
        # ip nat inside

        # ip nat outside

- Creare lista di indirizzi per il NAT

        # conf-t
        # access-list <list_index> permit <ip_addr> <wildcard>
    
    `wildcard` è il reciproco della `subnet_mask`

- Associare NAT alla lista

        # conf-t
        # ip nat inside source list <list_index> interface <outside_interface_name> overload

### PORT FORWARDING



### DHCP