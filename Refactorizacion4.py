class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        return f"Title: {self.title}\nContent: {self.content}"


class ReportSaver:
    @staticmethod
    def save_to_file(report, filename):
        with open(filename, 'w') as file:
            file.write(report.generate_report())


report = Report("My Report", "This is the content.")
ReportSaver.save_to_file(report, "report.txt")


with open("report.txt", "r") as file:
    saved_content = file.read()

print(saved_content)