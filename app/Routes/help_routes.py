import json
from typing import Dict

from flask import Blueprint, abort, request

from db_connector import DBConnector

hr = Blueprint('hr', __name__)


@hr.route('help', methods=['POST'])
def help():
    """
    Returns all the help commands and explains their function.
    :return: str
    """

    returnstring = "1. Help with team commands " \
                   "2. Help with project commands" \
                   "3. Help with user commands" \
                   "4. Help with manager commands" \
                   "5. Show all commands" \
                   "Use /specific_help [number] to get help"

    return returnstring


@hr.route('specific_help', methods=['POST'])
def specific_help():
    """
    This is a function similar to a switch case function
    Its purpose is to be able to print all of the different strings
    :return:
    """
    # loads payload as json then converts it to a dictionary
    req = request.form

    # this is the switcher function that switches the 4 different cases and returns their string
    switcher = {
        1: "Team Help" \
           "/ma-team-create [name] Create a team with a specified name"
           "/ma-team-update [name] [new name] Update a teams name"
           "/ma-team-delete [name] Deletes the specified team"
           "/ma-team-join [name] Join a specific team"
           "/ma-teams Shows all available teams",
        2: "Project Help "
           "/ma-project-create [name] Create a project with a specified name"
           "/ma-project-update [name] [new name] Update a projects name"
           "/ma-project-delete [name] Deletes the specified project"
           "/ma-project-join [name] Join a specific project"
           "/ma-projects Shows all your projects",
        3: "User Help"
           "/ma-status View information about yourself"
           "/ma-track Toggle tracking the time you spend working",
        4: "Manager Help"
           "/ma-m-status View the status of all users"
           "/ma-m-move [name of user] [name of new team] Move user to a new team",
        5: "Show all commands"
           "/ma-team-create [name] Create a team with a specified name"
           "/ma-team-update [name] [new name] Update a teams name"
           "/ma-team-delete [name] Deletes the specified team"
           "/ma-team-join [name] Join a specific team"
           "/ma-teams Shows all available teams"
           "/ma-project-create [name] Create a project with a specified name"
           "/ma-project-update [name] [new name] Update a projects name"
           "/ma-project-delete [name] Deletes the specified project"
           "/ma-project-join [name] Join a specific project"
           "/ma-projects Shows all your projects"
           "/ma-status View information about yourself"
           "/ma-track Toggle tracking the time you spend working"
           "/ma-m-status View the status of all users"
           "/ma-m-move [name of user] [name of new team] Move user to a new team"
    }
    # Prints the function
    func = switcher.get(req['text'])

    return func()
