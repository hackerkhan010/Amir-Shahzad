username=input("Enter Your Username :")
password=input("Enter Your Password :")
if username == 'admin':
  if password =='admin':
      print("Login Successful")
  else:
      print("Incorrect Password")
else:
      print("Incorrect Username")
