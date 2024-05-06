# Laboratory Exercise #3: DELA ROSA, SORIANO
# Exception Handling in Laboratoy Activity 2

# For Bonus Item: Import the re module
import re

try: 
    # Open and Read the First File  
    ourFile1 = open("BSCPE1-5.csv", "r")
    lines = ourFile1.readlines()

    # To Extract First Member Data 
    first_member = lines[11]

    # To Extract Second Member Data 
    second_member = lines[46]

    # Open the new file with write permission 
    ourFile2 = open("output.txt","w")

    # First Member Name
    sp1 = first_member.split(",")  # Split parts
    fn1_1 = str((sp1[2][:8].lower()).capitalize())  # First part in first name
    fn2_1 = str((sp1[2][9:].lower()).capitalize())  # Second part in first name
    mi_1 = str((sp1[3][0].lower()).capitalize())  # Middle Initial
    ln1_1 = str((sp1[1][:5].lower()).capitalize())  # First part in last name
    ln2_1 = str((sp1[1][5:].lower()).capitalize())  # Second part in last name
    first_member_name = fn1_1 + " " + fn2_1 + " " + mi_1 + ". " + ln1_1 + ln2_1 # Name of First Member 

    # Second Member Name
    sp2 = second_member.split(",")  # Split parts
    fn1_2 = str((sp2[2][:8].lower()).capitalize())  # First part in first name
    fn2_2 = str((sp2[2][9:].lower()).capitalize())  # Second part in first name
    mi_2 = str((sp2[3][0].lower()).capitalize())  # Middle Initial
    ln = str((sp2[1].lower()).capitalize())  # Last Name 
    second_member_name = fn1_2 + " " + fn2_2 + " " + mi_2 + ". " + ln # Name of Second Member 

    # Parse the info and write it to new file 
    ourFile2.write(
        "FIRST MEMBER\n" +
        "Full name: " + first_member_name + "\n" +
        "Student number: " + sp1[0] + "\n" +
        "Email address: " + sp1[6] + "\n\n" +

        "SECOND MEMBER\n" +
        "Full name: " + second_member_name + "\n" +
        "Student number: " + sp2[0] + "\n" +
        "Email address: " + sp2[6] + "\n"
    )

    # Close the Files 
    ourFile1.close()
    ourFile2.close()

    # Read the cool_man txt file 
    ourFile3 = open("cool_man.txt", "r")
    readFile3 = ourFile3.read()

    # Open the output.txt file and write the cool_man txt
    ourFile2_append = open("output.txt", "a")
    ourFile2_append.write("\n" + readFile3)

    # Close the files 
    ourFile2_append.close() 
    ourFile3.close()

    # BONUS ITEM 

    # Pattern 
    pattern = r',S\w+O,J\w+O'

    # Files with their permissions 
    output_file = open("output.csv", "a")
    input_file = open("BSCPE1-5.csv", "r")

    # Search and append the info 
    for line_num, line in enumerate(input_file, 1):
        try:
            match = re.search(pattern, line)
            if match:
                output_line = f"Found at line {line_num}: {line}"
                output_file.write(output_line)
                break
        except re.error as r:
            print("\nRegex error:", str(r), "\n")
            break

    # Close the Files 
    input_file.close()
    output_file.close()

except FileNotFoundError as f:
    print("\nFile not found:", str(f),"\n")
except PermissionError as p:
    print("\nPermission error:", str(p), "\n")
except IndexError as i:
    print("\nIndex out of range:", str(i),"\n")
except NameError as n:
    print("\nVariable not defined:", str(n),"\n")
except Exception as e:
    print("\nAn error occurred:", str(e),"\n")