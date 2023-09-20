
import os
from models.ai_model import AIModel
from utils.file_analyzer import FileAnalyzer
from utils.github_analyzer import GithubAnalyzer

class Main:
    def __init__(self):
        self.ai_model = AIModel()
        self.file_analyzer = FileAnalyzer()
        self.github_analyzer = GithubAnalyzer()

    def run(self, repo_path):
        # Analyze the repository
        repo_info = self.github_analyzer.analyze(repo_path)

        # Analyze the files in the repository
        file_info = self.file_analyzer.analyze(repo_path)

        # Generate the readme content
        readme_content = self.ai_model.generate_readme(repo_info, file_info)

        # Write the readme content to a README.md file
        with open(os.path.join(repo_path, 'README.md'), 'w') as f:
            f.write(readme_content)

if __name__ == "__main__":
    main = Main()
    main.run("<Your Repository Path>")
