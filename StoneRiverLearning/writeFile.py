
##Working with Files and Classes


#Write to a file

writeMe = "example"

saveFile = open('testFileWrite.txt','w')
saveFile.write(writeMe)
saveFile.close()

#Append to a file

appendMe = "\n append example \n"

saveFile = open('testFileAppend.txt','a')
saveFile.write(appendMe)
saveFile.close()

#Read a file

readMe = open('testFileAppend.txt','r').read()
print(readMe)