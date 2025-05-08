# Quiz Application

This is a quiz application built using PyQt that allows users to select a topic and generates questions via the OpenAI API, accessed through Azure.

## Features

- User-friendly interface for selecting quiz topics.
- Dynamic question generation based on selected topics.
- Integration with OpenAI API for question retrieval.

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
│   │   └── topic_selector.py   # Allows users to select quiz topics
│   └── utils
│       └── config.py         # Configuration settings for the application
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files and directories to ignore by Git
└── README.md                  # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd quiz-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Select a quiz topic from the dropdown menu.
3. Start the quiz and answer the questions generated based on your selected topic.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.