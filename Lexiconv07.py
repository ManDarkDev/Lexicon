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
root.geometry("500x300")

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
