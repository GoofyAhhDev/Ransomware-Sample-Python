Ransomware Educational Sample

Overview:

This educational sample demonstrates a basic ransomware implementation for learning purposes only. It showcases how encryption and decryption can be applied to files in a directory structure using the Fernet symmetric encryption algorithm.


Disclaimer: This program is provided for educational purposes only. Please use it responsibly and only on systems for which you have proper authorization or permission, preferably permission obtained through a signed contract. The author (GoofyAhhDev) accepts no responsibility for any misuse or damage caused by this tool.


Usage:

    Startup:
        Run the script ransomware.py using Python.
        On startup, the program will display a welcome message and a disclaimer.

    Main Menu:
        The program presents a main menu with options to encrypt, decrypt, or quit.
        To choose an action, enter the corresponding key ('e' for encrypt, 'd' for decrypt, or 'q' to quit).

    Encryption:
        When selecting encryption, the user is prompted to provide the path to the target folder.
        Additionally, the user can choose to enable backup and receive an encryption key for decryption.
        If backup is enabled, files in the target folder will be copied to a backup folder before encryption.
        The encryption key will also be stored in a text file (encryption_key.txt) within the backup folder.
        If the user opts to receive an encryption key, a key will be generated and displayed after encryption.

    Decryption:
        To decrypt files, the user must provide the path to the encrypted folder and the encryption key.
        The program will decrypt all files in the specified folder using the provided key.

Dependencies:

    Python 3.x
    cryptography library
    six library

How to Run:

    Clone or download the repository to your local machine.
    Navigate to the project directory.
    Install "requirements.txt" with "pip install -r requirements.txt"
    Run the ransomware.py script using Python:

    python ransomware.py

Important Notes:

    I have not tested this code on systems other than windows so please be careful with what you do!
    Ensure you have Python installed on your system.
    Use this tool responsibly and only on your own systems.
    Do not use it for malicious purposes and only on systems with permission from the system owner.
    Understand the potential risks associated with encrypting files and losing access to them.