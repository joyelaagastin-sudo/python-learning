pcb = int(input("Enter the PCB percentage: "))
pcm = int(input("Enter the PCM percentage: "))

if pcb == 100:
    college = "Your ward has been selected in the Medical College."
elif pcm == 100:
    college = "Your ward has been selected in the Engineering College."
else:
    college = "Your ward has been selected in the Arts College."

print(college)