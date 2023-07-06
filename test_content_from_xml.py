import os
import re

number = 300
# path = "/mnt/c/Users/may-8/extract/"
path = "C:\Users\may-8\CC_myfiles\CC_70\CC_70000_190225_70044_MD_06210\CC_70000_190225_70044_MD_06210_00003.xml"

test_files = os.listdir(path)
print("start with", test_files[0])
file_to_write = open("ocr_output.txt", 'w+')

for i in range(number) :
    with open (path+test_files[i]) as my_file :
        print("file is "+test_files[i])
        reading = my_file.readlines()
        file_to_write.write("FROM FILE "+test_files[i]+"\n")

        # au cas où il y ait plusieurs contents dans le xml, on les compte
        # k = 0
        for j in reading :

            found = re.findall("(?s)(?<=CONTENT\=\").*?(?=\" HEIGHT)", j)

        # if "CONTENT=\"" in j and flag == True:
            for item in found :
                # file_to_write.write("   CONTRIB "+str(k)+"    "+str(item)+" ") --> chaque item est bien un mot
                file_to_write.write("  "+str(item)+"  ")

                # k += 1

            # if j.endswith("\"") :
                # flag = False
            file_to_write.write("\n")
