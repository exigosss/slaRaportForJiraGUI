from tkinter import *
from tkinter import ttk, Toplevel
from atlassian import ServiceManagement
from atlassian import Jira


root = Tk()
root.title("JIRA SLA Report")

def createReport(uri, auth, filter):
    SD = ServiceManagement(
        url = uri,
        token = auth
    )
    JIRA = Jira(
        url = uri,
        token = auth
    )
    data = JIRA.jql_get_list_of_tickets(
    jql=filter
    )

    result = ''
    issueKeys = []
    for i in data:
        sla = SD.get_sla(i['key'])
        result = result + '\n'
        result = result + i['key'] + ' | ' + i['fields']['summary'] + ' | ' + i['fields']['assignee']['displayName']
        for s in sla:
            if 'ongoingCycle' in s.keys():
                result = result + '\n'
                result = result + s['name'] + '\n'
                result = result + '# Start Time: ' + s['ongoingCycle']['startTime']['friendly'] + '\n'
                result = result + '# Goal: ' + s['ongoingCycle']['goalDuration']['friendly'] + '\n'
                result = result + '# Elapsed: ' + s['ongoingCycle']['elapsedTime']['friendly'] + '\n'
            elif 'completedCycles' in s.keys():
                for c in s['completedCycles']:
                    result = result + '\n'
                    result = result + s['name'] + '\n'
                    result = result + '# Start Time: ' + c['startTime']['friendly'] + '\n'
                    result = result + '# Goal: ' + c['goalDuration']['friendly'] + '\n'
                    result = result + '# Elapsed: ' + c['elapsedTime']['friendly'] + '\n'
    return result

def showResults(*args):
    jql = str(jqlQuery.get())
    userPat = str(pat.get())
    uri = str(url.get())

    rootResult = Toplevel(root)
    rootResult.title("SLA Report Result")
    Label(rootResult, text = createReport(uri, userPat, jql)).pack()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Please provide JIRA URL").grid(column=1, row=1, sticky=N)
url = StringVar()
url_entry = ttk.Entry(mainframe, width=30, textvariable=url)
url_entry.grid(column=1, row=2, sticky=S)

ttk.Label(mainframe, text="Please provide PAT").grid(column=1, row=3, sticky=N)
pat = StringVar()
pat_entry = ttk.Entry(mainframe, width=30, textvariable=pat, show='*')
pat_entry.grid(column=1, row=4, sticky=S)

ttk.Label(mainframe, text="Please provide JQL filter for SLA report").grid(column=1, row=5, sticky=N)
jqlQuery = StringVar()
jqlQuery_entry = ttk.Entry(mainframe, width=30, textvariable=jqlQuery)
jqlQuery_entry.grid(column=1, row=6, sticky=S)

ttk.Button(mainframe, text="Show", command=showResults).grid(column=1, row=7, sticky=S)

mainloop()