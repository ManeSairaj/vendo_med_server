import sys
import time

# Simulated motor pin mapping
motor_pins = {
    '1': 17,
    '2': 18,
    '3': 27,
    '4': 22
}

# Read command-line arguments
args = sys.argv[1:]

if len(args) == 0 or len(args) > 4:
    print("Usage: python mock_rotate_servos.py [1-4] (up to 4 motors)")
    sys.exit(1)

# Simulate rotating each requested motor
for motor_num in args:
    if motor_num not in motor_pins:
        print(f"[ERROR] Invalid motor number: {motor_num}. Use 1, 2, 3, or 4.")
    else:
        print(f"[INFO] Simulating rotation of Motor {motor_num} (GPIO {motor_pins[motor_num]}) to 90°")
        time.sleep(0.5)
 
print("[INFO] Simulation complete.")