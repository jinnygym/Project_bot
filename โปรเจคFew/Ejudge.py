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
            'Cookie': '_hjid=a38f6863-6a5c-4d88-bd28-ae00aa2845aa; _ga_KC6DWQ6BQ1=GS1.1.1630639901.4.1.1630639944.0; _ga_TL3MKTGGKJ=GS1.1.1630869230.4.0.1630869230.0; _ga=GA1.1.1782557095.1627896882; _ga_7BJDLT59DV=GS1.1.1636702090.16.1.1636704657.0; remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6IlVaQ1NmeHEyTXQ0Y3NXZ0ZvcEkwSWc9PSIsInZhbHVlIjoiMHBFZG9tM0FEb0JcL2tlYWJEOGdzSEVPM3JMQU80T0RwWGl1MWJpd1E3ZVJoNUhia3gyQlYyMFk4ZnhsTmk5dHZTTHI4aVFBMVpiZm1rak84ZG4rVW5QUDU5aXZIUkFNQ3dzc0VJa2MwYXc0PSIsIm1hYyI6ImE3ZjhiMGM4NjhjNTUwNDdjY2UzYmEzZmZkYTQ3NTNlM2YyYjA4ZWJiZTU3NTcyZjAwMTIwYjY5MjZhYzQyYjIifQ%3D%3D; __ejudge=eyJpdiI6Ilc5M05tRXdGQ2dQUWVkbzFYVHdLYWc9PSIsInZhbHVlIjoiS1BvQjI3VFN6U1M2MDN4djZ2U2JQZzl5bmhoR0FybW1xenRNY1RabjVpTVg3NVcySjVjRjhvOTRTYXQ3bUJnUmt3Y3NHSGM5Rzk0d2VOTHBnNlNadEE9PSIsIm1hYyI6ImU3OGY0ZGE4OTU2ZmUwY2Q1YjFkMGYwZTcxNzY4NmY1NjkwMjkzOWNmMWY1NTM3NjMwNmM4MmNlZWM5YWY0NTgifQ%3D%3D'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text

    def entercourse():
        ejudgeclass.requestget("https://ejudge.it.kmitl.ac.th/course/161/enter")

    def getstart():  
        result = ejudgeclass.requestget("https://ejudge.it.kmitl.ac.th/course/161/leaderboard")
        test2 = ejudgeclass.cutstring("<tbody>", '</tbody>', result)[0]
        test3 = ejudgeclass.cutstring("<tr>", "</tr>", test2)
        resff = []
        for res in test3:
            fezaw = ejudgeclass.cutstring("<td>", "</td>", res)
            fewspan = ejudgeclass.cutstring(">", "<", fezaw[2])
            fewtest = ejudgeclass.cutstring('href="', '">', fezaw[1])
            score = ejudgeclass.cutstring('<td >', '</td>', res)
            resff.append({'profile': fewtest[0].strip(), 'studentid': fewspan[0].strip(), 'name': fezaw[3].strip(), 'problem_score': score[0].strip(), 'quiz_score': score[1].strip(), 'total_score': score[2].strip()})
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
        search = open(file,"r", encoding="utf8")
        for line in search.readlines():
            fewf = str(json.loads(line.strip())["problem"]).strip()
            if fewf == problem:
                print(fewf)
                booleanfew = True
                return booleanfew
        return booleanfew

    def golink(link, page):
        if page == 1:
            result = ejudgeclass.requestget("%s&problemPage=1" %(link))
            test2 = ejudgeclass.cutstring("<tbody>", '</tbody>', result)[1]
            test3 = ejudgeclass.cutstring("<tr>", "</tr>", test2)
            resff = []
            for res in test3:
                fezaw = ejudgeclass.cutstring("<td>", "</td>", res)
                problem = ejudgeclass.cutstring('">', "</a>", fezaw[2])
                course = ejudgeclass.cutstring('">', "</a>", fezaw[1])
                star = ejudgeclass.cutstring('<i class="fas fa-star">', "</i>", fezaw[3])
                status = "Not Pass"
                if fezaw[4].count("Not Pass") >= 1:
                    status = "Not Pass"
                else:
                    status = "Pass"
                resff.append({'course': course[0].strip(), 'problem': problem[0].strip(), 'star': len(star), 'status': status.strip()})
        elif page > 1:
            resff = []
            for i in range(1, page+1):
                print("%s&problemPage=%s" %(link, str(i)))
                result = ejudgeclass.requestget("%s?problemPage=%s" %(link, str(i)))
                test2 = ejudgeclass.cutstring("<tbody>", '</tbody>', result)[1]
                test3 = ejudgeclass.cutstring("<tr>", "</tr>", test2)
                for res in test3:
                    fezaw = ejudgeclass.cutstring("<td>", "</td>", res)
                    problem = ejudgeclass.cutstring('">', "</a>", fezaw[2])
                    course = ejudgeclass.cutstring('">', "</a>", fezaw[1])
                    star = ejudgeclass.cutstring('<i class="fas fa-star">', "</i>", fezaw[3])
                    status = "Not Pass"
                    if fezaw[4].count("Not Pass") >= 1:
                        status = "Not Pass"
                    else:
                        status = "Pass"
                    resff.append({'course': course[0].strip(), 'problem': problem[0].strip(), 'star': len(star), 'status': status.strip()})
        return resff