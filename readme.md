# Task Management Project

A **lightweight, Python-based task management system** that blends **database efficiency** with the simplicity of **Markdown**. This project is designed to offer flexible, powerful task management through both **SQLite** and **plain-text file integration**, making it ideal for those who prefer **customizable workflows** over rigid third-party tools.  

This project is a hands-on exercise to deepen my Python skills, while building something **practical** and **expandable** for real-world use.

---

## 🚀 Features

- **Effortless Database Setup:** Quickly initialize your SQLite database with `db_init.py`.
- **Full CRUD Operations:** Create, read, update, and delete tasks with intuitive scripts (`task_import_db.py`, `task_update_db.py`, `task_delete.py`).
- **Markdown Integration:** Generate and parse Markdown task entries with `task_creator.py` and `task_parser.py`—perfect for linking tasks to notes.
- **Version Control Support:** Track changes in task files using simple Git utilities (`git_file_change.py`).
- **Modular Architecture:** Easily extend or customize functionalities using `model.py`.

---

## ⚡ Quick Start

1. **Initialize the Database:**  
   Run `db_init.py` to set up your SQLite database.
   
   ```bash
   python db_init.py
   ```

2. **Add or Update Tasks:**  
   Use `task_import_db.py` to add new tasks, or `task_update_db.py` to modify existing ones.

   ```bash
   python task_import_db.py
   python task_update_db.py
   ```

3. **Delete Tasks:**  
   Remove tasks from the database with `task_delete.py`.

   ```bash
   python task_delete.py
   ```

4. **Customize and Expand:**  
   Extend task behavior or structure through `model.py` for tailored workflows.

---

## 🔧 Project Vision & Roadmap

The ultimate goal is to create a **hybrid task management system** that merges the **robustness of databases** with the **flexibility of plain-text files**. It will support **Markdown-based task management**, integrating seamlessly with **note-taking applications** (like Obsidian), while maintaining **version control** through Git for transparent tracking.

### Coming Soon:
- **Markdown Task Storage:**  
  Store and manage tasks directly within `.md` files, while maintaining database syncing.
  
- **Note-Taking Integration:**  
  Seamless linking between tasks and notes, allowing for context-rich task management.
  
- **Advanced Querying & Reporting:**  
  Powerful search and reporting functionalities, with filters for due dates, priorities, and tags.

---
## Bucket List
Natural language integration (today, tomorrow,...)
## 🛠 Tech Stack

- **Python 3.x**  
- **SQLite** for lightweight data storage  
- **Markdown** for plain-text task representation  
- **Git** for version control integration  

---

## 🤝 Contributing

This project is primarily a **learning exercise**, but I’m open to feedback, suggestions, or even potential collaboration! If you’ve got ideas to improve the system or want to adapt it for your workflow, feel free to fork or open an issue.

---

