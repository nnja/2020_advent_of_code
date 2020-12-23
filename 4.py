from util import *

data = get_data(4, split=False)

def create_passports(data):
    passports = []
    lines = data.split("\n\n")

    for line in lines:        
        passport = {}
        entries = line.split()
        for entry in entries:
            k, v = entry.split(":")
            passport[k] = v
        passports.append(passport)
    return passports

def p1(data):

    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    optional = {"cid"}

    passports = create_passports(data)
    num_valid = 0
    for passport in passports:
        valid = True    
        for field in required:
            if field not in passport.keys():
                valid = False
        num_valid += valid
    return num_valid

byr = lambda x: len(x) == 4 and int(x) >= 1920 and int(x) <= 2002
iyr = lambda x: len(x) == 4 and int(x) >= 2010 and int(x) <= 2020
eyr = lambda x: len(x) == 4 and int(x) >= 2020 and int(x) <= 2030

def hgt(x):
    if x.endswith("cm"):
        val = x.replace("cm", "")
        if not val.isdigit():
            return False
        num = int(val)
        if num >= 150 and num <= 193:
            return True
    if x.endswith("in"):
        val = x.replace("in", "")
        if not val.isdigit():
            return False
        num = int(val)
        if num >= 59 and num <= 76:
            return True
    return False

hcl = lambda x: re.search(r'#[0-9a-fA-F]{6}', x)
ecl = lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
pid = lambda x: len(x) == 9 and x.isdigit()

def p2(data):
    num_valid = 0
    passports = create_passports(data)

    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    optional = {"cid"}

    passports = create_passports(data)
    num_valid = 0
    for passport in passports:
        valid = True    
        for field in required:
            if field not in passport.keys() or not globals()[field](passport[field]):
                valid = False
        num_valid += valid
    return num_valid




def test():

    data = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

    data2 = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

    data3 = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

    run_tests(p1, [(data, 2)], delim=None)
    # run_tests(p2, [(data2, 0)], delim=None)
    run_tests(p2, [(data3, 4)], delim=None)


test()
print("Result1:", p1(data))
print("Result2:", p2(data))