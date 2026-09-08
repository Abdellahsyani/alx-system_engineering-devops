# 0x07. Networking basics #0

Answer files for the theory questions (OSI model, network types, MAC vs. IP,
TCP vs. UDP) plus two Bash scripts that inspect the local network stack.

## Key files

| File | Contents |
| --- | --- |
| `0-OSI_model` | Answers: the OSI model is organised in layers and is a conceptual model |
| `1-types_of_network` | Answers about LAN / WAN / Internet scope |
| `2-MAC_and_IP_address` | Answers distinguishing hardware and logical addresses |
| `3-UDP_and_TCP` | Answers on reliability and connection semantics |
| `4-TCP_and_UDP_ports` | Lists listening TCP, UDP and Unix sockets with the owning program |
| `5-is_the_host_on_the_network` | Sends 5 ICMP echo requests to the IP passed as `$1` |

## Usage

```bash
sudo ./4-TCP_and_UDP_ports          # sudo shows program names for all sockets
./5-is_the_host_on_the_network 8.8.8.8
```

`5-is_the_host_on_the_network` prints a usage line when no argument is given.

## Notes

The answer files contain only the numeric choice per question — one per line.
`4-TCP_and_UDP_ports` relies on `netstat` (`net-tools`), which is not installed
by default on recent Ubuntu images; `ss -lntup` is the modern equivalent.
