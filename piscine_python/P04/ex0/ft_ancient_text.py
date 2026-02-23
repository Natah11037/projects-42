import time
import os

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        file = open("ancient_fragment.txt", "r")
        print("Accessing Storage Vault: ancient_fragment.txt\n"
              "Connection established..\n")
        print("RECOVERED DATA:")
        file_content = file.read()
        file.close()
        print(file_content)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        time.sleep(2)
        os.system("clear")
        for i in range(10):
            print("\033[31m"
                  "ALERT !!! ALERT !!! ALERT !!!"
                  "ALERT !!! ALERT !!! ALERT !!!"
                  "ALERT !!! ALERT !!! ALERT !!!"
                  "ALERT !!! ALERT !!! ALERT !!!\n\n"
                  "\033[0m" * 10)
            time.sleep(2)
            os.system("clear")
            print("\033[31m⚠ CRITICAL ALERT - SECURITY BREACH DETECTED ⚠\n\n"
                  "[23:47:12] UNAUTHORIZED ACCESS from IP: 192.168.1.337\n"
                  "[23:47:13] Firewall breach on port 4242\n"
                  "[23:47:13] Encryption keys compromised\n"
                  "[23:47:14] User data exposed: 4,291 records leaked\n\n"
                  "THREAT LEVEL: CRITICAL\n"
                  "SYSTEMS AFFECTED: Authentication Server, Database, Backup"
                  "Node\n\n"
                  "Initiating emergency lockdown protocol...\n"
                  "Purging sensitive data...\n"
                  "Alerting security team...\n\n"
                  ">>> LOCKDOWN COMPLETE. All access revoked.\n"
                  ">>> Incident ID: #SEC-20260220-0042\n"
                  ">>> Estimated damage: SEVERE\n\n"
                  "ARCHIVE DATA LOST\n\n"
                  "Contact your system administrator immediately.\033[0m")
            time.sleep(4)
            os.system("clear")
