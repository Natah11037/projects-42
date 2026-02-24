if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n\n"
          "CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as extraction:
            data_extracted = extraction.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    finally:
        print("STATUS: Crisis handled, system stable\n")

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "w") as extraction2:
            extraction2.write("New Data stored")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained\n")

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as extraction3:
            data_extracted3 = extraction3.read()
    except Exception:
        print("RESPONSE: Security protocols closed due to an error")
    else:
        print(f"SUCCESS: Archive recovered - '{data_extracted3}'")
    finally:
        print("STATUS: Normal operations resumed\n")

    print("All crisis scenarios handled successfully. Archives secure.")
