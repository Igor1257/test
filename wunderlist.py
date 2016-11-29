# coding=utf-8

import wunderpy2

# inbox 103024398
from wunderpy2 import WunderApi

CLIENT_ID = "73fb97eb7715be852069"
ACCESS_TOKEN = '927bb36d40cf32fac899da24922e01caee421aa9dfe0b781946c96c33764'


class ExtWunderlist(WunderApi):
    def __init__(self):
        WunderApi.__init__(self)
        api = wunderpy2.WunderApi()
        self.client = api.get_client(ACCESS_TOKEN, CLIENT_ID)

    def is_list_exist(self, title):
        for project in self.projects:
            if project[u'title'] == title:
                return True
        return False

    def get_project_id(self, title=u'inbox'):
        for project in self.projects:
            if project[u'title'] == title:
                return project[u'id']
                # TODO: кидать эксепшен если не найден прожект с таким тайтлом

    def get_project_title(self, id):
        for project in self.projects:
            if project[u'id'] == id:
                return project[u'title']
                # TODO: кидать эксепшен если не найден прожект с таким id

    def get_tasks(self):
        result = []
        for project in self.client.get_lists():
            pass
        return result

    def add_task(self):
        pass


w = ExtWunderlist()
uid = w.get_project_id(u'inbox')

'''
def print_lists():
    global lists
    lists = client.get_lists()
    for clist in lists:
        print clist['title']
        print clist['id']


def create_list():
    client.create_list('Test')


def create_task_in_test():
    task = client.create_task(277837973, "My new task", due_date="2015-08-02", starred=True)
    return task


def update_task(task):
    client.update_task(task['id'], task['revision'], title=task['title'] + ' 100')


# task = client.create_task(1234, "My new task", due_date="2015-08-02", starred=True)
# client.create_note(task[wunderpy2.Task.ID], "My note")
# client.create_subtask(task[wunderpy2.Task.ID], "My subtask")

pass
'''
