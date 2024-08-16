#Dictionaries are a built-in data type that store key-value pairs. 
#They are unordered, mutable, and indexed by keys, which can be of any immutable type (like strings, numbers, or tuples)

'Bitcoin Mining Dictionary'

import json

BitcoinTerminology = {

    "PSU": "Power Supply Unit - a critical hardware component that converts electrical power into a form usable by the computer's internal components.",
    "HB": "Hashboard - are specialized circuit boards used in Bitcoin mining machines, particularly in ASIC miners.",
    "CB": "Control Board - The control board acts as the communication bridge between the miner's hashboards and the external network (e.g., mining pool, internet).",
    "TH/s": "Terrahash per second - a unit of measurement used to describe the computational power or hash rate of a Bitcoin mining machine or network.",
    "$/KwH": "Cost per Kilowatt-Hour - the amount of money charged for consuming one kilowatt-hour of electrical energy, (ex. $0.10/kWh). Used to calculate the cost of electricity usage over time.",
    "IP": "IP Address - a unique numerical identifier assigned to each device connected to a computer network that uses the Internet Protocol for communication.",
    "SN": "Serial Number - a unique identifier assigned to a specific item, device, or product by the manufacturer.",
    "MAC": "Media Access Control Address - a unique identifier assigned to network interfaces for communication on the physical network segment.",
    "IT": "Information Technology - a set of related fields that encompass computer systems, software, programming languages, and data and information processing, and storage.",
    "API": "Application Programming Interface - a set of rules, protocols, and tools that enables software applications to communicate with each other, exchange data, and share functionality.",
    "FIRM": "Firmware - is a specialized software program embedded in hardware devices that provides low-level control and operates the device's functions.",
    "ASIC": "Application-Specific Integrated Circuit - A custom-designed microchip optimized for a specific task. Performs specialized computations(i.e. a hash).",

}

print(BitcoinTerminology["HB"])
# Convert dictionary to a formatted string with keys sorted alphabetically
formatted_output = json.dumps(BitcoinTerminology, indent=4, sort_keys=True)

# Print the formatted string
print(formatted_output)
