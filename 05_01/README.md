# Laboratorio 1 Maggio 2022

## Cisco Packet Tracer

Laboratorio di introduzione su Cisco Packet Tracer.

Comandi del CLI visti

- HELP page &rarr; lista dei comandi disponibili

      > ?

- Visualizzare le interfacce 

      > show interfaces

- Privilegi di root

      > enable

- Salvare la configurazione corrente allo startup

      # copy running-config startup-config

- Configurare il Router

      # configure terminal
      
  
      # conf t

- Cambiare il nome del Router

      # hostname <new_name>

- Visualizza configurazione corrente

      # show run
        
      # show running-config

- Riavvia Router

      > reload

- Visualizzare tabella di routing

      > show ip route

- Imposta password per root

      # enable secret <passw>

- Rimuovere password

      # no enable secret

- Configurare un'interfaccia

      # interface interface_name

- Accendere un interfaccia

      # no shutdown

- Configurare indirizzo IP

      # ip address <ip_address> <subnet_mask>

- Settare il clock dell'interfaccia

      # clock rate <frequency> 

- Settare una password per connessione in remoto (Console)
        
      # console line 0
      # password <passw>
      # login

- Impostare il Router per accesso remoto via ethernet

      # line vty 0 4
      # password <passw>
      # login
