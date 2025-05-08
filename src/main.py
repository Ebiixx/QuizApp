import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressDialog, QLabel
from PyQt5 import QtCore
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

        self.questions = []  # Liste der Fragen
        self.current_question_index = 0  # Index der aktuellen Frage
        self.correct_answer = None

        self.setup_ui()
        self.setup_connections()

        # Standardthema setzen
        self.select_topic()

    def setup_ui(self):
        # Themen in die ComboBox laden
        self.ui.topicComboBox.addItems(self.topics)
        self.ui.questionLabel.hide()
        self.ui.answer1.hide()
        self.ui.answer2.hide()
        self.ui.answer3.hide()
        self.ui.answer4.hide()
        self.ui.submitButton.hide()

        # Punkteanzeige hinzufügen
        self.ui.scoreLabel = QLabel(self)
        self.ui.scoreLabel.setGeometry(700, 10, 80, 30)  # Oben rechts
        self.ui.scoreLabel.setText("Score: 0")
        self.ui.scoreLabel.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.ui.scoreLabel.show()

    def setup_connections(self):
        self.ui.startButton.clicked.connect(self.start_quiz)
        self.ui.submitButton.clicked.connect(self.check_answer)
        self.ui.topicComboBox.currentIndexChanged.connect(self.select_topic)

    def start_quiz(self):
        selected_topic = self.topic_selector.get_selected_topic()
        if not selected_topic:
            QMessageBox.warning(self, "Warning", "Please select a topic.")
            return

        # Spinner anzeigen
        progress_dialog = QProgressDialog("Generating quiz...", None, 0, 0, self)
        progress_dialog.setWindowTitle("Please wait")
        progress_dialog.setCancelButton(None)
        progress_dialog.setModal(True)
        progress_dialog.show()

        try:
            # Mehrere Fragen abrufen
            self.questions = self.quiz_manager.fetch_questions(selected_topic, num_questions=20)
            self.current_question_index = 0
            progress_dialog.close()  # Spinner schließen
            self.display_question()
        except Exception as e:
            progress_dialog.close()  # Spinner schließen
            QMessageBox.critical(
                self,
                "Error",
                f"An error occurred while fetching questions:\n{str(e)}"
            )

    def display_question(self):
        # Prüfen, ob noch Fragen übrig sind
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
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
        else:
            QMessageBox.information(self, "Quiz Completed", "You have completed the quiz!")

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
            self.show_feedback("Correct!", "green")
            self.update_score()
        else:
            self.show_feedback(f"Wrong! Correct: {self.correct_answer}", "red")

        # Nächste Frage anzeigen
        self.current_question_index += 1
        self.reset_answers()
        self.display_question()

    def reset_answers(self):
        self.ui.answer1.setAutoExclusive(False)
        self.ui.answer2.setAutoExclusive(False)
        self.ui.answer3.setAutoExclusive(False)
        self.ui.answer4.setAutoExclusive(False)

        self.ui.answer1.setChecked(False)
        self.ui.answer2.setChecked(False)
        self.ui.answer3.setChecked(False)
        self.ui.answer4.setChecked(False)

        self.ui.answer1.setAutoExclusive(True)
        self.ui.answer2.setAutoExclusive(True)
        self.ui.answer3.setAutoExclusive(True)
        self.ui.answer4.setAutoExclusive(True)

    def select_topic(self):
        # Setze das Standardthema, falls keines ausgewählt wurde
        selected_topic = self.ui.topicComboBox.currentText()
        if not selected_topic:
            selected_topic = self.topics[0]  # Erstes Thema als Standard
        self.topic_selector.set_selected_topic(selected_topic)

    def show_feedback(self, message, color="green"):
        self.ui.feedbackLabel = QLabel(self)
        self.ui.feedbackLabel.setGeometry(50, 450, 300, 30)  # Position im UI
        self.ui.feedbackLabel.setText(message)
        self.ui.feedbackLabel.setStyleSheet(f"color: {color}; font-size: 14px; font-weight: bold;")
        self.ui.feedbackLabel.show()

        # Feedback nach 3 Sekunden ausblenden
        QtCore.QTimer.singleShot(3000, self.ui.feedbackLabel.hide)

    def update_score(self):
        current_score = int(self.ui.scoreLabel.text().split(": ")[1])
        current_score += 1
        self.ui.scoreLabel.setText(f"Score: {current_score}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()