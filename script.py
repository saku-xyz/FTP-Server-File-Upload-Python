#!/usr/bin/env python
# coding: utf-8

# # FTP Server
# 
# One of the main features of FTP server is the ability to store and retrieve files. In this tutorial, you will learn how you can download and upload files in FTP server using Python.
# 
# We will be using Python's built-in ftplib module, we gonna use a test FTP server for this tutorial, it is called DLPTEST, let's define its information:

# In[1]:


import ftplib

FTP_HOST = "ftp.example.com"
FTP_USER = "ftp@example.com"
FTP_PASS = "Password@123"


# The password can change from time to time, make sure you visit their website for the correct credentials, connecting to this server:

# In[2]:


# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"


# ## Uploading Files
# 
# To upload a file, we gonna need to use the ftp.storbinary() method, the below code handles that:

# In[3]:


# local file name you want to upload
filename = "index.html"
with open(filename, "rb") as file:
    # use FTP's STOR command to upload the file
    ftp.storbinary("STOR index.html", file)


# We opened the file with "rb" mode, which means we're reading the local file in binary mode.
# 
# After that, we used the FTP's STOR command, which stores the file in binary mode, it transfer that file on a new port. Note that the file must exist in your local working directory, otherwise this won't work.
# 
# This test server will delete the file after 30 minutes, to make sure the file is successfully uploaded, we need to list all files and directories using ftp.dir() method:

# In[4]:


# list current files & directories
ftp.dir()


# ## Downloading files
# 
# Now let's try to download that same file again:

# In[5]:


# the name of file you want to download from the FTP server
filename = 'index.html'
with open(filename, "wb") as file:
    # use FTP's RETR command to download the file
    ftp.retrbinary("RETR index.html", file.write)


# This time, we're opening the local file in "wb" mode, as we're gonna write the file from the server to the local machine.
# 
# We're using RETR command, which downloads a copy of a file on the server, we provide the file name we want to download as the first argument to the command, and the server will send a copy of the file to us.
# 
# ftp.retrbinary() method takes the method to call when storing the file on the local machine as a second argument.

# Finally, you got to quit and close the FTP connection:

# In[6]:


# quit and close the connection
ftp.quit()

