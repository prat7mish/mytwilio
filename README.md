The project is for sms authentication of the user. The following steps are involved:
1. Ensure to update the following fields in settings.py:
      TWILIO_ACCOUNT_SID = "Your_SID"
      TWILIO_AUTH_TOKEN = "Your Token"
      
2. Then in your localhost on the browser you'll be prompted to enter your phone number(eg:+919988562310)
3. 4 digit OTP is generated which can be viewed in the terminal and also as an SMS to the number entered.
4. If the OTP is then successfully entered, then the user lands on "Success" page else the user is redirected back on the same page to enter the correct OTP.
