from sys import stdout, stderr

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    data_first_input = input("Input Stream active. Enter archivist ID: ")
    data_second_input = input("Input Stream active. Enter status report: ")
    stdout.write(f"\n[STANDARD] Archive status from {data_first_input}:"
                 f" {data_second_input}\n")
    stderr.write("[ALERT] System diagnostic: Communication channels"
                 " verified\n")
    stdout.write("[STANDARD] Data transmission complete\n\n")
    print("Three-channel communication test successful.")
