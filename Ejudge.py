import requests
import json


class ejudgeclass:

    def cutstring(start, to, adata):
        res = []
        result1 = adata.split(start)
        for value in result1:
            res.append(value.split(to)[0])
        del res[0]
        return res

    def requestget(url):
        payload, headers = {}, {
            'Cookie': '_hjid=28ae9c21-e0bd-4ec6-972e-2581c23c0b73; _ga=GA1.1.465663323.1625084564; _ga_TL3MKTGGKJ=GS1.1.1631642750.15.0.1631642750.0; _ga_7BJDLT59DV=GS1.1.1636722089.2.0.1636722089.0; remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6IlBreW5hSlFuSmlTVG9lRm56bkk2MkE9PSIsInZhbHVlIjoiMnQ5NTBIbGE5VDI4SFNDbVh1WXV3SVN0NHhnamRwQ2YyVWNITTFiVDZoSkNmOGpFQjBuc1VlZ0JTRkd4SHBOUnZaeW5TbzNMNXdlaFRDZkJhb0dQMzlSUVA1TUNoeDNDWnp4aHBxVkszVjQ9IiwibWFjIjoiNjJkMDFlNzc5MGE5OWU5ZWFmZTU1NGQ2MjY5NTYzNDljMmQwNjNhODRhMmQ3MTFkYThiNmY4MjZjZTE0N2VmZiJ9; __ejudge=eyJpdiI6IjRucXAwM1FwVzBXSzFNOG0rTEREekE9PSIsInZhbHVlIjoiQk9FMVVVNE1MRWJNdk1udlhWSlJDaVJSMElrZjhONFNUbEhvdXh3ZlRnbkg4bjVjMGV0ZWlWc1ZteGxrdmdaUTQyR2NzbUdWTjBpVFAxWmlWcXFRRnc9PSIsIm1hYyI6IjJhZTkzNDJiZmI1ZDJjZmYyMWIyOGQ2NWRjNGE5OWRkMjRiZTQxZDI0ZThlYTI2YjI3YjQ5MmU3MmEzM2QyNWIifQ%3D%3D'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text

    def entercourse():
        ejudgeclass.requestget(
            "https://ejudge.it.kmitl.ac.th/course/161/enter")

    def getstart():
        result = ejudgeclass.requestget(
            "https://ejudge.it.kmitl.ac.th/course/161/leaderboard")
        test2 = ejudgeclass.cutstring("<tbody>", '</tbody>', result)[0]
        test3 = ejudgeclass.cutstring("<tr>", "</tr>", test2)
        resff = []
        for res in test3:
            fezaw = ejudgeclass.cutstring("<td>", "</td>", res)
            fewspan = ejudgeclass.cutstring(">", "<", fezaw[2])
            fewtest = ejudgeclass.cutstring('href="', '">', fezaw[1])
            score = ejudgeclass.cutstring('<td >', '</td>', res)
            resff.append({'profile': fewtest[0].strip(), 'studentid': fewspan[0].strip(), 'name': fezaw[3].strip(
            ), 'problem_score': score[0].strip(), 'quiz_score': score[1].strip(), 'total_score': score[2].strip()})
        return resff

    def findejudge(keyword):
        few = ejudgeclass.getstart()
        index = -1
        response = {}
        for i in range(len(few)):
            if few[i]["name"].count(keyword) >= 1 or few[i]["studentid"].count(keyword) >= 1:
                index = i
                break
        if index == -1:
            response["status"] = "error"
            response['message'] = 'Not Found'
        else:
            response["status"] = "success"
            response['data'] = few[index]
        return response

    def checkfile(problem, file):
        booleanfew = False
        search = open(file, "r", encoding="utf8")
        for line in search.readlines():
            fewf = str(json.loads(line.strip())["problem"]).strip()
            if fewf == problem:
                print(fewf)
                booleanfew = True
                return booleanfew
        return booleanfew

    def golink(link, page):
        if page == 1:
            result = ejudgeclass.requestget("%s&problemPage=1" % (link))
            test2 = ejudgeclass.cutstring("<tbody>", '</tbody>', result)[1]
            test3 = ejudgeclass.cutstring("<tr>", "</tr>", test2)
            resff = []
            for res in test3:
                fezaw = ejudgeclass.cutstring("<td>", "</td>", res)
                problem = ejudgeclass.cutstring('">', "</a>", fezaw[2])
                course = ejudgeclass.cutstring('">', "</a>", fezaw[1])
                star = ejudgeclass.cutstring(
                    '<i class="fas fa-star">', "</i>", fezaw[3])
                status = "Not Pass"
                if fezaw[4].count("Not Pass") >= 1:
                    status = "Not Pass"
                else:
                    status = "Pass"
                resff.append({'course': course[0].strip(), 'problem': problem[0].strip(
                ), 'star': len(star), 'status': status.strip()})
        elif page > 1:
            resff = []
            for i in range(1, page+1):
                print("%s&problemPage=%s" % (link, str(i)))
                result = ejudgeclass.requestget(
                    "%s?problemPage=%s" % (link, str(i)))
                test2 = ejudgeclass.cutstring("<tbody>", '</tbody>', result)[1]
                test3 = ejudgeclass.cutstring("<tr>", "</tr>", test2)
                for res in test3:
                    fezaw = ejudgeclass.cutstring("<td>", "</td>", res)
                    problem = ejudgeclass.cutstring('">', "</a>", fezaw[2])
                    course = ejudgeclass.cutstring('">', "</a>", fezaw[1])
                    star = ejudgeclass.cutstring(
                        '<i class="fas fa-star">', "</i>", fezaw[3])
                    status = "Not Pass"
                    if fezaw[4].count("Not Pass") >= 1:
                        status = "Not Pass"
                    else:
                        status = "Pass"
                    resff.append({'course': course[0].strip(), 'problem': problem[0].strip(
                    ), 'star': len(star), 'status': status.strip()})
        return resff
