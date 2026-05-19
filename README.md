# Alumni Management System

A web-based portal developed for **St. Joseph's University** to bridge the gap between current students and alumni. The platform allows alumni to register, share career insights, and stay connected with the institution, while providing an administrative overview to manage the portal effectively.

---

## 🚀 Features

* **User Authentication & Profiles:** Secure registration and login for alumni and students with role-based access.
* **Alumni Directory:** A searchable and filterable database of university alumni across various batches and departments.
* **Interactive Dashboard:** Personalized user feeds displaying recent updates, networking opportunities, and system stats.
* **Dynamic Forms:** Built-in form validation for registration, login, and profile updates using Flask-WTF.

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask Framework)
* **Database:** MongoDB (NoSQL database for flexible data storage)
* **Frontend:** HTML5, CSS3, JavaScript
* **Environment & Package Management:** `uv` (Fast Python package installer)

---

## 📋 Prerequisites

Before running this project, ensure you have the following installed on your system:
* [Python 3.12+](https://www.python.org/downloads/)
* [MongoDB Community Server](https://www.mongodb.com/try/download/community) (Make sure the MongoDB service is running locally)
* [`uv` package manager](https://docs.astral.sh/uv/)

---

## ⚙️ Installation & Setup

Follow these steps to set up and run the application locally on your machine:

### 1. Clone the Project
Navigate to your working directory and open your terminal or PowerShell.

### 2. Set Up the Virtual Environment
Create and activate an isolated environment using `uv`:
```bash
# Create the virtual environment
uv venv

# Activate on Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Activate on Mac/Linux
source .venv/bin/activate
