'Bitcoin Mining Dictionary' 
import tkinter as tk
from tkinter import ttk


BitcoinTerminology = {
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "host":"Host - A host is any device on a network that can send and receive data, typically having a unique IP address. This term can refer to both clients and servers because any device that participates in a network (and is capable of communication) is considered a host. In other words, host is a broader term that encompasses both the client and server roles, as well as other network device.",
    "Server": "Server - A server is a device, software, or system that provides services, data, or resources to clients over a network. Servers listen for client requests and respond accordingly, often serving multiple clients simultaneously. A server can be a dedicated piece of hardware or a software application that performs specific tasks, such as web hosting, file sharing, or database management.",
    "client":"A client is a device, software, or system that initiates communication with a server to request services, data, or resources. Clients rely on servers to fulfill their requests and typically interact with servers over a network. In many cases, clients are end-user devices like computers, smartphones, or applications such as web browsers, email clients, or file-sharing applications",
    "malgo":"Mining Algorithm - A mining algorithm refers to the specific set of rules and procedures that a blockchain network (like Bitcoin) uses to validate and secure transactions. These algorithms typically rely on a form of proof of work, where miners solve complex mathematical problems to add new blocks to the blockchain. Examples of mining algorithms include.",
    "hash":"A hash is the result or output produced by a hash function. It’s a unique string of characters that represents the data. In mining, the goal is to find a specific hash that meets the requirements of the mining algorithm, often referred to as a target. Miners continuously change the data slightly (called nonce) to generate different hashes until they find one that meets the criteria set by the network.",
    "telnet":"telnet- Used to communicate with a remote device or system using the Telnet protocol. Useful for testing open ports.",
    "getmac":"getmac - Retrieves the media access control (MAC) address and list of network protocols associated with each address for all network adapters.",
    "arp":"arp - Displays and modifies entries in the Address Resolution Protocol (ARP) cache, which contains IP addresses and their resolved Ethernet or physical addresses.",
    "netstat":"netstat - Displays active TCP connections, ports on which the computer is listening, Ethernet statistics, and the IP routing table.",
    "nslookup":"nslookup - Queries the Domain Name System (DNS) to obtain domain name or IP address mapping.",
    "tracert":"tracert - Determines the route taken to a destination by sending ICMP echo requests to each hop along the way.",
    "ping":"ping tests the reachability of a host on an IP network and measures the round-trip time for messages sent.",
    "ipconfig":"ipconfig - Displays all current TCP/IP network configuration values and refreshes DHCP and DNS settings.",
    "51%":"51% Attack: A scenario where a miner or group of miners controls more than 50 percent of the network's hash rate, potentially allowing them to manipulate the blockchain by reversing transactions or double-spending",
    "ecdsa":"Elliptic Curve Digital Signature Algorithm (ECDSA): A cryptographic algorithm used in Bitcoin for creating digital signatures. It ensures authenticity and non-repudiation of transactions",
    "cryptographic hash functions":"Cryptographic Hash Function: A mathematical algorithm that transforms input data into a fixed-size string of bytes. It is deterministic, one-way, and collision-resistant, properties essential for blockchain security",
    "halving":"Block Reward Halving: The periodic reduction of the block reward by 50%, which occurs approximately every 210,000 blocks (about every 4 years). This mechanism controls the issuance rate of new bitcoins",
    "p2p":"Peer-to-Peer (P2P) Network - A decentralized communications model where each node has equivalent capabilities and responsibilities. Bitcoin operates on a P2P network for transaction and block propagation",
    "DLT":"Distributed Ledger Technology (DLT) - A decentralized database managed by multiple participants across multiple nodes. Bitcoin's blockchain is a type of DLT",
    "bft":"Byzantine Fault Tolerance (BFT) - The ability of a distributed network to reach consensus despite the presence of malicious actors or faulty nodes. Bitcoin's PoW consensus mechanism provides probabilistic BFT",
    "merkle":"Merkle Tree - A data structure used to efficiently summarize and verify the integrity of large sets of data. In Bitcoin, Merkle trees are used to summarize all transactions in a block",
    "stratum":"Stratum Protocol - A client-server protocol used in mining pools that enables efficient transmission of mining jobs and submission of results, reducing network overhead and latency.",
    "bpd":"Block Propagation Delay - The time it takes for a newly mined block to be transmitted and validated across the network. Minimizing propagation delay is crucial for reducing orphaned blocks and maintaining network efficiency",
    "fpga":"Field-Programmable Gate Array (FPGA): Integrated circuits that can be reprogrammed after manufacturing to perform specific tasks. FPGAs were used in early Bitcoin mining but have been largely supplanted by ASICs due to efficiency constraints",
    "nonce":"Nonce: An arbitrary number used only once in cryptographic communication. In Bitcoin mining, miners increment the nonce value to find a hash output below the target difficulty threshold",
    "difficulty":"Mining Difficulty - A parameter that adjusts the complexity of the PoW puzzle to maintain a consistent block generation time (approximately every 10 minutes for Bitcoin). It adjusts every 2016 blocks based on total network hash rate",
    "pow":"Proof of Work (PoW): A consensus mechanism that requires miners to perform computational work to propose new blocks. It secures the network by making it computationally expensive to manipulate the blockchain",
    "sha-256":"SHA-256 Hashing Algorithm - A cryptographic hash function used in Bitcoin's Proof-of-Work (PoW) algorithm. Miners repeatedly compute SHA-256 hashes to solve computational puzzles and validate new blocks.",
    "gpu":"GPU (Graphics Processing Unit) is a specialized processor designed to accelerate the rendering of images, videos, and animations by performing parallel processing tasks, commonly used in both graphical applications and general-purpose computing tasks such as AI and data processing.",
    "cooling":"Cooling (e.g., Fans or Heatsinks) - Devices that prevent overheating by dissipating heat generated by the CPU and other components",
    "uefi":"Unified Extensible Firmware Interface - also known as BIOS(Basic Input/Output System), Firmware that initializes hardware during POST and loads the operating system.",
    "ram":"RAM (Random Access Memory) - Volatile memory that stores data and instructions for the CPU to access while the server is running.",
    "motherboard":"Motherboard (control board) - The main circuit board of the server that connects and allows communication between all components",
    "cpu":"CPU (Central Processing Unit) - The server's processor that executes instructions and performs computations.",
    "route":"route - Displays or modifies the routing table, showing the paths network traffic takes to reach other networks.",
    "nmap":"nmap - Scans networks to discover hosts, services, and security vulnerabilities.",
    "tcpdump":"tcpdump - Captures and analyzes network traffic at a packet level.",
    "dig":"dig - Performs DNS lookups to retrieve detailed information about domain names and DNS records",
    "arp!":"arp - Displays and modifies the Address Resolution Protocol (ARP) table, which maps IP addresses to MAC addresses",
    "nslookup":"nslookup - Queries DNS servers to obtain domain name or IP address information.",
    "xconfig":"ipconfig (Windows) / ifconfig (Linux/Unix) - Displays the current network configuration of a device, including IP addresses and network interfaces",
    "netstat":"netstat - Shows active network connections, listening ports, and network protocol statistics.",
    "tracex":"traceroute (Linux) / tracert (Windows) - Displays the path packets take to reach a network host, identifying each hop along the route",
    "ping":"ping - Sends ICMP echo requests to a host to check network connectivity and measure response time.",
    "watt":"A watt (W) is the unit of power in the International System of Units (SI), defined as the rate at which energy is transferred or used. One watt is equivalent to one joule of energy per second, and it is used to measure the power of electrical devices, light sources, engines, and other systems that consume or generate energy",
    "nm":"Nanometers (nm): Used to measure the wavelength of light in optical fibers, with common transmission windows around 850 nm, 1310 nm, and 1550 nm for multi-mode and single-mode fibers",            
    "BER":"Bit Error Rate (BER): A unitless measurement that describes the number of errors in the transmitted data, providing insight into the link's overall quality.",
    "latency":"Latency (ms): Measured in milliseconds, latency refers to the delay in transmitting data across a network link, important for detecting performance issues",
    "linkspeed":"Link Speed (Mbps, Gbps): The rate at which data is transmitted across the link, typically measured in megabits per second (Mbps) or gigabits per second (Gbps)",
    "attenuator":"Attenuators: Devices used to reduce the power of an optical signal to prevent overloading sensitive equipment at the receiving end",
    "dbm":"dBm refers to decibels relative to 1 milliwatt of optical power, commonly used to measure the absolute power in a fiber optic linkSo, while light energy itself isn’t directly measured in decibels, decibels are used to describe signal strength or loss in fiber optic communications based on the power levels of the light signal.",
    "splice":"Fiber Splices - The process of joining two fiber optic cables end-to-end, either through mechanical means or fusion, to ensure a continuous data path.",
    "Patch Panels": "Hardware components used to organize and connect multiple fiber optic or copper cables within a network, providing easy access and management of connections",
    "transceivers":"Transceivers (SFP/SFP+/QSFP): Small, pluggable modules that convert electrical signals to optical signals (and vice versa) for data transmission over fiber optic or copper networks.",
    "fiber":"Fiber Optic Cable - A cable that transmits data as light pulses through glass or plastic fibers, offering high-speed and long-distance communication",
    "packet":"Packets are transmitted across networks through a process called packet switching, where data is broken into small chunks (packets) and sent individually across the network. Each packet includes the destination address and follows the most efficient path, potentially through multiple routers and switches, before being reassembled into the original data at the destination. The transmission process includes error-checking and acknowledgment to ensure all packets arrive correctly",
    "vlan":"VLAN (Virtual Local Area Network) is used to logically segment a physical network into separate, isolated sub-networks to improve security and manageability within the same infrastructure",
    "vpn":"VPN (Virtual Private Network) is used to securely connect remote devices to a private network over the internet, ensuring encrypted data transmission.",
    "mesh":"Mesh Network - A mesh network is a type of network topology where each node (device) connects directly to multiple other nodes, allowing for data to be transmitted along the most efficient path. If one node fails, the network can automatically reroute data using the remaining nodes, making mesh networks highly reliable and resilient, especially for large areas or where wired infrastructure is difficult",
    "man":"MAN (Metropolitan Area Network) - A MAN is a network that covers a larger geographic area than a LAN but smaller than a WAN, typically used to connect multiple networks across a city or metropolitan region.",
    "lan":"LAN (Local Area Network) - A LAN is a network that connects computers and devices within a small, localized area such as a home, office, or building, allowing for data sharing and communication",
    "wan":"WAN (Wide Area Network) - A WAN is a network that spans a large geographic area, such as a city, country, or even globally, connecting multiple smaller networks like LANs for long-distance communication.",
    "lilo":"LILO (Linux Loader) is a simpler bootloader that requires manual updates after configuration changes and lacks the flexibility and troubleshooting features of GRUB",
    "grub":"GRUB (GRand Unified Bootloader) is a powerful bootloader that supports multiple operating systems, offers dynamic configuration, and includes an interactive command-line interface for troubleshooting",
    "pxe":"Preboot Execution Environment Server - is a network service that enables computers to boot and load an operating system remotely over a network, without requiring a local hard drive or operating system, typically used for network-based OS installations and system imaging",
    "static":"Static IP - is a manually assigned, fixed IP address given to a device, ensuring its consistent identification on a network.",
    "dhcp":"Dynamic Host Configuration Protocol - automatically assigns IP addresses to devices on a network, ensuring efficient and temporary use of available IPs",
    "otdr":"Optical Time Domain Reflectometers - OTDRs are advanced tools that use a pulse of light to measure the distance and characteristics of the fiber optic cable. They provide a graphical representation of the fiber’s behavior, helping to identify faults, breaks, or other issues",
    "vfl":"visual fault locator - VFL will detect optical signals and locate faults in the fiber optic cable. This handheld device emits a low-level laser beam that illuminates the fiber, making it visible to the naked eye",
    "ack":"ACK (Acknowledge) - Finally, the initiating device (client) responds with a TCP segment with the ACK flag set, acknowledging the server’s SYN segment by incrementing the server’s sequence number by 1. At this point, both devices have agreed on the sequence numbers, and the connection is fully established, allowing data transmission to begin",
    "synack":"SYN-ACK (Synchronize-Acknowledge) - The receiving device (server) responds with a TCP segment that has both the SYN and ACK (acknowledge) flags set. The SYN flag signals the server's sequence number, while the ACK flag acknowledges the client’s SYN by incrementing the client’s sequence number by 1. This step confirms that the server has received the client’s request to establish a connection",
    "syn":"SYN (Synchronize) - The initiating device (client) sends a TCP segment with the SYN (synchronize) flag set to the receiving device (server). This message contains the client’s initial sequence number, used to synchronize the sequence numbers for data transmission",
    "minaj":"TCP 3-way handshake is a process used to establish a reliable connection between two devices (client and server) in a Transmission Control Protocol (TCP) network",                                                            
    "ssd":"Solid State Drive - (SSD) is a storage device that uses flash memory to store data electronically, offering faster performance and no moving parts",
    "hdd":"Hard Disk Drive - A Hard Disk Drive (HDD) is a traditional storage device that uses spinning magnetic disks to read and write data mechanically",
    "e2e":"End-to-End Testing -  This involves using a light source and a power meter at both ends of the cable to verify the integrity of the fiber and ensure minimal loss",
    "fiber":"A fiber optic cable is a high-speed data transmission medium that uses strands of glass or plastic fibers to transmit information as light pulses over long distances with minimal signal loss",
    "mmfiber":"Multi-Mode Fiber uses a larger core (about 50-62.5 microns) to transmit multiple light paths, which is more suitable for shorter distances with lower bandwidth",
    "smfiber":"Single Mode Fiber uses a small core (about 9 microns) to transmit light in a single path, ideal for long-distance, high-bandwidth data transmission.",
    "mbr":"Master Boot Record (MBR) is located in the first sector of a storage device, such as a hard drive or SSD, specifically at sector 0. It contains the bootloader and partition table, which are essential for starting the boot process and managing partitions on the drive.",
    "boot":"Boot refers to the sequence in which the system loads the operating system after the POST is successfully completed, starting the computer for use.",
    "POST":"POST (Power-On Self-Test) is a diagnostic process performed by the BIOS when a computer is powered on to check the hardware components and ensure they are functioning properly before booting",
    "south":"Southbridge - The Southbridge is responsible for managing lower-speed peripheral interfaces such as USB, SATA, and audio, serving as a bridge between the CPU and these slower devices.",
    "north":"Northbirdge - The Northbridge is a chipset in a computer's motherboard that connects the CPU to high-speed components like the RAM, graphics card (via PCIe), and often manages communication with the Southbridge.",
    "bios":" BIOS (Basic Input/Output System) - also known as Unified Extensible Firmware Interface, is a program that initializes and tests hardware components during the startup process of a computer and loads the operating system. The BIOS is a type of firmware, as it is permanently programmed into the computer's motherboard to control essential hardware functions",
    "dns":"Domain Name Service - is a system that translates human-readable domain names (like bitcoinversus.tech) into machine-readable IP addresses, enabling web browsers to locate and access websites",
    "hub":"Hub - a basic network device that connects multiple devices to a single network, primarily forwarding data to a central server without managing communication between devices on the same network.",
    "switch":"Switch- a device that enables communication between multiple devices within a Local Area Network (LAN), efficiently managing data traffic between them",
    "router":"Router - A device that serves as the central hub for managing connections between devices on a LAN and external networks, such as the internet, directing data traffic between them.",
    "url":"URL - The mining pool URL is the address that directs your Bitcoin miner to connect and contribute its hashing power to the pool. The mining pool URL typically follows the format stratum+tcp://<pool_address>:<port_number>.",
    "port":"Port Number - The port number specifies the entry point for communication between your Bitcoin miner and the mining pool server, commonly used to select the difficulty level or encryption method.",
    "rsi":"Relative Strength Index - The Relative Strength Index (RSI) is a momentum oscillator used in technical analysis to measure the speed and change of Bitcoin's price movements, indicating overbought or oversold conditions based on its recent trading performance",
    "hydrocool": "hydrocooling - a form of cooling for bitcoin mining machines that involves circulating water or a water-based coolant through a closed system to absorb and remove heat from the hardware, enabling efficient temperature regulation and enhanced performance",
    "immersion":"immersion coooling - involves submerging mining hardware in a thermally conductive but electrically insulating liquid to efficiently dissipate heat, enabling higher performance and energy efficiency compared to traditional air cooling methods. Man use dielectric fluids such as mineral oil or biodegradable oil",
    "motor":"An electromagnetic induction motor for exhaust fans in air-cooled Bitcoin mining operations is a device that converts electrical energy into mechanical energy to drive the fan, using the principle of electromagnetic induction to create rotational motion that efficiently expels heat from the mining environment",
    "hfuel": "Hydrogen fuel cells generate electricity by combining hydrogen and oxygen in an electrochemical process, producing water as the only byproduct ",
    "wave" : "Wave energy - converts the up-and-down motion of ocean waves into electricity through specialized devices that capture and transfer the energy",
    "tidal": "Tidal energy - generates electricity by capturing the kinetic energy of moving water caused by tides and ocean currents to turn turbines",
    "biomass" : "Biomass energy is produced by burning organic materials, such as wood, crop waste, or animal waste, to generate heat and electricity",
    "multi":" multimeter - a versatile tool for measuring voltage, current, and resistance. Bitcoin mining engineers use this tool to trouble shoot different electrical problems",
    "wind" : "Wind energy - produced by using wind turbines to convert the kinetic energy of wind into electrical power",
    "sol" : "Solar energy - harnesses sunlight through photovoltaic cells or solar thermal systems to generate electricity directly from the sun's rays.",
    "hydro" : "Hydropower - generates electricity by using the flow of water, typically from dams, to turn turbines that produce electrical power",
    "nuke": "Nuclear Energy - Nuclear energy is produced by splitting atoms of uranium or other heavy elements in a controlled reaction, releasing heat to generate electricity.",
    "fossil" : "Fossil Fuels (Coal, Oil, Natural Gas): Fossil fuels are energy sources formed from the remains of ancient organisms that are burned to generate electricity, releasing carbon dioxide as a byproduct",
    "peakoff" : "Peak off times are periods of lower electricity demand and cheaper energy, usually during late evenings and early mornings ",
    "peakon" : "Peak on - Peak on times are periods of high electricity demand and costs, typically during business hours.",
    "lfl" : "Large flexible loads - the ability of mining operations to adjust their energy consumption in response to grid demands, often by ramping down during peak times or increasing usage when there is excess power available. This flexibility allows miners to participate in demand response programs, stabilizing the grid while optimizing their energy costs",
   "psu": "Power Supply Unit - a critical hardware component that converts electrical power into a form usable by the computer's internal components.",
    "hb": "Hashboard - are specialized circuit boards used in Bitcoin mining machines, particularly in ASIC miners.",
    "cb": "Control Board - The control board acts as the communication bridge between the miner's hashboards and the external network (e.g., mining pool, internet).",
    "th/s": "Terrahash per second - a unit of measurement used to describe the computational power or hash rate of a Bitcoin mining machine or network.",
    "$/kwh": "Cost per Kilowatt-Hour - the amount of money charged for consuming one kilowatt-hour of electrical energy, (ex. $0.10/kWh). Used to calculate the cost of electricity usage over time.",
    "ip": "IP Address - a unique numerical identifier assigned to each device connected to a computer network that uses the Internet Protocol for communication.",
    "sn": "Serial Number - a unique identifier assigned to a specific item, device, or product by the manufacturer.",
    "mac": "Media Access Control Address - a unique identifier assigned to network interfaces for communication on the physical network segment.",
    "it": "Information Technology - a set of related fields that encompass computer systems, software, programming languages, and data and information processing, and storage.",
    "api": "Application Programming Interface - a set of rules, protocols, and tools that enables software applications to communicate with each other, exchange data, and share functionality.",
    "firm": "Firmware - is a specialized software program embedded in hardware devices that provides low-level control and operates the device's functions.",
    "asic": "Application-Specific Integrated Circuit - A custom-designed microchip optimized for a specific task. Performs specialized computations(i.e. a hash).",
    "hash$":"Hashprice - The hashprice metric is a financial measure used in the cryptocurrency mining industry to evaluate the daily revenue a miner can generate per unit of hash rate, typically expressed in dollars per terahash per day ($TH/day)",
    "pool" : "Mining pool - a collective group of miners who combine their computational resources over a network to increase their chances of successfully mining a block and earning Bitcoin rewards.",
    "form": "Transformer - An electrical device that transfers energy between two or more circuits through electromagnetic induction, used in Bitcoin mining to step up or step down voltage levels according to the power requirements of the mining hardware.",
    "gear": "Switchgear - An assembly of electrical disconnect switches, fuses, or circuit breakers used to control, protect, and isolate electrical equipment in a Bitcoin mining operation to enhance safety and manage load distribution",
    "pdu" : "Power Distrubution Unit - A device that distributes electrical power to various components or systems within a Bitcoin mining setup, typically from a single source to multiple mining rigs",
    "disk" : "Disk Management (in the context of downloading and putting firmware to a new Bitcoin machine) – The process of preparing, configuring, and maintaining the storage system on a Bitcoin mining device, which includes downloading the appropriate firmware and installing it to ensure the machine operates with the latest updates and optimal settings",
    "ui" : "User Interface - also known as Graphical User Interface (GUI) A visual part of a computer application or operating system through which a user interacts with a computer or software using graphical icons, visual indicators, and text.",
    "gen": "Genesis Block - The first block of the Bitcoin blockchain, created by Bitcoin's pseudonymous founder, Satoshi Nakamoto, on January 3, 2009. This foundational block, also known as Block 0, contains a special embedded message and serves as the starting point of the Bitcoin network. The 50 BTC reward from the Genesis Block is unspendable due to its unique construction",
    "air": "Air Cooling - A method of cooling Bitcoin mining equipment by using fans or blowers to circulate air across the hardware, dissipating heat generated by the mining process. This is the most common and traditional cooling method, relying on airflow to maintain optimal operating temperatures for mining rigs",
    "3p" : "3 Phase Electricity - Three-phase electricity is a type of electrical power distribution that uses three alternating currents, each phase offset by one-third of the cycle to provide a continuous flow of energy",
    "1p" : "Single Phase Electricity - One-phase electricity, or single-phase power, involves a single alternating current that delivers electric power in a unidirectional flow, typically used in residential properties.",
    "satoshi": "Satoshi Nakamoto - the pseudonymous person or group who developed Bitcoin, authored its original white paper, and designed and launched the first version of the Bitcoin software",
    "sat": "Sat - A satoshi, often abbreviated as sat, is the smallest unit of the Bitcoin cryptocurrency, named after its creator, Satoshi Nakamoto. One satoshi is equal to one hundred millionth of a single Bitcoin, or 0.00000001 BTC",
    "acdc": "Alternating Current to Direct Current - In a Bitcoin mining PSU, alternating current (AC) from the power grid is converted to direct current (DC) to supply the stable and continuous power required by the mining hardware. This conversion is essential because the mining machines' components, like ASIC chips, operate on DC power for efficient and consistent performance",
    "heatdiss": "Heat Dissipation - Heat dissipation from the exhaust at air-cooled Bitcoin mining facilities involves releasing the excess heat generated by mining hardware into the environment. Various methods to utilize this heat include redirecting it for residential or industrial heating, greenhouse farming, or even in sustainable energy projects to improve overall energy efficiency",
    "ppa": "Power Purchase Agreement - an arrangement in which a third-party developer installs, owns, and operates an energy system on a customer’s property. The customer then purchases the system's electric output for a predetermined period. A PPA allows the customer to receive stable and often low-cost electricity with no upfront cost, while also enabling the owner of the system to take advantage of tax credits and receive income from the sale of electricity. Though most commonly used for renewable energy systems, PPAs can also be applied to other energy technologies such as combined heat and power (CHP).",
    }


