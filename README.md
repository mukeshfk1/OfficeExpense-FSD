# Office Expense Project Setup

This guide will help you set up and run the project.

## Prerequisites

- Python (>=3.8)
- pip (latest version recommended)

## Setup Instructions

### 1. Create and Activate a Virtual Environment

#### Windows (Command Prompt):
```sh
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
Ensure you have a `requirements.txt` file with the necessary dependencies. Then, install them using:

```sh
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file, you can install Flask manually:

```sh
pip install flask
```

### 3. Run the Application
Execute the Flask application:

```sh
python main.py
```

### 4. Access the Application
By default, Flask runs on `http://127.0.0.1:5000`. Open your browser and navigate to this URL.

## Additional Notes
- To deactivate the virtual environment, use `deactivate`.
- If using a `flask run` command, set the `FLASK_APP` environment variable:
  - Windows: `set FLASK_APP=main.py`
  - macOS/Linux: `export FLASK_APP=main.py`


