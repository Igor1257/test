import wunderpy2
import taskw


class wu:
    client = None

    def __init__(self):
        self.tasks = []
        CLIENT_ID = "73fb97eb7715be852069"
        ACCESS_TOKEN = "927bb36d40cf32fac899da24922e01caee421aa9dfe0b781946c96c33764"
        api = wunderpy2.WunderApi()
        self.client = api.get_client(ACCESS_TOKEN, CLIENT_ID)
        self.projects = self.client.get_lists()
        for project in self.projects:
            for task in self.client.get_tasks(project['id']):
                self.tasks.append(task)

    def get_project_title_by_id(self, pid):
        for project in self.projects:
            if project[u'id'] == pid:
                if project[u'title'] == 'inbox':
                    return ""
                else:
                    return project[u'title']

    def convert_project_title_to_list_id(self, title):
        if title == '':
            title = u'inbox'
        for project in self.projects:
            if project[u'title'] == title:
                return project['list_id']


class tw:
    def __init__(self):
        self.client = taskw.TaskWarrior()
        self.tasks = self.client.load_tasks()

    def get_task_by_wunder_id(self, wunder_id):
        for task in self.tasks['pending']:
            if 'wunder_id' in task.keys():
                if task['wunder_id'] == str(wunder_id):
                    return task


def add_wu_task_2_tw(_wu_task):
    project_name = w.get_project_title_by_id(_wu_task[u'list_id'])
    result = t.client.task_add(
        description=_wu_task[u'title'],
        project=project_name,
        wunder_id=_wu_task[u'id'],
        wunder_revision=_wu_task[u'revision']
    )
    pass


def add_tw_task_2_wu(_tw_task):
    if not _tw_task.has_key('wunder_id'):
        wu.client.client.create_task(
            list_id=wu.convert_project_title_to_list_id(_tw_task['project']),
            title=_tw_task['description']
        )


w = wu()
t = tw()


def update_tw_task(wu_task):
    tw_task = t.get_task_by_wunder_id(wu_task[u'id'])
    if wu_task[u'revision'] > int(tw_task['wunder_revision']):
        tw_task['description'] = wu_task['title']
        tw_task['wunder_revision'] = wu_task['revision']
        t.client.task_update(tw_task)



for wu_task in w.tasks:
    tw_task = t.get_task_by_wunder_id(wu_task[u'id'])
    if not tw_task:
        add_wu_task_2_tw(wu_task)
    else:
        update_tw_task(wu_task)
for tw_task in t.tasks['pending']:
    add_tw_task_2_wu(tw_task)












# for task in t.tasks['pending']:
#     if 'wunder_id' not in task.keys():
#         list_id = w.convert_project_title_to_list_id(task['project'])
#         w.client.create_task(
#             list_id=list_id,
#             title=task['description']
#         )
