#Dictionaries are a built-in data type that store key-value pairs. 
#They are unordered, mutable, and indexed by keys, which can be of any immutable type (like strings, numbers, or tuples)
#You can give them order though
'Bitcoin Mining Dictionary'
import time
import os
import json
BtcWord = input(" ")


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
    "Hash$":"Hashprice - The hashprice metric is a financial measure used in the cryptocurrency mining industry to evaluate the daily revenue a miner can generate per unit of hash rate, typically expressed in dollars per terahash per day ($TH/day)",
    "Pool" : "Mining pool - a collective group of miners who combine their computational resources over a network to increase their chances of successfully mining a block and earning Bitcoin rewards.",
    "Form": "Transformer - An electrical device that transfers energy between two or more circuits through electromagnetic induction, used in Bitcoin mining to step up or step down voltage levels according to the power requirements of the mining hardware.",
    "Gear": "Switchgear - An assembly of electrical disconnect switches, fuses, or circuit breakers used to control, protect, and isolate electrical equipment in a Bitcoin mining operation to enhance safety and manage load distribution",
    "PDU" : "Power Distrubution Unit - A device that distributes electrical power to various components or systems within a Bitcoin mining setup, typically from a single source to multiple mining rigs",
    "Disk" : "Disk Management (in the context of downloading and putting firmware to a new Bitcoin machine) – The process of preparing, configuring, and maintaining the storage system on a Bitcoin mining device, which includes downloading the appropriate firmware and installing it to ensure the machine operates with the latest updates and optimal settings",
    "UI" : "User Interface - also known as Graphical User Interface (GUI) A visual part of a computer application or operating system through which a user interacts with a computer or software using graphical icons, visual indicators, and text.",
    "Gen": "Genesis Block - The first block of the Bitcoin blockchain, created by Bitcoin's pseudonymous founder, Satoshi Nakamoto, on January 3, 2009. This foundational block, also known as Block 0, contains a special embedded message and serves as the starting point of the Bitcoin network. The 50 BTC reward from the Genesis Block is unspendable due to its unique construction",
    "AIR": "Air Cooling - A method of cooling Bitcoin mining equipment by using fans or blowers to circulate air across the hardware, dissipating heat generated by the mining process. This is the most common and traditional cooling method, relying on airflow to maintain optimal operating temperatures for mining rigs",
    "3P" : "3 Phase Electricity - Three-phase electricity is a type of electrical power distribution that uses three alternating currents, each phase offset by one-third of the cycle to provide a continuous flow of energy",
    "1P" : "Single Phase Electricity - One-phase electricity, or single-phase power, involves a single alternating current that delivers electric power in a unidirectional flow, typically used in residential properties.",
    "Satoshi": "Satoshi Nakamoto - the pseudonymous person or group who developed Bitcoin, authored its original white paper, and designed and launched the first version of the Bitcoin software",
    "Sat": "Sat - A satoshi, often abbreviated as sat, is the smallest unit of the Bitcoin cryptocurrency, named after its creator, Satoshi Nakamoto. One satoshi is equal to one hundred millionth of a single Bitcoin, or 0.00000001 BTC",
    }

print(json.dumps(BitcoinTerminology, indent=2))  # Add this line after defining the dictionary

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to animate scrolling text horizontally
def scroll_text_horizontally(text, width=80, delay=0.05):
    padded_text = ' ' * width + text + ' ' * width
    for i in range(len(padded_text) - width + 1):
        clear_screen()
        print(padded_text[i:i+width])
        time.sleep(delay)

def get_definition():
    while True:
        BtcWord = input("Enter Code Name or 'exit' to quit: ").strip()

        if BtcWord.lower() == "exit":
            print("Exiting the program.")
            break
        else:
            # Normalize the input to lowercase for case-insensitive matching
            BtcWord = BtcWord.lower()
            # Use a case-insensitive search for keys
            matched_key = next((key for key in BitcoinTerminology if key.lower() == BtcWord), None)
            if matched_key:
                definition = BitcoinTerminology[matched_key]
                scroll_text_horizontally(f"{matched_key}: {definition}")
            else:
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






