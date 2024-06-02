class FileManipulator:
    def replace_line_in_file(self, filepath: str, search_text: str, replace_text: str):
        with open(filepath, "r") as file:
            lines = file.readlines()

        with open(filepath, "w") as file:
            for line in lines:
                file.write(line.replace(search_text, replace_text))
