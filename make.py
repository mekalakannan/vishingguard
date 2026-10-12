"""Creates fake_scam.wav (text-to-speech test audio) in the current folder.

Run:  python make_fake.py
Needs: pip install pyttsx3
"""
import pyttsx3

TEXT = "Sir, your bank account is blocked. Tell me the OTP immediately."

engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.save_to_file(TEXT, "fake_scam.wav")
engine.runAndWait()
print("fake_scam.wav ready")