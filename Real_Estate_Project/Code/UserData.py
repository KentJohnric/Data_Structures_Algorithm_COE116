

class Data:

#----------Setters------------------#
    def setFullname(self,fullname):
        self.fullname = fullname

    def setUsername(self,username):
        self.username = username

    def setPassword(self,password):
        self.password = password

    def setPhoneContact(self,phonecontact):
        self.phonecontact = phonecontact

    def setEmail(self,email):
        self.email = email

#----------Getters-----------------#
    def getFullname(self):
        return self.fullname

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password
    def getPhoneContact(self):
        return self.phonecontact
    def getEmail(self):
        return self.email

#----------Functions---------------#

    def checkUsers(self,username):

        with open("Users.txt", "r") as usersfile:

            for lineread in usersfile.readlines():

                tempUser = lineread.split(";", 4)[3]
                if tempUser == username:
                    self.fullname = lineread.split(";",4)[0]
                    self.phonecontact = lineread.split(";", 4)[1]
                    self.email = lineread.split(";", 4)[2]
                    self.username = lineread.split(";", 4)[3]
                    self.password = lineread.split(";",4)[4]
                    return True
                    break

            return False



#Login check
    def checkLogin(self,username,password):
        with open("Users.txt","r") as usersfile:

            for lineread in usersfile.readlines():
                tempUser = lineread.split(";", 4)[3]
                tempPassword = lineread.split(";", 4)[4]
                stripPW = tempPassword.rstrip('\n')

                if tempUser == username and stripPW == password:
                    self.fullname = lineread.split(";",4)[0]
                    return True
                    break

            return False

    #save the data in file
    def Register(self):
        with open("Users.txt", "a") as usersfile:

            usersfile.write(self.fullname+";"+self.phonecontact+";"+self.email+";"+self.username+";"+self.password+"\n")

    #Delete users in text file
    def Deluser(self,username):
        with open("Users.txt","r") as userfile:
            lines = userfile.readlines()

        with open("Users.txt","w") as userfile:
            for line in lines:
                tempusername = line.split(";", 4)[3]

                if tempusername != username:
                    userfile.write(line)

    #check if the username is taken
    def checkUsername(self,username):
        with open("Users.txt","r") as userfile:

            for line in userfile.readlines():

                tempuser = line.split(";",4)[3]
                if tempuser == username:
                    return True
                    break

            return False

    def items(self):

        with open('Users.txt','r') as userfile:
            list=[]
            x = 1
            for line in userfile:
                data = line.split(';')
                Lines = str(x)+". "+ '--'.join(data)
                list.append(Lines)
                x=x+1
            return list













