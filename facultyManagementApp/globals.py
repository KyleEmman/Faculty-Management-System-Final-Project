from facultyManagementApp.models import Log

departmentList = (
    ('CAFA','College of Architecture and Fine Arts (CAFA)'),
    ('CAL','College of Arts and Letters (CAL)'),
    ('CBA','College of Business Administration (CBA)'),
    ('CCJE','College of Criminal Justice Education (CCJE)'),
    ('CHTM','College of Hospitality and Tourism Management (CHTM)'),
    ('CICT','College of Information and Communications Technology (CICT)'),
    ('CIT','College of Industrial Technology (CIT)'),
    ('CLaw','College of Law (CLaw)'),
    ('CON','College of Nursing (CON)'),
    ('COE','College of Engineering (COE)'),
    ('COED','College of Education (COED)'),
    ('CS','College of Science (CS)'),
    ('CSER','College of Sports, Exercise and Recreation (CSER)'),
    ('CSSP','College of Social Sciences and Philosophy (CSSP)'),
    ('GS','Graduate School (GS)'),
)
userLevelList = (
    ('1','Faculty'),
    ('2','Department Head'),
    ('3','Research Coordinator'),
    ('4','Extension Coordinator'),
)

def getTemplate(userLevel):
    if userLevel == 1:
        return "layouts/faculty.html"
    elif userLevel == 2:
        return "layouts/deptHead.html"
    elif userLevel == 3:
        return "layouts/resCoord.html"
    elif userLevel == 4:
        return "layouts/extCoord.html"
    else:
        return "layouts/admin.html"

def addLog(name, activity):
    log = Log(
        name = name,
        activity = activity
    )
    log.save()