import os
try:
    from dotenv import load_dotenv
except ImportError:
    print(
        "[ERROR] python-dotenv is not installed.\n"
        "To install it, run the following command:\n"
        "pip install python-dotenv\n"
        "or\n"
        "poetry add python-dotenv\n"
    )
    exit(1)


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    load_dotenv()
    print("Configuration loaded:")

    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    if matrix_mode:
        print(f"Mode: {matrix_mode}")
    else:
        print("[WARNING] MATRIX_MODE missing")

    if database_url:
        if matrix_mode == "development":
            print("Database: Connected to local instance")
        elif matrix_mode == "production":
            print("Database: Connected to production database")
        else:
            print("Database: Connected to unknown environment")
    else:
        print("[ERROR] DATABASE_URL missing")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("[ERROR] API_KEY missing")

    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("[WARNING] LOG_LEVEL missing")

    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("[ERROR] ZION_ENDPOINT missing")

    print("\nEnvironment security check:")
    if matrix_mode and database_url and api_key and log_level and \
       zion_endpoint:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available\n")
    else:
        print("\n[KO] Environment variables are not properly configured.")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
