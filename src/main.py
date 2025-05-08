import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from components.quiz_manager import QuizManager
from components.topic_selector import TopicSelector
from ui.main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.quiz_manager = QuizManager()
        self.topic_selector = TopicSelector()

        self.setup_connections()

    def setup_connections(self):
        self.ui.startButton.clicked.connect(self.start_quiz)
        self.ui.topicComboBox.currentIndexChanged.connect(self.select_topic)

    def start_quiz(self):
        selected_topic = self.topic_selector.get_selected_topic()
        if selected_topic:
            self.quiz_manager.fetch_questions(selected_topic)
            # Logic to start the quiz goes here
        else:
            QMessageBox.warning(self, "Warning", "Please select a topic.")

    def select_topic(self):
        self.topic_selector.set_selected_topic(self.ui.topicComboBox.currentText())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()