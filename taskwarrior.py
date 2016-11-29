from taskw import TaskWarrior
import task

class ExtTaskWarrior(TaskWarrior):
    def __init__(self):
        TaskWarrior.__init__(self)
        self.tasks = self.load_tasks()




    def get_tasks_wo_wunderlist_id(self):
        result = []
        for task in self.tasks['pending']:
            if not 'wunder_id' in task:
                result.append(task)
        return result

    def get_task_by_wunder_id(self, wunder_id):
        for task in self.tasks['pending']:
            if 'wunder_id' in task.keys():
                if task['wunder_id'] is wunder_id:
                    return task
        return None

    def update_task(self, uuid, wunder_id, wunder_revision):
        id, task = self.get_task(uuid=uuid)
        task['wunder_id'] = wunder_id
        task['wunder_revision'] = wunder_revision
        self.task_update(task)
        pass
