import os

class Device:
    def __init__(self, dev_id, timeslot, data_file):
        self.id = dev_id
        self.timeslot = timeslot
        self.data_file = data_file

    def transmit_data(self):
        print(f"Device {self.id} transmet les données :")
        if os.path.exists(self.data_file):  #File est la ou pas ? 
            try:
                with open(self.data_file, 'r', encoding='utf-8') as file:
                    for line in file:
                        print(line.strip())  
            except FileNotFoundError:
                print(f"Erreur : Fichier {self.data_file} introuvable.")
        else:
            print(f"Erreur : Fichier {self.data_file} introuvable.")
        print()

class TDMAProtocol:
    def __init__(self, devices):
        self.devices = devices

    def run_tdma(self, total_slots):
        for i in range(total_slots):
            print(f"Time Slot {i + 1}:")
            for device in self.devices:
                if device.timeslot == i:
                    device.transmit_data()
            print()

def main():
    num_devices = int(input("Entrez le nombre de périphériques au sein de l'avion : ")) #Combien de perif on a ? 
    devices = []


    
    for i in range(num_devices):
        dev_id = i + 1  # differencie les perifs par id 
        timeslot = int(input(f"Entrez le Time Slot du périphérique {i + 1} : "))
        data_file = input(f"Entrez le nom du fichier source pour le périphérique {i + 1} : ")
        devices.append(Device(dev_id, timeslot, data_file))
        
    # Determin quel nb max de slot needs 
    total_slots = max(device.timeslot for device in devices)
    tdma_protocol = TDMAProtocol(devices)
    tdma_protocol.run_tdma(total_slots)

if __name__ == "__main__":
    main()
