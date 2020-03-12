import csv

with open("D:\\OneDrive\\Jugando con Python\\Practicas\\csv\\contacts.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("D:\\OneDrive\\Jugando con Python\\Practicas\\csv\\new_contacts.csv", "w", newline="") as new_file:
        fieldnames = ["Name", "Phone 1 - Value",
                      "Phone 2 - Value", "Phone 3 - Value"]

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter="\t")

        csv_writer.writeheader()

        keys_want = ["Name", "Phone 1 - Value",
                     "Phone 2 - Value", "Phone 3 - Value"]

        for line in csv_reader:
            #del line["Name","Given Name","Additional Name","Family Name","Yomi Name","Given Name Yomi","Additional Name Yomi","Family Name Yomi","Name Prefix","Name Suffix","Initials","Nickname","Short Name","Maiden Name","Birthday","Gender","Location","Billing Information","Directory Server","Mileage","Occupation","Hobby","Sensitivity","Priority","Subject","Notes","Language","Photo","Group Membership","E-mail 1 - Type","E-mail 1 - Value","E-mail 2 - Type","E-mail 2 - Value","Phone 1 - Type","Phone 1 - Value","Phone 2 - Type","Phone 2 - Value","Phone 3 - Type","Phone 3 - Value","Address 1 - Type","Address 1 - Formatted","Address 1 - Street","Address 1 - City","Address 1 - PO Box","Address 1 - Region","Address 1 - Postal Code","Address 1 - Country","Address 1 - Extended Address","Address 2 - Type","Address 2 - Formatted","Address 2 - Street","Address 2 - City","Address 2 - PO Box","Address 2 - Region","Address 2 - Postal Code","Address 2 - Country","Address 2 - Extended Address","Organization 1 - Type","Organization 1 - Name","Organization 1 - Yomi Name","Organization 1 - Title","Organization 1 - Department","Organization 1 - Symbol","Organization 1 - Location","Organization 1 - Job Description","Website 1 - Type","Website 1 - Value","Jot 1 - Type","Jot 1 - Value"]
            #{k:v for k, v in bigDict.items() if k in ('l', 'm', 'n')}
            result = {key: value for key,
                      value in line.items() if key in keys_want}
            csv_writer.writerow(result)
            print(result)
