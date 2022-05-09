# Laboratorio del 9 Maggio 2022

## Cisco Packet Tracer

Routing Statico e protocolli di routing

- Riassunto (configurazione router)
  
      > enable
      # conf t
      # interface <interface_name>
      # ip address <ip_address> <subnet_mask>
      # no shutdown
      # exit
      # exit
      # copy running-config startup-config

- Configurare routing statico

      # ip route <dest_ip> <dest_subnet> <next_hop>

  Per configurare il routing statico bisogna specificare al router su che interfaccia (Next Hop) mandare i pacchetti destinati alla rete identificata da `dest_ip`   

- Configurare protocollo RIP
      
      # router rip

- Configurare versione di RIP

      # version <version>

- Configurare su quali reti abilitare RIP

      # network <ip_address>

- Mostrare configurazione

      # show ip protocols

- Impostare interfaccia passiva

      # passive-interface <interface_name>

  `interface_name` include sia il nome dell'interfaccia sia `porta/slot` (es. `FastEthernet0/1`)
