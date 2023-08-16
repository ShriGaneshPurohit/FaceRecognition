# Face Recognition Attendance System

This Git repository contains a Face Recognition Attendance System implemented in Python using OpenCV for face detection and recognition, Excel for data storage, Tkinter for the graphical user interface (GUI), and SQL for database management.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)


## Introduction

The Face Recognition Attendance System is a project that aims to automate the attendance management process using face recognition technology. The system captures images of individuals, processes them to detect and recognize faces, records attendance data, and stores it in both Excel sheets and a SQL database.

## Features

- Face detection and recognition using OpenCV.
- Graphical User Interface (GUI) built with Tkinter for easy interaction.
- Excel sheets are used to store attendance data.
- SQL database integration for efficient data management.
- User-friendly and intuitive interface for both administrators and users.

## Requirements

- Python (>= 3.6)
- OpenCV
- Tkinter
- pandas
- mysqlconnector


## Installation

1. Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/your-username/face-recognition-attendance.git
   ```

2. Navigate to the project directory:

   ```bash
   cd face-recognition-attendance
   ```



## Usage

1. Run the main application:

   ```bash
   python main.py
   ```

2. The GUI will appear, providing options for administrators and users.
3. Administrators can add new users, train the face recognition model, and view attendance reports.
4. Users can mark their attendance by having their faces recognized.

## Contributing

Contributions to this project are welcome! If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Implement your feature or fix.
4. Commit and push your changes: `git commit -m "Description of your changes"` and `git push origin feature-name`.
5. Create a pull request, describing the changes you've made.


