if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n\n"
          "Initializing new storage unit: new_discovery.txt")
    archive = open("new_discovery.txt", "w")
    print("Storage unit created successfully...\n\n"
          "Inscribing preservation data...")
    archive.write("[ENTRY 001] New quantum algorithm discovered\n")
    print("[ENTRY 001] New quantum algorithm discovered")
    archive.write("[ENTRY 002] Efficiency increased by 347%\n")
    print("[ENTRY 002] Efficiency increased by 347%")
    archive.write("[ENTRY 003] Archived by Data Archivist trainee\n\n")
    print("[ENTRY 003] Archived by Data Archivist trainee\n")
    print("Data inscription complete. Storage unit sealed.\n"
          "Archive 'new_discovery.txt' ready for long-term preservation.")
    archive.close()
