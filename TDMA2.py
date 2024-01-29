import tkinter as tk
from tkinter import messagebox
import os

class Device:
    def __init__(self, dev_id, timeslot, data_file):
        self.id = dev_id
        self.timeslot = timeslot
        self.data_file = data_file

    def transmit_data(self):
        message = f"Device {self.id} transmet les données :\n"
        if os.path.exists(self.data_file):
            message += f"Le fichier {self.data_file} a été trouvé.\n"
            try:
                with open(self.data_file, 'r', encoding='utf-8') as file:
                    message += f"Lecture du fichier {self.data_file} :\n"
                    for line in file:
                        message += line.strip() + '\n'
            except FileNotFoundError:
                message += f"Erreur : Fichier {self.data_file} introuvable.\n"
        else:
            message += f"Erreur : Fichier {self.data_file} introuvable.\n"
        return message + '\n'

def create_device_frame(dev_id):
    frame = tk.Frame(root, padx=10, pady=5, bg="#f0f0f0")
    frame.pack(pady=10)

    label_timeslot = tk.Label(frame, text=f"Time Slot du périphérique {dev_id} : ", bg="#f0f0f0")
    label_timeslot.pack(side=tk.LEFT)

    entry_timeslot = tk.Entry(frame)
    entry_timeslot.pack(side=tk.LEFT)

    label_file = tk.Label(frame, text=f"Nom du fichier source pour le périphérique {dev_id} : ", bg="#f0f0f0")
    label_file.pack(side=tk.LEFT)

    entry_file = tk.Entry(frame)
    entry_file.pack(side=tk.LEFT)

    def create_device():
        timeslot_val = int(entry_timeslot.get())
        data_file_val = entry_file.get()
        if timeslot_val and data_file_val:
            devices.append(Device(dev_id, timeslot_val, data_file_val))
            messagebox.showinfo("Information", f"Périphérique {dev_id} ajouté avec succès!")
        else:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs!")

    button_device = tk.Button(frame, text="Valider", command=create_device, bg="#4caf50", fg="white")
    button_device.pack(side=tk.LEFT, padx=5)

def start_protocol():
    if devices:
        total_slots = max(device.timeslot for device in devices)
        for i in range(total_slots):
            output_text.insert(tk.END, f"Time Slot {i + 1}:\n")
            slot_devices = [device for device in devices if device.timeslot == i + 1]
            for device in slot_devices:
                output_text.insert(tk.END, device.transmit_data())
            output_text.insert(tk.END, "\n")
    else:
        messagebox.showwarning("Attention", "Aucun périphérique ajouté!")

devices = []

root = tk.Tk()
root.title("Protocole TDMA")
root.configure(bg="#f0f0f0")

label_devices = tk.Label(root, text="Nombre de périphériques au sein de l'avion : ", bg="#f0f0f0")
label_devices.pack()

entry_devices = tk.Entry(root)
entry_devices.pack()

button_devices = tk.Button(root, text="Configurer", command=lambda: [create_device_frame(i + 1) for i in range(int(entry_devices.get()))], bg="#2196f3", fg="white")
button_devices.pack()

button_start = tk.Button(root, text="Démarrer le protocole", command=start_protocol, bg="#f44336", fg="white")
button_start.pack()

output_text = tk.Text(root, height=20, width=50, bg="white", fg="black", font=("Arial", 10))
output_text.pack()

root.mainloop()
