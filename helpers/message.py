RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[00m"

def PRINT_ERROR(s):
    print(f"{RED}[-] {s}{RESET}")


def PRINT_SUCCESS(s):
    print(f"{GREEN}[+] {s}{RESET}")


def PRINT_MESSAGE(s):
    print(f"[!] Message:{CYAN} {s}{RESET}")
