# Simple-Firewall

## Overview
This project demonstrates the creation of a simple firewall using Software-Defined Networking (SDN) with the OpenFlow protocol. The lab builds on foundational knowledge of Mininet and introduces key SDN concepts. The aim is to create a basic firewall that controls the flow of network traffic based on predefined rules using an OpenFlow-enabled switch.

## Scenario and Concept
In traditional networking, the data plane and control plane are tightly coupled, meaning that the same devices are responsible for forwarding traffic and making forwarding decisions. SDN decouples these planes, centralizing the control plane (the "brain" of the network) in a controller that dictates how traffic should flow through the network's data plane (the switches).

In this lab, you'll set up a network using Mininet and implement a simple firewall using the POX controller, an open-source SDN controller written in Python. The firewall rules are implemented within the controller, which sends commands to the switches to control the flow of traffic based on the protocol.

## Firewall Rules
The firewall in this lab is designed to allow specific types of traffic while blocking others:
- **Allow all ARP and TCP traffic**: These types of traffic are considered safe and necessary for network operations.
- **Drop all other traffic**: Any traffic that does not match the allowed ARP and TCP rules is dropped to minimize potential attack vectors.
This approach is a basic security measure, providing a layer of protection by limiting the network "surface" exposed to potential attackers.

## Implementation Details
- **Mininet Setup**: The provided Mininet script (lab3.py) configures a simple network topology that connects to a remote SDN controller.
- **POX Controller**: The core of the firewall logic is implemented in the lab3controller.py file. This script installs flow rules on the OpenFlow switches to enforce the firewall rules.
- **Flow Table Management**: The OpenFlow switch uses a flow table to determine how to handle incoming packets. The rules installed by the POX controller ensure that only ARP and TCP traffic are allowed, while all other traffic is dropped.

## Testing and Validation
To validate the firewall's functionality, the following tests are conducted:

- **Ping All** **(`pingall`)**: Verifies that ICMP traffic is blocked, as it should not be allowed through the firewall.
- **Flow Dump** **(`dpctl dump-flows`)**: Displays the flow entries in the switch to ensure the correct rules are installed.
- **Iperf**: Tests the network performance to ensure that TCP traffic can still flow freely despite the firewall rules.

# #Conclusion
This project gave me hands-on experience with SDN and OpenFlow, demonstrating how to create a simple but effective firewall. By the end, I can say with confidence I have a deeper understanding of how SDN can be leveraged to control network traffic and improve security in a networked environment.
