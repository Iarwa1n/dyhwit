import random
import json

class Task():
    pass

class MultipleChoiceTask(Task):
    def __init__(self, task:str, choices:list, correct_choice:str):
        self._task = task    
        self._choices = choices
        self._correct_choice = correct_choice

    def check(self, choice):
        print(choice, self._correct_choice)
        return choice == self._correct_choice
    
    def get_randomized_choices(self):
        randomized_choices = self._choices.copy()
        random.shuffle(randomized_choices)
        return randomized_choices
    
    @property
    def task(self):
        return self._task
    

class Quest():
    def __init__(self, tasks:[Task]):
        self._tasks = tasks
        self._correct_answers = 0
        self._incorrect_answers = 0
        self._progress = []

    def get_tasks(self):
        return self._tasks

    def get_tasks_left(self):
        return len(self._tasks) - len(self._progress)
    
    def answer(self, task, answer):
        if task not in self._tasks:
            raise ValueError("Task not in quest")
        
        if task.check(answer):
            self._correct_answers += 1
        else:
            self._incorrect_answers += 1
 
    @staticmethod
    def load_from_json(file_to_quest):
        with open(file_to_quest) as f:
            #string = f.read()
            data = json.load(f)
        result = []
        for tasks in data:
            result.append(MultipleChoiceTask(tasks["task"], tasks["choices"], tasks["correct_choice"]))
        return Quest(result)
      
