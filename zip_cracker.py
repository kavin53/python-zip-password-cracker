import zipfile

pwd_file = input("enter password file path : ")
zip_file = input("enter zip file path : ")

zip_file = zipfile.ZipFile(zip_file)
pwd_file = open(pwd_file,'r')

found = False

for password in pwd_file:
     try:
         zip_file.extractall(pwd=password.strip("\n").encode())
         print(f"password found = {password}")
         found = True
         break
     except:
         found = False
         pass
if found == False:
    print("password not found")




