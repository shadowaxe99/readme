
import os
import re

class FileAnalyzer:
    def __init__(self, path):
        self.path = path

    def get_file_content(self):
        with open(self.path, 'r') as file:
            content = file.read()
        return content

    def get_file_structure(self):
        file_structure = {}
        for root, dirs, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root, file)
                file_structure[file_path] = self.get_file_content(file_path)
        return file_structure

    def get_code_blocks(self):
        file_structure = self.get_file_structure()
        code_blocks = {}
        for file, content in file_structure.items():
            code_blocks[file] = re.findall(r'
        return code_blocks
