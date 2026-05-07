## task1-pw_checker.py

### Project title
Password Strength Checker
### Description
Takes a password as input and classifies its strength as **Weak**, **Medium**, or **Strong** based on:
- Length thresholds (>= 8, >= 12)
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of digits
- Presence of symbols

### How to run (commands used)
```bash
python task1-pw_checker.py
```

### Example
- Enter your password when prompted
- The script prints: `Password strength: <Weak/Medium/Strong>`

---------------------------------------------------------------------------------

## task2-Encrypt_decrypt.py

### Project title
Text Encrypt/Decrypt (Caesar Cipher)
### Description
Encrypts or decrypts a text string using a Caesar cipher approach:
- Supports both uppercase and lowercase letters
- Keeps non-alphabet characters unchanged
- Uses a user-provided shift value
- User selects: `e` for encrypt or `d` for decrypt

### How to run (commands used)
```bash
python task2-Encrypt_decrypt.py
```

### Example
- Enter text
- Enter shift value (integer)
- Type `e` to encrypt or `d` to decrypt
- The script prints: `Result: ...`

----------------------------------------------------------------------------------------------

## task3-check_phishing.py

### Project title
Phishing Message Checker
### Description
Checks a user-provided message/email for phishing-related keywords such as:
- `urgent`, `verify`, `password`, `bank`
- `click here`, `login`, `otp`
- `account blocked`, `update details`
- `win`, `prize`

If any keywords are found, it prints a warning and the list of matched red flags; otherwise it prints a safe-message confirmation.

### How to run (commands used)
```bash
python task3-check_phishing.py
```

### Example
- Enter email/message when prompted
- The script prints whether phishing signs are detected

-------------------------------------------------------------------------------------------------

## task4-System_Vulnerability.py

### Project title
System Vulnerability Checklist
### Description
A simple interactive checklist that asks for system security-related confirmations and prints status messages. It currently checks:
- Password length (>= 8 considered Strong)
- Whether the system is updated
- Whether the firewall is enabled
- Whether guest account is disabled

### How to run (commands used)
```bash
python task4-System_Vulnerability.py
```

### Example
- Enter password length
- Answer prompts with `yes` or `no`
- The script prints the security checklist results

------------------------------------------------------------------------------------------------

## Notes
- These scripts do not require extra dependencies; they use Python built-ins only.
- If you have multiple Python versions installed, you may need to use `python` vs `python3` depending on your setup.