# Function to display the definition of the selected term
def show_definition(*args):
    selected_term = entry_var.get().lower()
    definition.set(BitcoinTerminology.get(selected_term, "Term not found"))

# Autocomplete function for populating suggestions
def update_suggestions(*args):
    search_term = entry_var.get().lower()
    if search_term == "":
        suggestions.set([])
        return

    # Filter dictionary terms based on search query
    filtered_terms = [term for term in BitcoinTerminology if search_term in term.lower()]
    suggestions.set(filtered_terms[:5])  # Show top 5 suggestions

# Setup the GUI interface
root = tk.Tk()
root.title("Bitcoin Mining Dictionary")
root.geometry("500x500")

# Define tkinter variables
entry_var = tk.StringVar()
suggestions = tk.StringVar(value=[])
definition = tk.StringVar()

# Entry widget for user input
entry = ttk.Entry(root, textvariable=entry_var, width=50)
entry.pack(pady=10)
entry.bind("<KeyRelease>", update_suggestions)  # Update suggestions as user types

# Listbox for showing suggestions
listbox = tk.Listbox(root, listvariable=suggestions, height=5)
listbox.pack()

# Label for displaying the definition
definition_label = ttk.Label(root, textvariable=definition, wraplength=400)
definition_label.pack(pady=10)

# Event when a term is selected from the listbox
def on_select(event):
    if listbox.curselection():
        selected_term = listbox.get(listbox.curselection())
        entry_var.set(selected_term)
        show_definition()

listbox.bind("<<ListboxSelect>>", on_select)

# Show the definition when a term is typed or selected
entry_var.trace("w", show_definition)

root.mainloop()
