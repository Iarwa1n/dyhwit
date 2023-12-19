from typing import Optional
from rich import print_json
from rich import print

from dyhwit.task import Quest
import typer
from getpass import getpass, getuser

cli = typer.Typer()

@cli.command()
def noop():
    print("noop")
    
@cli.command()
def quest(
    file_to_quest: str
):
    # load quest from quest json
    quest = Quest.load_from_json(file_to_quest)
    for task in quest.get_tasks():
        print(task.task)
        for choice in task.get_randomized_choices():
            print(choice)
        answer = input("Answer: ")
        quest.answer(task, answer)
        print("")
    print("Quest finished!")
    print(f"Correct answers: {quest._correct_answers}")
def run_cli():
    cli()


if __name__ == "__main__":
    run_cli()
