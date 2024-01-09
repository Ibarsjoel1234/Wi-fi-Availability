import subprocess

def get_available_networks():
    result = subprocess.check_output(["netsh", "wlan", "show", "network"])
    output = result.decode("utf-8")
    return output

def get_all_profiles():
    results = subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    outputs = results.decode("utf-8")
    return outputs

def get_all_an():
    values = subprocess.check_output(["netsh", "wlan", "show", "all"])
    ##final = values.decode("utf-8")
    return values

def main():
    
    print("\n")
    print("NOTE:\n")
    print("Press 1 for the Available WLAN Networks\n")
    print("Press 2 for the Available Network Profiles\n")
    print("Press 3 for the Available Network Profiles All\n")  # Added option for 3
    print("\n")
    user_input = input("Enter the number: ")

    networks = get_available_networks()
    ava_ns = get_all_profiles()
    nm = get_all_an()

    if user_input == "1":
        print("Available WLAN Networks:")
        print(networks)
    elif user_input == "2":
        print("All networks:")
        print(ava_ns)
    elif user_input == "3":
        print("All networks:")
        print(nm)
    else:
        print("Invalid input. Please enter 1 or 2 or 3.")

if __name__ == "__main__":
    main()
