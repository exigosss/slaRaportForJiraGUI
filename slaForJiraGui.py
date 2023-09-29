from tkinter import *
from tkinter import ttk, Toplevel
from atlassian import ServiceManagement
from atlassian import Jira


root = Tk()
root.geometry('300x250')
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
    breachedIssues = []
    if slaBreached.get() == 1:
        for i in data:
            sla = SD.get_sla(i['key'])
            for s in sla:
                if 'ongoingCycle' in s.keys():
                    if s['ongoingCycle']['breached'] == TRUE and s['name'] != 'Time to close after resolution':
                        if i not in breachedIssues:
                            breachedIssues.append(i)
                elif 'completedCycles' in s.keys():
                    for c in s['completedCycles']:
                        if c['breached'] == TRUE and s['name'] != 'Time to close after resolution':
                            if i not in breachedIssues:
                                breachedIssues.append(i)
        for i in breachedIssues:
            sla = SD.get_sla(i['key'])
            if sla:
                result = result + '\n\n'
                result = result + i['key'] + ' | ' + i['fields']['summary'] + ' | ' + i['fields']['assignee']['displayName']
            for s in sla:
                if 'ongoingCycle' in s.keys():
                    if slaBreached.get() == 1 and s['ongoingCycle']['breached'] == TRUE and s['name'] != 'Time to close after resolution':
                        result = result + '\n'
                        result = result + s['name'] + '\n'
                        result = result + '# ONGOING\n'
                        result = result + '# Start Time: ' + s['ongoingCycle']['startTime']['friendly'] + '\n'
                        result = result + '# Goal: ' + s['ongoingCycle']['goalDuration']['friendly'] + '\n'
                        result = result + '# Elapsed: ' + s['ongoingCycle']['elapsedTime']['friendly'] + '\n'
                        result = result + '# Paused: ' + str(s['ongoingCycle']['paused']) + '\n'
                        result = result + '# Breached: ' + str(s['ongoingCycle']['breached']) + '\n'
                    elif slaBreached.get() == 0:
                        result = result + '\n\n'
                        result = result + s['name'] + '\n'
                        result = result + '# ONGOING\n'
                        result = result + '# Start Time: ' + s['ongoingCycle']['startTime']['friendly'] + '\n'
                        result = result + '# Goal: ' + s['ongoingCycle']['goalDuration']['friendly'] + '\n'
                        result = result + '# Elapsed: ' + s['ongoingCycle']['elapsedTime']['friendly'] + '\n'
                        result = result + '# Paused: ' + str(s['ongoingCycle']['paused']) + '\n'
                        result = result + '# Breached: ' + str(s['ongoingCycle']['breached']) + '\n'
                elif 'completedCycles' in s.keys():
                    for c in s['completedCycles']:
                        if slaBreached.get() == 1 and c['breached'] == TRUE and s['name'] != 'Time to close after resolution':
                            result = result + '\n'
                            result = result + s['name'] + '\n'
                            result = result + '# COMPLETED\n'
                            result = result + '# Start Time: ' + c['startTime']['friendly'] + '\n'
                            result = result + '# Goal: ' + c['goalDuration']['friendly'] + '\n'
                            result = result + '# Elapsed: ' + c['elapsedTime']['friendly'] + '\n'
                            result = result + '# Breached: ' + str(c['breached']) + '\n'
                        elif slaBreached.get() == 0:
                            result = result + '\n'
                            result = result + s['name'] + '\n'
                            result = result + '# COMPLETED\n'
                            result = result + '# Start Time: ' + c['startTime']['friendly'] + '\n'
                            result = result + '# Goal: ' + c['goalDuration']['friendly'] + '\n'
                            result = result + '# Elapsed: ' + c['elapsedTime']['friendly'] + '\n'
                            result = result + '# Breached: ' + str(c['breached']) + '\n'
    elif slaBreached.get() == 0:
        for i in data:
            sla = SD.get_sla(i['key'])
            if sla:
                result = result + '\n\n'
                result = result + i['key'] + ' | ' + i['fields']['summary'] + ' | ' + i['fields']['assignee']['displayName']
            for s in sla:
                if 'ongoingCycle' in s.keys():
                    if slaBreached.get() == 1 and s['ongoingCycle']['breached'] == TRUE and s['name'] != 'Time to close after resolution':
                        result = result + '\n'
                        result = result + s['name'] + '\n'
                        result = result + '# ONGOING\n'
                        result = result + '# Start Time: ' + s['ongoingCycle']['startTime']['friendly'] + '\n'
                        result = result + '# Goal: ' + s['ongoingCycle']['goalDuration']['friendly'] + '\n'
                        result = result + '# Elapsed: ' + s['ongoingCycle']['elapsedTime']['friendly'] + '\n'
                        result = result + '# Paused: ' + str(s['ongoingCycle']['paused']) + '\n'
                        result = result + '# Breached: ' + str(s['ongoingCycle']['breached']) + '\n'
                    elif slaBreached.get() == 0:
                        result = result + '\n'
                        result = result + s['name'] + '\n'
                        result = result + '# ONGOING\n'
                        result = result + '# Start Time: ' + s['ongoingCycle']['startTime']['friendly'] + '\n'
                        result = result + '# Goal: ' + s['ongoingCycle']['goalDuration']['friendly'] + '\n'
                        result = result + '# Elapsed: ' + s['ongoingCycle']['elapsedTime']['friendly'] + '\n'
                        result = result + '# Paused: ' + str(s['ongoingCycle']['paused']) + '\n'
                        result = result + '# Breached: ' + str(s['ongoingCycle']['breached']) + '\n'
                elif 'completedCycles' in s.keys():
                    for c in s['completedCycles']:
                        if slaBreached.get() == 1 and c['breached'] == TRUE and s['name'] != 'Time to close after resolution':
                            result = result + '\n'
                            result = result + s['name'] + '\n'
                            result = result + '# COMPLETED\n'
                            result = result + '# Start Time: ' + c['startTime']['friendly'] + '\n'
                            result = result + '# Goal: ' + c['goalDuration']['friendly'] + '\n'
                            result = result + '# Elapsed: ' + c['elapsedTime']['friendly'] + '\n'
                            result = result + '# Breached: ' + str(c['breached']) + '\n'
                        elif slaBreached.get() == 0:
                            result = result + '\n'
                            result = result + s['name'] + '\n'
                            result = result + '# COMPLETED\n'
                            result = result + '# Start Time: ' + c['startTime']['friendly'] + '\n'
                            result = result + '# Goal: ' + c['goalDuration']['friendly'] + '\n'
                            result = result + '# Elapsed: ' + c['elapsedTime']['friendly'] + '\n'
                            result = result + '# Breached: ' + str(c['breached']) + '\n'        
    return result
