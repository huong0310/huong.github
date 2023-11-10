notefrequency_table = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88
}
frequency = float(input("Enter the frequency in Hz: "))
for note, notefrequency in notefrequency_table.items():
    if abs(frequency - notefrequency) <= 1:
        print("The frequency corresponds to the note:", note)
        break
else:
    print("The frequency does not correspond to a known note.")