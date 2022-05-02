# Laboratorio 1 Maggio 2022

## Cisco Packet Tracer

Laboratorio di introduzione su Cisco Packet Tracer.

Comandi del CLI visti

- HELP page &rarr lista dei comandi disponibili
```console
> ?
```

- Visualizzare le interfacce 
```console
> show interfaces
```

- Privilegi di root
```console
> enable
```

- Salvare la configurazione corrente allo startup
```console
# copy running-config startup-config
```

- Configurare il Router
```console
# configure terminal
```
```console
# conf t
```

- Cambiare il nome del Router
```console
# hostname <new_name>
```

- Visualizza configurazione corrente
```console
# show run
```
```console
# show running-config
```

- Riavvia Router
```console
> reload
```

- Visualizzare tabella di routing
```console
> show ip route
```

- Imposta password per root
```console
# enable secret <passw>
```

- Rimuovere password
```console
# no enable secret
```

- Configurare un'interfaccia
```console
# interface interface_name
```

- Accendere un interfaccia
```console
# no shutdown
```

- Configurare indirizzo IP
```console
# ip address <ip_address> <subnet_mask>
```

- Settare il clock dell'interfaccia
```console
# clock rate <frequency> 
```