def showResults(*args):
    #get user input
    jql = str(jqlQuery.get())
    userPat = str(pat.get())
    uri = str(url.get())
    #create new window
    rootResult = Toplevel(root)
    rootResult.geometry('900x800')
    rootResult.title("SLA Report Result")
    #create scrollbar
    h = Scrollbar(rootResult, orient='vertical')
    h.pack(side = RIGHT, fill=Y)
    #create text for result
    t = Text(rootResult, height=55, width=35, yscrollcommand=h.set)
    t.insert(END, createReport(uri, userPat, jql))
    t.pack( side=TOP, fill=X)
    h.config(command=t.yview)

#mainframe = ttk.Frame(root)
#mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)

l1 = ttk.Label(root, text="\nPlease provide JIRA URL")#.grid(column=1, row=1, sticky=N)
url = StringVar()
url_entry = ttk.Entry(root, width=45, textvariable=url)
#url_entry.grid(column=1, row=2, sticky=S)
l1.pack()
url_entry.pack()

l2 = ttk.Label(root, text="\nPlease provide PAT")#.grid(column=1, row=3, sticky=N)
pat = StringVar()
pat_entry = ttk.Entry(root, width=45, textvariable=pat, show='*')
#pat_entry.grid(column=1, row=4, sticky=S)
l2.pack()
pat_entry.pack()

l3 = ttk.Label(root, text="\nPlease provide JQL filter for SLA report")#.grid(column=1, row=5, sticky=N)
jqlQuery = StringVar()
jqlQuery_entry = ttk.Entry(root, width=45, textvariable=jqlQuery)
l3.pack()
jqlQuery_entry.pack()
#jqlQuery_entry.grid(column=1, row=6, sticky=S)

slaBreached = IntVar()
c = Checkbutton(root,
                variable=slaBreached,
                text='Show only breached SLA',
                onvalue=1,
                offvalue=0)
#c.grid(column=1,
#       row=7)
c.pack()

b = ttk.Button(root,
           text="Show",
           command=showResults)
b.pack()

mainloop()