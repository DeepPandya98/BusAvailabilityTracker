# BusAvailabilityTracker

## Description
Simple script created to track availability of bus tickets for McHacks 2019. The script checks "bus.mchacks.ca" every 5 minutes and automatically sends a text message to registered recipients when tickets become available. 

## Installation
```
git clone https://github.com/Deep297/BusAvailabilityTracker.git
```

# Install dependencies:

```
pip install -r requirements.txt
install tesseract onto computer
```

# Twilio Setup
  1. Create Twilio Account
  2. Buy a Twilio number
  3. Registered verified recipients
  
# Update config.json
```
Update ACCOUNT_SID, AUTH_TOKEN and NUMBER from Twilio
Update TESSERACT_FILEPATH to location of tesseract.exe installed on computer
Add verified recipients to NOTIF_RECIPIENTS
```

# Start Bus Tracker
```
python mcHacksBusTracker.py
```
