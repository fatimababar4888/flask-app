# Flask Basic Web Application

A simple Flask web application with multiple routes, form handling, and a modern UI.

## Features

- Home page with hero section and feature cards
- About page with information about the app
- Contact form with validation and flash messages
- Modern, responsive design
- Clean and organized code structure

## Installation

1. Make sure you have Python installed (Python 3.7 or higher)

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the Flask application:

```bash
python app.py
```

The app will be available at `http://localhost:5000`

## Project Structure

```
flask_app/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── README.md             # This file
│
├── templates/            # HTML templates
│   ├── index.html
│   ├── about.html
│   └── contact.html
│
└── static/               # Static files (CSS, JS, images)
```

## Routes

- `/` - Home page
- `/about` - About page
- `/contact` - Contact form (GET and POST)

## License

This is a basic example application for educational purposes.

