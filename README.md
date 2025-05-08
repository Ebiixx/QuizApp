# Quiz App

An interactive quiz application that generates questions on various topics and allows users to answer them.

## Features

- Select a topic from a dropdown list.
- Automatically generate 20 quiz questions based on the selected topic.
- Display questions and multiple-choice answers in the user interface.
- Provide feedback for correct and incorrect answers.
- Update the score in the top-right corner for correct answers.
- Automatically reset the answer selection after each question.
- Support for multiple topics such as Science, History, Technology, etc.

## Prerequisites

- Python 3.10 or higher
- PyQt5 for the user interface
- A working OpenAI API or Azure OpenAI API (depending on configuration)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Quiz-App
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your API keys:
   ```plaintext
   AZURE_OPENAI_ENDPOINT=https://<your-resource-name>.openai.azure.com/
   AZURE_OPENAI_API_KEY=<your-api-key>
   ```

## Usage

1. Start the application:

   ```bash
   python src/main.py
   ```

2. Select a quiz topic from the dropdown list.
3. Start the quiz and answer the generated questions based on your selected topic.

## Project Structure

```
quiz-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── ui
│   │   └── main_window.ui     # UI layout for the main window
│   ├── components
│   │   ├── quiz_manager.py    # Manages quiz questions and user answers
│   │   ├── api_client.py      # Interacts with OpenAI API via Azure
│   │   └── topic_selector.py  # Allows users to select quiz topics
│   └── utils
│       └── config.py          # Configuration settings for the application
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files and directories to ignore by Git
└── README.md                  # Documentation for the project
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to suggest improvements or fix bugs.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
