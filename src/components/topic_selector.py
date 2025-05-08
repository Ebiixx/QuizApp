class TopicSelector:
    def __init__(self):
        self.selected_topic = None

    def set_selected_topic(self, topic):
        """Set the currently selected topic."""
        self.selected_topic = topic

    def get_selected_topic(self):
        """Get the currently selected topic."""
        return self.selected_topic