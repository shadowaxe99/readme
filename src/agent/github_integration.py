
import requests
from github import Github

class GithubIntegration:
    def __init__(self, access_token):
        self.access_token = access_token
        self.github = Github(self.access_token)

    def search_repositories(self, query):
        repositories = self.github.search_repositories(query=query)
        return repositories

    def clone_repository(self, repo_url, local_dir):
        command = f'git clone {repo_url} {local_dir}'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    def integrate_repository(self, repo_name, local_dir):
        repo = self.github.get_repo(repo_name)
        self.clone_repository(repo.clone_url, local_dir)

