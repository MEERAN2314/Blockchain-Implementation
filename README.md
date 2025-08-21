# Simple Blockchain Explorer

This project implements a basic blockchain explorer using Python with FastAPI for the backend and Jinja2 for rendering the frontend HTML. It allows users to add new transactions and view the current state of the blockchain through a simple web interface.

## Features

*   **Blockchain Implementation**: A simplified blockchain structure with blocks, transactions, and basic proof-of-work.
*   **Transaction Management**: Add new transactions (sender, recipient, amount) to be included in the next mined block.
*   **Web Interface**: A user-friendly web interface to interact with the blockchain.
*   **Dynamic UI**: Enhanced user interface with modern styling and animations for a smoother experience.
*   **Real-time Feedback**: Instant feedback messages for transaction additions.

## Technologies Used

*   **Backend**: Python 3, FastAPI
*   **Templating**: Jinja2
*   **Frontend**: HTML5, CSS3, JavaScript

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

*   Python 3.7+
*   pip (Python package installer)

### Installation Steps

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/MEERAN2314/Blockchain-Implementation.git
    cd Blockchain-Implementation
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application**:
    ```bash
    uvicorn main:app --reload
    ```
    The `--reload` flag is optional but useful for development as it restarts the server on code changes.

## Usage

Once the application is running, open your web browser and navigate to:

```
http://127.0.0.1:8000
```

### Adding a Transaction

1.  On the homepage, locate the "Add New Transaction" section.
2.  Enter the **Sender**, **Recipient**, and **Amount** in the respective fields.
3.  Click the "Add Transaction" button.
4.  A success or error message will appear at the top of the screen, and the page will reload to display the updated blockchain.

### Viewing the Blockchain

The "Blockchain" section displays all the blocks in the chain, including their index, timestamp, transactions, and hash. New blocks will appear with a subtle animation.

## UI Improvements

The user interface has been significantly improved with:
*   A modern, clean design using `Segoe UI` font and a gradient background.
*   Smooth `fadeInScale` animation for the main container.
*   `slideInLeft` and `slideInRight` animations for `h2` titles and blockchain table rows, creating a dynamic entry effect.
*   Enhanced input fields and buttons with hover and active states.
*   A custom, animated message box for transaction feedback, replacing the default browser `alert()`.

## Screenshots

Here are some screenshots of the application:

### Homepage
![Homepage](Output%20Images/image1.png)

### Add Transaction Form
![Add Transaction Form](Output%20Images/image2.png)

### Blockchain Table
![Blockchain Table](Output%20Images/image3.png)

### Transaction Added Feedback
![Transaction Added Feedback](Output%20Images/image4.png)

### Error Feedback
![Error Feedback](Output%20Images/image5.png)
