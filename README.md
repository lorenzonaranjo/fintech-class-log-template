# FinTech class log

FIN 4506/5506, Spring 2027, second half (Professor Naranjo).

This repository is yours alone. Each class ends with a short task: you record your work on it in that session's `log.md`, hand the file in on Canvas before you leave, and commit it here.

## How it counts

Your participation grade for the second half comes from this log. A session counts when your `log.md` for that session, with your work in it, is **uploaded to that session's Canvas assignment before the end of that class**. Canvas records when each file arrives, so an upload after class does not count for that session.

The log is graded for completion, not for being right. You may use Claude or any other tool. The task is a problem in the format of the final exam, though, and the final is closed book, so the log is your practice for it.

## Each session

1. Open the session's folder, for example `session-03-03-30/log.md`.
2. Copy the task from the course site into the **Task** section.
3. Work on it, and write your answer, what you checked, and what is still unclear.
4. Upload `log.md` to the session's Canvas assignment. This is what counts.
5. Commit and push, so that your log is kept with its history:

   ```bash
   git add -A
   git commit -m "Session 3"
   git push
   ```

If the task involves code, put the code file in the same folder.

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

`check_setup.py` checks each piece and tells you what is missing, then renders a test page. Come to the first class with every line passing, or with the output of the script if something fails.

Every time you work on the course, open a terminal, go to `fin4506`, and activate the environment first.
