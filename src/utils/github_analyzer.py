
from github import Github

class GithubAnalyzer:
    def __init__(self, token):
        self.github = Github(token)

    def analyze_repo(self, repo_name):
        repo = self.github.get_repo(repo_name)
        files = repo.get_contents("")
        file_list = []
        for file in files:
            file_list.append(file.path)
        return file_list
