class TopicSelector:
    def __init__(self):
        self.topics = ["Science", "History", "Geography", "Literature"]
        self.selected_topic = None

    def get_available_topics(self):
        return self.topics

    def select_topic(self, topic):
        if topic in self.topics:
            self.selected_topic = topic
            return True
        return False

    def notify_quiz_manager(self, quiz_manager):
        if self.selected_topic:
            quiz_manager.set_topic(self.selected_topic)