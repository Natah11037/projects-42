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
