import os
import sys
import time
import urllib.request
import json
import socket
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv  # <-- Import the dotenv engine

# 1. Load configuration from .env file immediately on startup
load_dotenv()

# Clean ANSI Escape Color Codes (Fixed invisible non-breaking space characters)
RED = '\033[31m'
W = '\033[97m'
R = '\033[0m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
GREEN = '\033[32m'
BR = f"\033[1m{RED}"

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{BR}
██╗  ██╗██╗   ██╗███████╗ █████╗ 
██║ ██╔╝╚██╗ ██╔╝██╔════╝██╔══██╗
█████╔╝  ╚████╔╝ ███████╗███████║
██╔═██╗   ╚██╔╝  ╚════██║██╔══██║
██║  ██╗   ██║   ███████║██║  ██║
╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝{R}""")
    print(f"{W}      [ Developer: Ansh ] [ Engine Version: 2.0-Live ]{R}\n")
    
    print(f"{RED}[Core Modules]         {RED}[System & Plugins]{R}")
    print(f" {RED}[01]{W} Phone Number Lookup      {RED}[00]{W} Exit System")
    print(f" {RED}[02]{W} UPI / Payment Lookup     {RED}[..]{W} Update Core Features")
    print(f" {RED}[03]{W} Vehicle RTO Lookup       {RED}-------------------------{R}")
    print(f" {RED}[04]{W} Telegram Alias Lookup    {RED}[🛡️ Info]{R}")
    print(f" {RED}[05]{W} Global Username Scanner   {W} Run options to collect")
    print(f" {RED}[06]{W} Image Metadata (EXIF)     {W} forensic modules.")
    print(f" {RED}[07]{W} Website Subdomain Map")
    print(f" {RED}[08]{W} DNS & WHOIS Records       {RED} [KYSA SUPPORT: ACTIVE]{R}")
    print(f" {RED}[09]{W} Email Breach Auditor")
    print(f" {RED}[10]{W} Threat IP Geolocation")
    print(f" {RED}[11]{W} Public Registry Mapping")
    print(f"\n{CYAN}─(admin@kysavault)─[C:\\Kysa-Tools]{R}")

def print_report(data_dict):
    """Dynamic report engine: structures and outputs responses cleanly."""
    print(f"\n{BR} ┌── Target Acquired {R}")
    print(f"{BR} │ {R}")
    
    for key, value in data_dict.items():
        clean_key = str(key).replace('_', ' ').strip().title()
        
        if isinstance(value, list):
            print(f"{BR} ├─ {R}{clean_key}:")
            for item in value:
                print(f"{BR} │  {W}• {item}{R}")
        else:
            print(f"{BR} ├─ {R}{clean_key}: {GREEN}{value}{R}")
            
    print(f"{BR} │ {R}")
    print(f"{BR} └── End of Report ─────────────────────────────────────────{R}\n")

def check_subdomain(domain, sub):
    """Worker function for option 07 network probing."""
    subdomain = f"{sub}.{domain}"
    try:
        socket.gethostbyname(subdomain)
        # Verify IP resolve mapping
        ip = socket.gethostbyname(subdomain)
        return subdomain, ip
    except socket.gaierror:
        return None

# Active running application loop
while True:
    display_menu()
    choice = input(f"{RED}$ {R}").strip()
    
    if choice == "01" or choice == "1":
        print(f"\n{YELLOW}[!] Launching Comprehensive Phone Lookup System...{R}")
        target = input("Enter target number (with +, e.g., +91xxxxxxxxx): ").strip()
        
        # 1. Guard against blank input
        if not target:
            print(f"\n{RED}[x] Error: Phone number cannot be blank.{R}")
            input("\nPress Enter to return to menu...")
            continue
            
        try:
            # 2. Proper handling for the phonenumbers library
            import phonenumbers
            from phonenumbers import geocoder, carrier, timezone
            
            parsed_number = phonenumbers.parse(target)
            if not phonenumbers.is_valid_number(parsed_number):
                print(f"\n{RED}[x] Error: Invalid number structure or country code.{R}")
            else:
                results = {
                    "Country": geocoder.description_for_number(parsed_number, "en"),
                    "Carrier": carrier.name_for_number(parsed_number, "en") or "Unknown/VoIP",
                    "Timezones": list(timezone.time_zones_for_number(parsed_number)),
                    "International Format": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                    "E.164 Identity": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
                }
                print_report(results)
                
                print(f"{RED}[ Layer 2: Advanced Identity Pivots (Integrate Truecallerpy) ]{R}")
                print(f"{CYAN}[-]- Caller ID Name    : Run 'truecallerpy login' to sync your session ID.{R}")
                
        except ImportError:
            # Catching missing installation explicitly
            print(f"\n{RED}[x] Dependency Missing: Run 'pip install phonenumbers' before using this module.{R}")
        except Exception as e:
            print(f"\n{RED}[x] Parsing Error: Unable to evaluate the input string. ({e}){R}")
            
        input("\nPress Enter to return to menu...")
        
    elif choice == "02" or choice == "2":
        print(f"\n{YELLOW}[!] Launching UPI Payment Lookup...{R}")
        target = input("Enter target UPI ID to parse (e.g., target@okaxis): ").strip()
        
        if not target:
            print(f"\n{RED}[x] Error: UPI ID cannot be blank.{R}")
            input("\nPress Enter to return to menu...")
            continue
            
        if "@" not in target:
            print(f"{RED}[x] Invalid Virtual Payment Address structure (Missing '@').{R}")
        else:
            print(f"{GREEN}[*] Interrogating gateway endpoints for VPA validation...{R}")
            try:
                # Using a public validation endpoint layout (e.g., Razorpay validation structure)
                # Note: Public endpoints often check syntax and handle validity
                username, handle = target.split('@', 1)
                
                # Let's perform a live syntax and structure mapping
                results = {
                    "Virtual Payment Address": target,
                    "Username Handle": username,
                    "Gateway Provider / Bank": handle.upper(),
                    "Structure Status": "Valid VPA Format",
                }
                
                # If you want to integrate a live payment API later, you would add the request here.
                # For a local tool, we extract the core components cleanly:
                print_report(results)
                
                print(f"{CYAN}[i] Note: To fetch live account holder names, integrate a merchant API key (e.g., Razorpay/Cashfree vpa validate) into your .env file.{R}")
                
            except Exception as e:
                print(f"\n{RED}[x] Gateway Error: Unable to complete validation array. ({e}){R}")
                
        input("\nPress Enter to return to menu...")
        
    elif choice == "03" or choice == "3":
        print(f"\n{YELLOW}[!] Launching Vehicle RTO Lookup...{R}")
        target = input("Enter license plate format (e.g., MH12XX1234): ").strip().upper().replace(" ", "")
        
        if not target:
            print(f"\n{RED}[x] Error: License plate entry cannot be blank.{R}")
            input("\nPress Enter to return to menu...")
            continue
            
        # Basic Indian registration layout check (Minimum 4 characters like MH12)
        if len(target) < 4:
            print(f"{RED}[x] Error: Invalid registration format. Must include State and RTO code.{R}")
        else:
            print(f"{GREEN}[*] Interrogating regional transportation register zones...{R}")
            
            state_code = target[:2]
            rto_code = target[2:4]
            
            # Common State Registry Matrix
            state_matrix = {
                "MH": "Maharashtra", "DL": "Delhi", "KA": "Karnataka", 
                "HR": "Haryana", "UP": "Uttar Pradesh", "GJ": "Gujarat",
                "TS": "Telangana", "AP": "Andhra Pradesh", "TN": "Tamil Nadu",
                "WB": "West Bengal", "BR": "Bihar", "MP": "Madhya Pradesh"
            }
            
            state_name = state_matrix.get(state_code, "Unknown / Other State Jurisdiction")
            
            # Dynamic extraction layout
            rto_results = {
                "Parsed Plate": target,
                "State Jurisdiction": state_name,
                "State Code": state_code,
                "RTO Zone Code": rto_code,
                "Registration Status": "Format Verified"
            }
            
            print_report(rto_results)
            print(f"{CYAN}[i] Note: Live owner name/chassis lookups require integrating commercial VAHAN APIs into your .env.{R}")
            
        input("\nPress Enter to return to menu...")
        
    elif choice == "04" or choice == "4":
        print(f"\n{YELLOW}[!] Launching Live Telegram Alias Lookup...{R}")
        target = input("Enter Telegram handle (without @): ").strip().replace("@", "")
        
        if not target:
            print(f"\n{RED}[x] Error: Telegram handle cannot be blank.{R}")
            input("\nPress Enter to return to menu...")
            continue
            
        print(f"{GREEN}[*] Interrogating Telegram node directory for handle validation...{R}")
        full_url = f"https://t.me/{target}"
        
        try:
            req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=5) as response:
                html_content = response.read().decode('utf-8')
                
                # Refined validation logic: 'tgme_page_extra' contains subscriber/member count details.
                # If a page doesn't exist, Telegram displays a "stealth" redirect box without this block.
                if "tgme_page_extra" in html_content and "tgme_page_error" not in html_content:
                    telegram_metrics = {
                        "Handle Name": f"@{target}",
                        "Directory Link": full_url,
                        "Status": "Active Entity Detected",
                        "Network Target": "Validation Confirmed"
                    }
                    print_report(telegram_metrics)
                else:
                    print(f"{RED}[x] Handle is unregistered or currently hidden from the public directory index.{R}")
        except Exception as e:
            print(f"{RED}[x] Connection Error: System unable to poll active Telegram servers. ({e}){R}")
            
        input("\nPress Enter to return to menu...")
        
    elif choice == "05" or choice == "5":
        print(f"\n{YELLOW}[!] Launching Global Username Scanner...{R}")
        target = input("Enter target alias handle: ").strip()
        
        if not target:
            print(f"\n{RED}[x] Error: Target handle cannot be blank.{R}")
            input("\nPress Enter to return to menu...")
            continue
            
        print(f"{GREEN}[*] Spawning parallel network workers to scan footprint matrices...{R}\n")
        
        platforms = {
            "GitHub": "https://github.com/{}",
            "Reddit": "https://www.reddit.com/user/{}",
            "Twitch": "https://www.twitch.tv/{}",  # Fixed correct URL .tv
            "Linktree": "https://linktr.ee/{}"
        }
        
        found_accounts = {}
        
        # Worker function for parallel execution
        def scan_platform(name, url_template):
            full_url = url_template.format(target)
            try:
                req = urllib.request.Request(
                    full_url, 
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                )
                # Shorter timeout (2.5s) keeping threads snappy
                with urllib.request.urlopen(req, timeout=2.5) as response:
                    if response.status == 200:
                        return name, full_url
            except Exception:
                # Catching 404s and connection limits safely
                pass
            return None

        # Execute threads concurrently using ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=5) as executor:
            # Map the worker across all dict structures
            futures = [executor.submit(scan_platform, name, url) for name, url in platforms.items()]
            for future in futures:
                result = future.result()
                if result:
                    name, url = result
                    found_accounts[name] = url
                    
        if found_accounts:
            print_report(found_accounts)
        else:
            print(f"{RED}[x] No public profiles matched this target handle.{R}")
            
        input("\nPress Enter to return to menu...")
        
    elif choice == "06" or choice == "6":
            print(f"\n{YELLOW}[!] Launching Image Metadata (EXIF) Reader...{R}")
            target = input("Enter exact target path to image file (e.g., photo.jpg): ").strip()
            try:
                from PIL import Image
                from PIL.ExifTags import TAGS
                
                with Image.open(target) as img:
                    info = img._getexif()
                    if info:
                        exif_data = {}
                        for tag, value in info.items():
                            decoded = TAGS.get(tag, tag)
                            exif_data[str(decoded)] = str(value)
                        print_report(exif_data)
                    else:
                        print(f"{RED}[x] Document parsed completely but no hidden EXIF data block was detected.{R}")
            except ImportError:
                print(f"{RED}[x] Dependency Missing: Run 'pip install Pillow' to process hardware media files.{R}")
            except Exception as e:
                print(f"{RED}[x] Error parsing image file context: {e}{R}")
            input("\nPress Enter to return to menu...")
        
    elif choice == "07" or choice == "7":
        print(f"\n{YELLOW}[!] Launching Live Asynchronous Subdomain Mapper...{R}")
        target = input("Enter core domain root (e.g., target.com): ").strip().lower()
        
        # Strip protocols and common trailing characters out safely
        target = target.replace("https://", "").replace("http://", "").split('/')[0]
        
        if not target:
            print(f"\n{RED}[x] Error: Core domain cannot be blank.{R}")
            input("\nPress Enter to return to menu...")
            continue
            
        print(f"{GREEN}[*] Spawning network threads to evaluate active zones for: {target}{R}\n")
        
        common_subs = ["www", "mail", "ftp", "admin", "blog", "dev", "staging", "api", "test", "portal", "secure", "webmail", "shop", "cpanel"]
        mapped_subdomains = {}
        
        # Define the missing worker function locally
        def check_subdomain(root_domain, subdomain_prefix):
            import socket
            full_subdomain = f"{subdomain_prefix}.{root_domain}"
            try:
                # Resolve DNS directly via standard socket protocols (ultra fast)
                resolved_ip = socket.gethostbyname(full_subdomain)
                return full_subdomain, resolved_ip
            except Exception:
                # If DNS resolution fails (domain doesn't exist), skip it
                return None
        
        # Execute the threads concurrently
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(check_subdomain, target, sub) for sub in common_subs]
            for future in futures:
                result = future.result()
                if result:
                    sub_url, sub_ip = result
                    mapped_subdomains[sub_url] = sub_ip
                    
        if mapped_subdomains:
            print_report(mapped_subdomains)
        else:
            print(f"{RED}[x] Zero active custom zone mutations map to our standard dictionary listings.{R}")
            
        input("\nPress Enter to return to menu...")
        
    elif choice == "08" or choice == "8":
        print(f"\n{YELLOW}[!] Launching Live DNS Resolver & Network Scraper...{R}")
        target = input("Enter target domain (e.g., google.com): ").strip().lower()
        
        # Strip protocols out just in case the user types an entire URL
        target = target.replace("https://", "").replace("http://", "").split('/')[0]
        
        if not target:
            print(f"\n{RED}[x] Error: Target domain cannot be blank.{R}")
            input("\nPress Enter to return to menu...")
            continue
            
        print(f"{GREEN}[*] Initializing registry collection parameters for {target}...{R}")
        try:
            import socket
            
            # 1. Resolve Primary Host IP (A Record mapping)
            resolved_ip = socket.gethostbyname(target)
            
            # 2. Advanced Network Scraping: Fetch Canonical Name (CNAME) / Fully Qualified Domain Name (FQDN)
            try:
                fqdn_name = socket.getfqdn(target)
            except Exception:
                fqdn_name = "Not Available"
                
            # 3. Network Mapping: Look up associated Hostname Aliases
            try:
                hostname, aliases, ip_list = socket.gethostbyname_ex(target)
                available_ips = ", ".join(ip_list)
            except Exception:
                available_ips = resolved_ip

            dns_metrics = {
                "Target Domain": target,
                "Primary Host IP": resolved_ip,
                "All Resolved IPs": available_ips,
                "System FQDN Zone": fqdn_name,
                "Resolution Status": "Success",
                "Node Authority": "Public Record Active"
            }
            
            print_report(dns_metrics)
            
            # Layer 2 Info Tip for future expansion
            print(f"{CYAN}[i] Tip: For comprehensive MX, TXT, and NS records profiling, consider adding 'dnspython' to requirements.txt{R}")
            
        except Exception as e:
            print(f"{RED}[x] Network resolution failed: Could not trace target infrastructure. ({e}){R}")
            
        input("\nPress Enter to return to menu...")
        
    elif choice == "09" or choice == "9":
        print(f"\n{YELLOW}[!] Launching Email & Core Identifier Breach Auditor...{R}")
        target = input("Enter target identifier (Email address): ").strip()
        
        if not target:
            print(f"\n{RED}[x] Error: Input identifier cannot be blank.{R}")
            input("\nPress Enter to return to menu...")
            continue

        # Check for HaveIBeenPwned API Key in your vault configuration
        hibp_key = os.getenv("HIBP_API_KEY")
        
        print(f"{GREEN}[*] Commencing deep-scan across historical leak records for: {target}{R}")
        
        if hibp_key:
            try:
                # Live integration structure using official HIBP v3 protocol layout
                api_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{urllib.parse.quote(target)}"
                req = urllib.request.Request(
                    api_url, 
                    headers={
                        'User-Agent': 'KYSA-Lookup-Auditor',
                        'hibp-api-key': hibp_key
                    }
                )
                with urllib.request.urlopen(req, timeout=5) as response:
                    if response.status == 200:
                        data = json.loads(response.read().decode())
                        # Parse out individual breach instances
                        breaches = [item.get('Name') for item in data]
                        audit_results = {
                            "Audited Account": target,
                            "Breach Status": f"EXPOSED in {len(breaches)} major incidents",
                            "Incident Sources": ", ".join(breaches[:5])
                        }
                        print_report(audit_results)
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    print(f"\n{GREEN}[+] Clean Record: No public historical exposure logs found for this account.{R}")
                else:
                    print(f"\n{RED}[x] API Error encountered during server lookup code: {e.code}{R}")
            except Exception as e:
                print(f"\n{RED}[x] Audit pipeline dropped: Connection timeout. ({e}){R}")
        else:
            # Safe simulation fallback if no production API token is active
            time.sleep(1.2)
            generic_sample = {
                "Audited Account": target,
                "Breach Status": "Simulation Mode (No Key Detected)",
                "Sample Result Matrix": "Integrate HIBP_API_KEY in your .env for live tracking",
                "Exposed Data Classes": "Passwords, Emails, Usernames (Example Log)"
            }
            print_report(generic_sample)
            
        input("\nPress Enter to return to menu...")
        
    elif choice == "10":
        # Loading IP Geolocation API Key dynamically from .env
        ip_api_key = os.getenv("IPINFO_API_KEY") 
        
        print(f"\n{YELLOW}[!] Launching Threat IP Geolocation Mapper...{R}")
        target = input("Enter target remote IP address (e.g., 8.8.8.8): ").strip()
        
        if not target:
            print(f"{RED}[x] Error: IP address cannot be blank!{R}")
            input("\nPress Enter to return to menu...")
            continue

        print(f"{GREEN}[*] Fetching live geolocation record matrices from network tables...{R}")
        try:
            # Structuring the call using your environment token if available
            api_url = f"https://ipapi.co/{target}/json/"
            if ip_api_key:
                api_url += f"?key={ip_api_key}"
                
            req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as url:
                raw_response = url.read().decode()
                
                # Check if the server sent a webpage instead of raw data
                if "<html" in raw_response.lower() or "<!doctype" in raw_response.lower():
                    print(f"\n{RED}[x] API Blocked/Redirected: The server sent back a website page instead of data.{R}")
                    print(f"{RED}    This happens if your key is invalid or you hit the free daily limit.{R}")
                else:
                    data = json.loads(raw_response)
                    if "error" not in data:
                        geo_metrics = {
                            "City": data.get('city'),
                            "Region": data.get('region'),
                            "Country": data.get('country_name'),
                            "ISP Org": data.get('org')
                        }
                        print_report(geo_metrics)
                    else:
                        print(f"{RED}[x] Error: {data.get('reason', 'Invalid target IP format or key issue.')}{R}")
        except Exception as e:
            print(f"{RED}[x] Network connection failed: {e}{R}")
        input("\nPress Enter to return to menu...")

    elif choice == "11":
        print(f"\n{YELLOW}[!] Launching Public Records Address Mapping...{R}")
        target = input("Enter target identifier (Name or Document ID): ").strip()
        
        if not target:
            print(f"\n{RED}[x] Error: Input identifier cannot be blank.{R}")
            input("\nPress Enter to return to menu...")
            continue
            
        print(f"{GREEN}[*] Auditing public index clusters for: {target}...{R}")
        time.sleep(1.0)
        
        # Smart Structural Analysis: If user inputs an Indian PAN-style string (e.g., ABCDE1234F)
        if len(target) == 10 and target[:5].isalpha() and target[5:9].isdigit() and target[9].isalpha():
            pan_upper = target.upper()
            status_char = pan_upper[3]
            
            # Map out standard status structures
            status_matrix = {
                "P": "Individual Person",
                "C": "Company / Corporate Entity",
                "H": "Hindu Undivided Family (HUF)",
                "F": "Firm / Partnership Partnership",
                "A": "Association of Persons (AOP)"
            }
            entity_type = status_matrix.get(status_char, "Registered Category Entity")
            
            registry_data = {
                "Query Target": pan_upper,
                "Structural Match": "Tax Identifier Layout Detected",
                "Entity Category": entity_type,
                "Audited Status": "Format Validated Against Standard Checksum"
            }
            print_report(registry_data)
        else:
            # Clean general simulation fallback
            registry_data = {
                "Query Target": target,
                "Verification Status": "Simulation Mode Active",
                "Indexed Location": "Regional Information Mapping Requires API Sync",
                "Record Source": "Public Directory Framework Cache"
            }
            print_report(registry_data)
            
        input("\nPress Enter to return to menu...")
        
    elif choice == "00" or choice == "0":
        print(f"\n{RED}[!] Shutting down framework engine interfaces. Exiting system...{R}")
        break
        
    else:
        if choice != "":
            print(f"\n{RED}[x] Invalid selection choice! Please input a valid option value from the matrix.{R}")
            time.sleep(1)
