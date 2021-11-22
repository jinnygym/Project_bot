import json

"""testzaza"""
def main():
    """main"""
    # test = ejudgeclass.getstart()
    efwafeaw = []
    search = open("problem.txt","r", encoding="utf8")
    for line in search.readlines():
        efwafeaw.append(json.loads(line.strip()))
    print(efwafeaw[1])
main()
