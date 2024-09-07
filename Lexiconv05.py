#Dictionaries are a built-in data type that store key-value pairs. 
#They are unordered, mutable, and indexed by keys, which can be of any immutable type (like strings, numbers, or tuples)
#You can give them order though
'Bitcoin Mining Dictionary'
import os
import time
import json
from pynput import mouse
from threading import Thread
import keyboard  # Import keyboard for detecting keypress
BtcWord = input(" ")


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
    "hfuel" : "Hydrogen fuel cells generate electricity by combining hydrogen and oxygen in an electrochemical process, producing water as the only byproduct ",
    "Wave Energy" : "Wave energy - converts the up-and-down motion of ocean waves into electricity through specialized devices that capture and transfer the energy",
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
    "ppa": "Power Purchase Agreement - an arrangement in which a third-party developer installs, owns, and operates an energy system on a customer’s property. The customer then purchases the system's electric output for a predetermined period. A PPA allows the customer to receive stable and often low-cost electricity with no upfront cost, while also enabling the owner of the system to take advantage of tax credits and receive income from the sale of electricity. Though most commonly used for renewable energy systems, PPAs can also be applied to other energy technologies such as combined heat and power (CHP)."
    ,}

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to animate scrolling text horizontally indefinitely
def scroll_text_horizontally(text, width=80, delay=0.05):
    global stop_scrolling  # Global flag to control scrolling
    padded_text = ' ' * width + text + ' ' * width
    stop_scrolling = False  # Reset the flag

    def on_click(x, y, button, pressed):
        global stop_scrolling
        if pressed:
            stop_scrolling = True
            return False  # Returning False to stop the listener

    listener = mouse.Listener(on_click=on_click)
    listener.start()  # Start the listener for mouse clicks

    try:
        while not stop_scrolling:
            for i in range(len(padded_text) - width + 1):
                if stop_scrolling:
                    break
                clear_screen()
                print(padded_text[i:i+width])
                time.sleep(delay)
    finally:
        listener.stop()  # Stop the mouse listener
        clear_screen()
        print(text)  # Print the full text once scrolling stops

# Function to get definition by keyword and scroll it indefinitely
def get_definition():
    print(json.dumps(BitcoinTerminology, indent=2))  # Debug: Print the dictionary for verification

    while True:
        BtcWord = input("Enter Code Name or 'exit' to quit: ").strip().lower()  # Normalize input

        if BtcWord == "exit":
            print("Exiting the program.")
            break
        elif BtcWord in BitcoinTerminology:
            definition = BitcoinTerminology[BtcWord]
            formatted_output = f"{BtcWord}: {definition}"
            print(f"Debug: Found definition for {BtcWord}")  # Debug: Confirm dictionary lookup
            # Start a thread to listen for key presses
            Thread(target=keyboard.wait, args=('esc',)).start()  # Wait for 'esc' key to stop scrolling
            scroll_text_horizontally(formatted_output)
        else:
            print(f"Debug: {BtcWord} not found in dictionary.")  # Enhanced debug statement
            print("Keyword not found. Please try again.")

# Main function to start the program
if __name__ == "__main__":
    get_definition()

#Explanation:
#BitcoinTerminology Dictionary: This dictionary contains the keywords and their corresponding definitions.
#Input Loop: The script enters a loop that prompts the user to input a keyword.
#'all' Keyword: If the user types all, the script will display all keywords and their definitions.
#'exit' Keyword: Typing exit will stop the program.
#Keyword Search: If the input matches a keyword in the dictionary, the script will display the corresponding definition. If the keyword is not found, it will prompt the user to try again.
#You can run this script in any Python environment to test it out!









