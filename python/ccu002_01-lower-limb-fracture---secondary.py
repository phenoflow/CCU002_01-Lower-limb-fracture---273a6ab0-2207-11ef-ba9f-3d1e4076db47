# Rochelle Knight, Venexia Walker, et al., 2024.

import sys, csv, re

codes = [{"code":"S828","system":"icd10"},{"code":"S827","system":"icd10"},{"code":"S823","system":"icd10"},{"code":"S921","system":"icd10"},{"code":"S822","system":"icd10"},{"code":"S922","system":"icd10"},{"code":"S829","system":"icd10"},{"code":"S824","system":"icd10"},{"code":"S820","system":"icd10"},{"code":"S923","system":"icd10"},{"code":"S826","system":"icd10"},{"code":"S927","system":"icd10"},{"code":"S825","system":"icd10"},{"code":"S929","system":"icd10"},{"code":"S920","system":"icd10"},{"code":"S821","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_01-lower-limb-fracture-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_01-lower-limb-fracture---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_01-lower-limb-fracture---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_01-lower-limb-fracture---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
