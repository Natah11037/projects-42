if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n\n"
          "Initiating secure vault access...")
    try:
        with open("classifiyed_data.txt", "r") as secure_extraction:
            print("Vault connection established with failsafe protocols\n\n"
                  "SECURE EXTRACTION:")
            data_extracted = secure_extraction.read()
    except (FileNotFoundError, Exception):
        print("\nAn Error has occured during the extraction of the"
              " classified data\n")
    else:
        print(f"{data_extracted}\n")
    try:
        with open("security_protocols.txt", "w") as secure_preservation:
            print("SECURE PRESERVATION:")
            secure_preservation.write(data_extracted)
    except Exception:
        print("\nAn Error has occured during the preservation of the"
              " classified data\n")
    else:
        print("[CLASSIFIED] New security protocols archived\n"
              "Vault automatically sealed upon completion\n\n"
              "All vault operations completed with maximum security.")
