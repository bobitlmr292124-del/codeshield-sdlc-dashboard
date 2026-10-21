# CodeShield SDLC Security Dashboard — Setup Guide

This guide explains how to install the dependencies, start the Django server and open the CodeShield dashboard in a web browser on your own computer.

CodeShield is a Python and Django web application for recording and managing security incidents in software development infrastructure. Each incident has an ID, title, description, SDLC pillar, severity and status, and the dashboard shows summary totals and charts.

## 1. What you need

- **Python 3.12 or newer.** The project was created with Django 6.1.2, and Django 6.1 supports Python 3.12, 3.13 and 3.14. Check your version with `py --version`.
  - **Windows users:** download Python from [python.org/downloads](https://www.python.org/downloads/), not the Microsoft Store. On the first screen of the installer, tick **Add python.exe to PATH**. After installing, close and reopen VS Code and the terminal, then check again with `py --version`.
- **pip**, which normally comes with Python.
- **Git** (optional, only if you want to clone the repository instead of downloading a ZIP).
- A web browser such as Chrome, Edge or Firefox.
- **An internet connection.** The dashboard charts load the Chart.js library from a CDN (`cdn.jsdelivr.net`). Without internet, the page still works but the charts will not display.
- A code editor such as Visual Studio Code (optional, but it gives you a built-in terminal).

## 2. Get the project

**Option A: Clone with Git**

```bash
git clone https://github.com/bobitlmr292124-del/codeshield-sdlc-dashboard.git
cd codeshield-sdlc-dashboard
```

**Option B: Download a ZIP**

1. Open the repository on GitHub.
2. Click **Code → Download ZIP**.
3. Extract the ZIP and open the extracted folder in VS Code (**File → Open Folder**).

## 3. Open a terminal in the project folder

In VS Code, choose **Terminal → New Terminal**. The terminal must be inside the `codeshield-sdlc-dashboard` folder, the one that contains `manage.py`, the `codeshield` folder and the `incidents` folder. Every command below is run from here.

> **Note:** the commands in this guide use `py`, the Python launcher on Windows. On macOS or Linux, replace `py` with `python3` (for example, `python3 manage.py runserver`).

Check you are in the right place: `manage.py` should appear when you list the files (`dir` on Windows, `ls` on macOS/Linux).

If `manage.py` is not listed, you may be one folder too high. Extracting a ZIP often creates a folder inside a folder (`codeshield-sdlc-dashboard\codeshield-sdlc-dashboard`). Run `cd codeshield-sdlc-dashboard` to go into the inner folder, then list the files again.

## 4. Create a virtual environment (recommended)

A virtual environment keeps the project's packages separate from the rest of your computer.

**Windows (PowerShell or the VS Code terminal)**

Windows usually blocks the activation script in PowerShell, so allow scripts for this terminal window first, then create and activate the environment:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
py -m venv venv
venv\Scripts\Activate.ps1
```

If it asks for confirmation, type `Y` and press Enter. The setting only affects the current terminal window, so repeat the first line if you open a new terminal later. When activation works, your prompt starts with `(venv)`.

Prefer to avoid PowerShell? Open a **Command Prompt** terminal in VS Code (the dropdown next to the **+** in the terminal panel) and activate with `venv\Scripts\activate` instead.

If `py -m venv venv` fails with "Python was not found", Python is not installed yet. Go back to step 1. Creating the virtual environment is optional, so you can skip this step and continue to step 5.

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

When it is active, your terminal prompt starts with `(venv)`.

## 5. Install the dependencies

The project includes a `requirements.txt` file, which lists the required package (Django 6.1.2). Install it with:

```bash
py -m pip install -r requirements.txt
```

Confirm it installed:

```bash
py -m django --version
```

This should print `6.1.2`.

If `requirements.txt` is missing from your copy of the project, install Django directly instead:

```bash
py -m pip install "Django>=6.1,<6.2"
```

## 6. Set up the database

The project uses a SQLite database. A fresh copy from GitHub does not include the database file, so you must create the tables before starting the server:

```bash
py manage.py migrate
```

Django will list the migrations it applies, ending with the `incidents` app. If the database is already up to date, Django reports "No migrations to apply", which is normal.

## 7. Start the Django server

```bash
py manage.py runserver
```

Wait until the terminal shows a message similar to:

```
Starting development server at http://127.0.0.1:8000/
```

Leave this terminal open while you use the dashboard.

## 8. Open the dashboard in a browser

Open this address in your browser:

```
http://127.0.0.1:8000/
```

If the terminal shows a different address or port, use that one instead.

## 9. What you should see

The home page is titled **Security Dashboard** and contains:

- **Incident Overview:** totals for all, open, critical and resolved incidents.
- **Security Analytics:** charts for **Incidents by Severity**, **Incidents by Status** and **Incidents by SDLC Pillar**.
- **Report a Security Incident:** a form on the same page for creating a new incident.
- **Incident Records:** the list of recorded incidents, each with options to edit or delete it.

On a fresh copy from GitHub the database starts empty, so the totals show 0 and the charts have no data until you add incidents (see step 10). Some copies of the project, for example a ZIP that includes `db.sqlite3`, may already contain sample incidents.

## 10. Quick check that everything works

1. Fill in the **Report a Security Incident** form. The **Incident ID** must be unique (for example `CS-010`). Choose a pillar, severity and status, then submit.
2. The new incident should appear in **Incident Records** and the totals should update.
3. Try the edit and delete options on an incident. Deleting shows a confirmation page first.

## 11. Optional: run the automated tests

```bash
py manage.py test
```

The project includes 2 tests (incident creation and dashboard loading). A successful run ends with `OK`.

## 12. Optional: Django admin

The admin page is at `http://127.0.0.1:8000/admin/`. To log in you must first create an administrator account:

```bash
py manage.py createsuperuser
```

Follow the prompts, then sign in at the admin address.

## 13. Stopping the server

Click in the terminal and press **Ctrl + C**.

## Troubleshooting

| Problem | What to try |
| --- | --- |
| "Python was not found; run without arguments to install from the Microsoft Store" | Python is not installed (Windows only has a Store shortcut). Install it from python.org with **Add python.exe to PATH** ticked, then reopen VS Code. |
| `venv\Scripts\activate` says the module or command could not be found | The virtual environment was never created because Python was missing. Install Python, then run `py -m venv venv` again. |
| PowerShell says "running scripts is disabled" | Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then `venv\Scripts\Activate.ps1`. |
| `py` is not recognized | Install Python 3.12 or newer from python.org and tick **Add python.exe to PATH**, then reopen VS Code. On macOS/Linux, use `python3` instead of `py`. |
| Django will not install, or says no matching version | Your Python is probably older than 3.12. Check `py --version` and upgrade Python. |
| `No module named django` | Activate your virtual environment (step 4), then repeat step 5. |
| `can't open file 'manage.py'` | You are in the wrong folder. Use `cd` to move into the folder that contains `manage.py`. |
| `no such table` error | Run `py manage.py migrate`, then start the server again. |
| `That port is already in use` | Stop any other running server, or use another port: `py manage.py runserver 8001`, then open `http://127.0.0.1:8001/`. |
| Charts are blank | If there are no incidents yet, the charts have nothing to show, so add one (step 10). Otherwise check your internet connection, because the charts load Chart.js from the internet. |
| Form says the incident ID already exists | Incident IDs must be unique. Use a different ID. |
| Browser cannot connect | Check that the terminal is still running the server and shows no errors. |

## Important note

This guide describes a **local development setup**. The project is configured with `DEBUG = True` and the Django development server, which is intended for development and testing only and should not be used for public production hosting.
