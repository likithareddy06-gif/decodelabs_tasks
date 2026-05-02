def check_phishing(message):
    phishing_keywords = [
        "urgent", "verify", "password", "bank",
        "click here", "login", "otp",
        "account blocked", "update details",
        "win", "prize"
    ]
    red_flags = []
    msg = message.lower()
    for word in phishing_keywords:
        if word in msg:
            red_flags.append(word)
    if red_flags:
        print("⚠️ Phishing Message Detected!")
        print("Red Flags Found:", red_flags)
        print("Reason: Message contains suspicious keywords.")
    else:
        print("✅ Safe Message (No major phishing signs detected)")
message = input("Enter email/message: ")
check_phishing(message)