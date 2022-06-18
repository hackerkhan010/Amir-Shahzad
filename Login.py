username=input("Enter Your Username :")
password=input("Enter Your Password :")
if username == 'admin':
  if password =='admin':
      print("Login Successful")
  else:
      print("Incorrect Password")
else:
      print("Incorrect Username")
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "facebook.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
© 2022 GitHub, Inc.
Terms
Privacy
Security
Statu
