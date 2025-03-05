import os
import speedtest
import psutil
import subprocess
from datetime import datetime

def clear_screen():
    os.system('clear')  # Changed from 'cls' to 'clear' for Unix-like systems

def print_header():
    clear_screen()
    print("╔══════════════════════════════════════╗")
    print("║           System Tools v1.0          ║")
    print("║        " + datetime.now().strftime("%Y-%m-%d %H:%M") + "        ║")
    print("║      Launch Command: tools           ║")
    print("╚══════════════════════════════════════╝\n")

def print_menu_item(number, text, selected=False):
    if selected:
        print(f"  >> {number}. {text} <<")
    else:
        print(f"     {number}. {text}")

def app_menu():
    while True:
        print_header()
        print("═══════ App Features Menu ═══════\n")
        options = [
            "Force Stop Application",
            "Kill Background Apps",
            "Clear App Cache",
            "Back to Main Menu"
        ]
        for i, option in enumerate(options, 1):
            print_menu_item(i, option)
        
        print("\n" + "─" * 36)
        choice = input("\nSelect an option (1-4): ")
        
        if choice == '1':
            app_force_stop()
        elif choice == '2':
            kill_background_apps()
        elif choice == '3':
            clear_app_cache()
        elif choice == '4':
            break

def main_menu():
    while True:
        print_header()
        print("═══════════ Main Menu ═══════════\n")
        options = [
            "App Features",
            "WiFi Tools",
            "Exit"
        ]
        for i, option in enumerate(options, 1):
            print_menu_item(i, option)
        
        print("\n" + "─" * 36)
        choice = input("\nSelect an option (1-3): ")
        
        if choice == '1':
            app_menu()
        elif choice == '2':
            wifi_speed_test()
        elif choice == '3':
            clear_screen()
            print("\n╔══════════════════════════════════════╗")
            print("║         Thank you for using!         ║")
            print("║             Goodbye!                 ║")
            print("╚══════════════════════════════════════╝")
            break

def app_force_stop():
    clear_screen()
    print("=== Force Stop Application ===")
    # List running processes
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"PID: {proc.info['pid']} - Name: {proc.info['name']}")
    
    pid = input("\nEnter PID to force stop (or 'q' to quit): ")
    if pid.lower() != 'q':
        try:
            subprocess.run(f"kill -9 {pid}", shell=True)  # Changed from taskkill to kill command
            print("Application stopped successfully")
        except:
            print("Failed to stop application")
    input("\nPress Enter to continue...")

def clear_app_cache():
    clear_screen()
    print("=== Clear App Cache ===")
    temp_path = os.path.expanduser("~/storage/shared/Android/data")  # Changed to Android data directory
    try:
        for item in os.listdir(temp_path):
            item_path = os.path.join(temp_path, item)
            try:
                if os.path.isfile(item_path):
                    os.unlink(item_path)
                else:
                    os.rmdir(item_path)
            except:
                continue
        print("Cache cleared successfully")
    except:
        print("Failed to clear cache")
    input("\nPress Enter to continue...")

def kill_background_apps():
    clear_screen()
    print("=== Kill Background Applications ===")
    killed = 0
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Skip system processes
            if proc.info['pid'] > 1000:
                proc.kill()
                killed += 1
        except:
            continue
    print(f"Killed {killed} background applications")
    input("\nPress Enter to continue...")

def wifi_speed_test():
    clear_screen()
    print("=== WiFi Speed Test ===")
    print("Testing... Please wait...")
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        
        print(f"\nDownload Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
        print(f"Ping: {ping:.2f} ms")
    except:
        print("Failed to perform speed test")
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()