from github import Github  ## http://pygithub.readthedocs.io/en/latest/index.html
import keyring
import base64

username = keyring.get_password("github", "username")
password = keyring.get_password("github", "password")

g = Github(username, password)

# get repo by name
repo = g.get_user().get_repo('repo-name')

# read file from repo
file_content = repo.get_file_contents('file_path')
decoded_content = base64.b64decode(file_content.content)

# store file to github
repo.create_file('/file-path', 'message', 'file-content')
