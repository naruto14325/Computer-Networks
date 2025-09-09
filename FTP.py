# ftp_client.py
from ftplib import FTP

# Public test FTP server credentials
HOST = "ftp.dlptest.com"
USER = "dlpuser"
PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"

def ftp_demo():
    try:
        # 1. Connect to FTP server
        ftp = FTP(HOST)
        ftp.login(USER, PASS)
        print("Connected to:", HOST)
        print("Server welcome:", ftp.getwelcome())

        # 2. List directory contents
        print("\n=== Directory Listing ===")
        ftp.retrlines("LIST")

        # 3. Upload a file
        filename = "upload_test.txt"
        with open(filename, "w") as f:
            f.write("Hello FTP! This is a test upload.\n")

        with open(filename, "rb") as f:
            ftp.storbinary(f"STOR {filename}", f)
        print(f"\nUploaded file: {filename}")

        # 4. Download the file back
        downloaded = "downloaded_test.txt"
        with open(downloaded, "wb") as f:
            ftp.retrbinary(f"RETR {filename}", f.write)
        print(f"Downloaded file as: {downloaded}")

        # 5. Verify contents
        with open(downloaded, "r") as f:
            content = f.read()
        print("\n=== Downloaded File Content ===")
        print(content)

        # Close connection
        ftp.quit()
        print("\nFTP session closed.")

    except Exception as e:
        print("FTP error:", e)

if __name__ == "__main__":
    ftp_demo()
