from time import sleep
from pishockpy import PishockAPI

# CONFIG
api_key = ""  # Replace with your API key
username = ""  # Replace with your username
sharecode = ""  # Replace with your sharecode
app_name = "Sleep Timer"  # Replace with What you want to call this madness

pishock = PishockAPI(api_key, username, sharecode, app_name)

def get_user_input():
    timer_duration = int(input("Enter the timer duration (in seconds): "))
    shock_intensity = float(input("Enter the shock intensity, 0.01 being 1%, Then 1 being 100% (0.0-1.0): "))
    shock_duration = int(input("Enter the shock duration (in seconds, 1-15): "))
    return timer_duration, shock_intensity, shock_duration

def main():
    timer_duration, shock_intensity, shock_duration = get_user_input()
    print(f"Timer set for {timer_duration} seconds. Waiting...")
    sleep(timer_duration)
    print(f"Sending shock with intensity {shock_intensity} and duration {shock_duration} seconds.")
    if pishock.shock(shock_intensity, shock_duration):
        print("Shock was successful")


if __name__ == "__main__":
    main()
