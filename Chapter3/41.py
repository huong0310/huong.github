base_frequency = 261.63
note = input("Enter the note name (e.g., C4): ")
letter = note[0]
octave = int(note[1])
frequency = base_frequency / (2 ** (4 - octave))
print("The frequency of", note, "is", frequency, "Hz.")