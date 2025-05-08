import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressDialog
from components.quiz_manager import QuizManager
from components.topic_selector import TopicSelector
from components.api_client import APIClient
from ui.main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create APIClient and pass it to QuizManager
        api_client = APIClient()
        self.quiz_manager = QuizManager(api_client)
        self.topic_selector = TopicSelector()

        # Themenliste
        self.topics = [
            "Science",
            "History",
            "Technology",
            "Mathematics",
            "Literature",
            "Geography"
        ]

        self.current_question = None
        self.correct_answer = None

        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        # Themen in die ComboBox laden
        self.ui.topicComboBox.addItems(self.topics)
        self.ui.questionLabel.hide()
        self.ui.answer1.hide()
        self.ui.answer2.hide()
        self.ui.answer3.hide()
        self.ui.answer4.hide()
        self.ui.submitButton.hide()

    def setup_connections(self):
        self.ui.startButton.clicked.connect(self.start_quiz)
        self.ui.submitButton.clicked.connect(self.check_answer)
        self.ui.topicComboBox.currentIndexChanged.connect(self.select_topic)

    def start_quiz(self):
        selected_topic = self.topic_selector.get_selected_topic()
        if selected_topic:
            # Spinner anzeigen
            progress_dialog = QProgressDialog("Generating quiz...", None, 0, 0, self)
            progress_dialog.setWindowTitle("Please wait")
            progress_dialog.setCancelButton(None)
            progress_dialog.setModal(True)
            progress_dialog.show()

            try:
                # Fragen abrufen
                question_data = self.quiz_manager.fetch_questions(selected_topic)
                progress_dialog.close()  # Spinner schließen
                self.display_question(question_data)
            except Exception as e:
                progress_dialog.close()  # Spinner schließen
                QMessageBox.critical(
                    self,
                    "Error",
                    f"An error occurred while fetching questions:\n{str(e)}"
                )
        else:
            QMessageBox.warning(self, "Warning", "Please select a topic.")

    def display_question(self, question_data):
        # Beispiel: Frage und Antworten aus den Daten extrahieren
        self.current_question = question_data["question"]
        self.correct_answer = question_data["correct_answer"]
        answers = question_data["answers"]

        # Frage und Antworten in der UI anzeigen
        self.ui.questionLabel.setText(self.current_question)
        self.ui.answer1.setText(answers[0])
        self.ui.answer2.setText(answers[1])
        self.ui.answer3.setText(answers[2])
        self.ui.answer4.setText(answers[3])

        self.ui.questionLabel.show()
        self.ui.answer1.show()
        self.ui.answer2.show()
        self.ui.answer3.show()
        self.ui.answer4.show()
        self.ui.submitButton.show()

    def check_answer(self):
        # Überprüfen, welche Antwort ausgewählt wurde
        selected_answer = None
        if self.ui.answer1.isChecked():
            selected_answer = self.ui.answer1.text()
        elif self.ui.answer2.isChecked():
            selected_answer = self.ui.answer2.text()
        elif self.ui.answer3.isChecked():
            selected_answer = self.ui.answer3.text()
        elif self.ui.answer4.isChecked():
            selected_answer = self.ui.answer4.text()

        if selected_answer == self.correct_answer:
            QMessageBox.information(self, "Correct!", "Your answer is correct!")
        else:
            QMessageBox.warning(self, "Wrong!", f"Wrong answer! The correct answer was: {self.correct_answer}")

    def select_topic(self):
        self.topic_selector.set_selected_topic(self.ui.topicComboBox.currentText())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()