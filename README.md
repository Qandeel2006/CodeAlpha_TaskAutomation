<h1 align="center">🗂️ Task Automation</h1>

<p align="center">
  <b>A Python script that moves all your .jpg images into one folder automatically.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/CodeAlpha-Task%203-6C47FF" alt="CodeAlpha">
  <img src="https://img.shields.io/badge/Level-Beginner-orange" alt="Level">
</p>

---

## 💡 About

This is **Task 3** of my [CodeAlpha](https://www.codealpha.tech) Python Programming Internship.
Sorting files by hand is boring, so this script does it for you. It finds every `.jpg` image in a folder and moves them into a new folder called `jpg_files`.

## 🎯 Chosen Idea

The task asked me to pick **one** of these automation ideas:

- [x] Move all `.jpg` files from a folder to a new folder
- [ ] Extract all email addresses from a `.txt` file and save them to another file
- [ ] Scrape the title of a fixed webpage and save it

I chose the first one because it is a real, everyday problem: it keeps a messy folder tidy without any manual work.

## ✨ Features

- 📂 Creates the `jpg_files` folder if it does not exist
- 🖼️ Moves every `.jpg` file (works with `.JPG` too)
- 🧾 Prints each file as it is moved
- 🔢 Shows how many files were moved

## 🔄 Before and After

```text
BEFORE                      AFTER
Pictures/                   Pictures/
├── holiday.jpg             ├── notes.txt
├── family.jpg              └── jpg_files/
└── notes.txt                   ├── holiday.jpg
                                └── family.jpg
```

## 🖥️ Example

```text
Enter the folder path (example: C:/Users/Me/Pictures): C:/Users/Me/Pictures
Moved: holiday.jpg
Moved: family.jpg
Done! 2 file(s) moved.
```

> ⚠️ **Tip:** try it on a test folder first. It really moves your files!

## ⚙️ Getting Started

**Requirements:** Python 3 (nothing else to install)

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_TaskAutomation.git
cd CodeAlpha_TaskAutomation
python task_automation.py
```

> On some computers the command is `python3` instead of `python`.

## 🧠 Concepts Used

| Concept | Where it is used |
|---------|------------------|
| `os` | Listing files and making the new folder |
| `shutil` | Moving the files |
| Loops and `if` | Checking each file in the folder |
| File handling | Working with paths and file names |

## 📁 Project Structure

```text
CodeAlpha_TaskAutomation/
├── task_automation.py
├── .gitignore
└── README.md
```

---

## 👤 Author

**Your Name**
Python Programming Intern at [CodeAlpha](https://www.codealpha.tech)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/YOUR_PROFILE)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?logo=github&logoColor=white)](https://github.com/YOUR_USERNAME)

<p align="center">
  ⭐ If you liked this project, give it a star! ⭐<br>
  Made with ❤️ during the <b>CodeAlpha</b> internship
</p>
