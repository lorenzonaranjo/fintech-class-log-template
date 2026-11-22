# FinTech class log

FIN 4506/5506, Spring 2027, second half (Professor Naranjo).

This repository is yours alone. Each class ends with a short task: you run some code, change something in it, and explain what you see. You keep that work in the session's folder, commit it, and hand in the whole log on Canvas before you leave.

## How it counts

Your participation grade for the second half comes from attendance and from this log. A session counts when the file made by `submit.py`, with that session's work committed in it, is **uploaded to that session's Canvas assignment before the end of that class**. Canvas records when each file arrives, so an upload after class does not count for that session.

The log is graded for completion, not for being right. You may use Claude or any other tool. The point is to work through the ideas of each class with the code in front of you; the final exam is on paper and closed book.

## Each session

1. Open the session's folder, for example `session-03-03-30/`, and copy the task from the course site into the **Task** section of `log.md`.
2. Save the task's code in the same folder, for example as `task.py`, and run it with `python task.py`. Paste what it prints into the **Output** section.
3. Make the changes the task asks for, run the code again, and paste each new output.
4. Write your explanation in **My answer**, how you know it is right in **What I checked**, and what is still unclear.
5. Commit, make the file to hand in, and upload it to the session's Canvas assignment. This is what counts:

   ```bash
   git add -A
   git commit -m "Session 3"
   python submit.py
   ```

   `submit.py` writes a file such as `class-log-2027-03-30-1545.bundle` in your course folder, with your whole log and its history. Upload that file. (GitHub's "Download ZIP" button leaves out the history, so do not use it.)
6. Push, so that GitHub keeps a copy: `git push`.

Commit as you work, not only at the end: the history of your log shows how you worked through each task.

## Setup

Do this once, before the first class on March 23. You set up one Python environment and use it for this log and for the project later.

1. **Claude Edu.** Complete the "AI Literacy for the WashU Scholar" module on Canvas. It gives you access to Claude Edu through your WashU account.
2. **Git and a GitHub account.** Install Git from <https://git-scm.com/downloads> (on a Mac, running `git --version` in the Terminal offers to install it). Create a GitHub account if you do not have one, then tell Git who you are, using the email of your GitHub account:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

3. **Python.** Install Python 3.13 from <https://www.python.org/downloads/>. On Windows, tick "Add python.exe to PATH" in the installer.
4. **Claude Code.** Follow the installation instructions at <https://code.claude.com/docs/en/setup>, then run `claude` in a terminal and log in with your WashU Claude account.
5. **Your class log on GitHub.** Open <https://github.com/lorenzonaranjo/fintech-class-log-template>, click **Use this template**, then **Create a new repository**. Choose your own account as the owner, name it `fin4506-class-log`, and select **Private**. Copy its URL from the green **Code** button.
6. **A course folder with the Python environment.** Make a folder for the course, create the environment in it, and clone your class log into it:

   ```bash
   mkdir fin4506
   cd fin4506
   python -m venv .venv
   git clone <your class log URL> class-log
   ```

   Activate the environment with `source .venv/bin/activate` (Mac) or `.venv\Scripts\activate` (Windows), then:

   ```bash
   cd class-log
   pip install -r requirements.txt
   python check_setup.py
   ```

   On Linux, including WSL on Windows, run `pip install torch --index-url https://download.pytorch.org/whl/cpu` before `pip install -r requirements.txt`. Otherwise pip downloads several gigabytes of GPU libraries you do not need.

`check_setup.py` checks each piece and tells you what is missing, then renders a test page. Come to the first class with every line passing, or with the output of the script if something fails.

Every time you work on the course, open a terminal, go to `fin4506`, and activate the environment first.
