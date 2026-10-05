from datetime import datetime

print("=" * 45)
print("          AURA HEALTH")
print("      Daily Wellness Check-In")
print("=" * 45)

name = input("Name: ")
sleep = float(input("Sleep duration (hours): "))
heart_rate = int(input("Resting heart rate (bpm): "))
energy = int(input("Energy level (1-10): "))
stress = int(input("Stress level (1-10): "))
mood = input("Mood today: ")

print("\n" + "=" * 45)
print("        DAILY WELLNESS SUMMARY")
print("=" * 45)

print("Date:", datetime.now().strftime("%d-%m-%Y"))
print("Name:", name)
print("Sleep:", sleep, "hours")
print("Resting Heart Rate:", heart_rate, "bpm")
print("Energy Level:", energy, "/10")
print("Stress Level:", stress, "/10")
print("Mood:", mood)

print("\nWellness check-in recorded successfully.")
print("AURA tracks wellness patterns over time.")