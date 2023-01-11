from django.shortcuts import redirect
import re
FACULTYREGEX = r"^/faculty/"
FACULTY = re.compile(FACULTYREGEX)

DEPTHEADREGEX = r"^/departmentHead/"
DEPTHEAD = re.compile(DEPTHEADREGEX)

RESCOORDREGEX = r"^/researchCoordinator/"
RESCOORD = re.compile(RESCOORDREGEX)

EXTCOORDREGEX = r"^/extensionCoordinator/"
EXTCOORD = re.compile(EXTCOORDREGEX)


        # ('1','Faculty'),
        # ('2','Department Head'),
        # ('3','Research Coordinator'),
        # ('4','Extension Coordinator'),

class FacultyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self,request):
        user = request.user
        response = self.get_response(request)
        resultFac = FACULTY.match(request.path)
        resultDept = DEPTHEAD.match(request.path)
        resultRes = RESCOORD.match(request.path)
        resultExt = EXTCOORD.match(request.path)

        if resultFac:
            if request.user.is_authenticated:
                if user.userLevel != 1:
                    pass
        elif resultDept:
            if request.user.is_authenticated:
                if user.userLevel != 2:
                    pass
        elif resultRes:
            if request.user.is_authenticated:
                if user.userLevel != 3:
                    pass
        elif resultExt:
            if request.user.is_authenticated:
                if user.userLevel != 4:
                    pass
        return response
