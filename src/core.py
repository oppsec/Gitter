import requests

from urllib3 import disable_warnings
disable_warnings()

from rich import print
from src.messages import input_name, error, success

class Account:
    def __init__(self, name, url, repos, gists, followers, following) -> None:
        self.name = name
        self.url = url
        self.repos = repos
        self.gists = gists
        self.followers = followers
        self.following = following


def get_username() -> None:
    """ Define Github account name """
    username_input = input(input_name)
    connect(username_input)


def connect(username_input) -> None:
    """
    Connect to the GitHub API and
    confirm if the account exists
    """
    github_api_url = f'https://api.github.com/users/{username_input}'
    response = requests.get(github_api_url, verify=False, timeout=10, allow_redirects=False)

    get_information(response) if response.status_code == 200 else print(error)


def get_information(response) -> None:
    """ Capture the JSON response and get the account informations """
    print(success)

    dump = response.json()
    account = Account(dump['login'], dump['html_url'], dump['public_repos'], dump['public_gists'], dump['followers'], dump['following'])
    
    result(account)


def result(account) -> str:
    """ Returns the informations """
    
    print(f"""[bold yellow]
* Account Name: {account.name}
* Account URL: {account.url}
* Account Public Repositories: {account.repos}
* Account Public Gists: {account.gists}
* Account Followers: {account.followers}
* Account Following: {account.following}
    [/]""")