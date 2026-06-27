# PM-Accelerator-AI_Eval_Harness

## 📊 Application Dashboard
<img width="1891" height="705" alt="Success USE" src="https://github.com/user-attachments/assets/7f5dab65-5529-44b9-9a6a-d3d7190e201a" />

### This image shows the completed, working AI Evaluation Harness Dashboard running live in your web browser.
1. It confirms that your frontend, backend, and local database are completely integrated and communicating perfectly with each other.
2. Key Elements on the Screen:
### Header: It displays the title "AI Evaluation Harness" along with the description "Real-time LLM validation telemetry and accuracy tracking."
3. Action Button: A blue "Execute Run" button sits in the top right corner.
4. Live Status Banner: The bright blue alert box says: 🚀 System Status Notice: Evaluation run saved safely to local database! This proves your Next.js frontend successfully reached out to your FastAPI backend, which then saved a real tracking row into your SQLite file.
### Data Table: Under "Latest Evaluation Run Records", a cleanly formatted table displays your live evaluation metric:
5.Run ID: 1
---
<img width="1513" height="962" alt="Screenshot 2026-06-26 185022" src="https://github.com/user-attachments/assets/5d90a2ee-2a86-419e-9fcb-d76457c00bdf" />

<img width="992" height="376" alt="Screenshot 2026-06-26 184927" src="https://github.com/user-attachments/assets/cd92a68d-3e89-41bc-be2b-951c5b8bcd58" />

<img width="1356" height="857" alt="Screenshot 2026-06-26 225952" src="https://github.com/user-attachments/assets/9c99169d-818e-443d-bf16-29647f0785ab" />

<img width="998" height="494" alt="Screenshot 2026-06-26 215749" src="https://github.com/user-attachments/assets/2f3af6b9-a3dd-40e6-af24-8fec66f11ce3" />

<img width="1600" height="967" alt="Screenshot 2026-06-27 004905" src="https://github.com/user-attachments/assets/e5e10d95-e7a0-4bea-bfd5-2b4d8f21b4cd" />


A project for the PM Accelerator AI/ML Internship Front-end developer cohort 9, team 10.

## 🚀 Features
- **PDF Extraction**: Reads layout blocks from uploaded documents.
- **Database System**: Uses a local SQLite database (`ai_eval.db`) to log test data.
- **Dataset Loader**: Includes tools to import test questions automatically.

## 🛠️ How to Run the Project
1. Run `init_db.py` to set up your local database tables.
2. Run `load_dataset.py` to populate your test queries.
3. Execute `main.py` to start the core harness application.

## 👥 Team Members
- @LiXiu37YaHua (Luminita Gheorghe)

## 💻 How to View the Project Output
Because this is a Python backend project, users cannot simply open a "live website" from GitHub. It must be run locally on a machine, or viewed via screenshots. 

### Option 1: Run the Project Locally
Anyone on the team can download a copy of these files to test them:
1. Click the blue **`<> Code`** button at the top of this repository page.
2. Click **Download ZIP**.
3. Extract the folder and open it inside **PyCharm**.
4. Set up your Python environment, install required packages, and run `main.py` to connect to `localhost`.

### Option 2: Look at Project Screenshots
To review the project output without downloading the code:
- Check the repository folders for any included output logs or terminal screenshots.
- View the active app visuals embedded directly in this documentation homepage.

### Option 3: Future Deployment
If the frontend needs to be publicly accessible over the internet later, the cohort team will deploy this backend architecture to a cloud hosting platform such as **Render**, **Vercel**, or **Streamlit Community Cloud**.

## 📦 Requirements & Installation
Before running the project locally, you need to install the required Python packages. Open your PyCharm terminal and run the following command:

```bash
pip install PyMuPDF
```
*Note: The `fitz` module imported in `pdf_reader.py` belongs to the `PyMuPDF` package.*

# AI Evaluation Harness: Engineering Project Report

## 📋 Metadata & Cohort Details
* **Program:** PM Accelerator — Cohort 9
* **Team:** Team 10: PlainAIV
* **Project Name:** Create Golden Datasets for Eval Harness
* **Session:** 2-Hour Tech Refresher (06/26/2026, 4:34 PM - 6:30 PM)
* **Developer:** Marissa Lanza — Front-End Developer
* **Author Role:** Software Engineering Student
* **Focus Area:** Golden Dataset Architecture, Live Telemetry Tracking, & Core Product Refresher
* **Development Date:** June 2026


## 1. 🎯 Executive Summary & Core Objective
This research and implementation project focused on building an end-to-end full-stack automated AI Evaluation Harness framework. The primary engineering goal was researching how to effectively construct, serve, store, and visualize structured Golden Datasets (ground-truth reference parameters) used to benchmark Large Language Model (LLM) accuracy.

The architecture successfully bridges:
* Data extraction layers
* A persistent database layer
* Back-end REST APIs
* A server-side rendered modern front-end user interface dashboard



## 💻 2. Technical Stack & Environment Layout
The project was intentionally split across specialized development environments to maintain clear engineering boundaries:

### Integrated Development Environments (IDEs)
* **PyCharm Professional:** Utilized exclusively for backend development, database configuration, script executions, and local file generation.
* **Visual Studio Code (VS Code):** Utilized exclusively for Next.js web application creation, component tree styling, and web server execution.

### Programming Languages & Runtime Engines
* **Python 3.9:** Powered data processing scripts, file extraction modules, and server endpoints.
* **Node.js 22 (LTS Upgrade):** Provided the JavaScript runtime required for compiling the modern front-end application layout.
* **TypeScript / React:** Enforced strict data typing across the dashboard page layout.

### Database Management System
* **SQLite (Local Database Engine):** Configured as a lightweight, zero-install embedded SQL data store saving direct relational rows (`ai_eval.db`) right within the project workspace tree.



## 🛠️ 3. Sequential Implementation Steps Taken

### Phase A: Document Generation & Parsing (PyCharm)
1. Installed `reportlab` inside the virtual environment (`venv`) to programmatically build an anchor target document layout.
2. Created `make_sample_pdf.py` to generate a 2-section corporate employee handbook file (`sample_handbook.pdf`) inside the `uploaded_pdfs/` workspace directory.
3. Leveraged PyMuPDF (`fitz`) inside `pdf_reader.py` to iterate over document indices and extract layout-aware structural blocks.

### Phase B: Golden Dataset Schema Design
Designed an extended JSON data tracking architecture saved directly as `datasets/hr_dataset.json` utilizing comprehensive evaluation parameters:
* `id`: Unique test case alphanumeric key
* `source_doc`: Origin file mapping
* `page_number`: Target source index
* `question`: The evaluation baseline inquiry
* `expected_answer`: The ground-truth perfect metric
* `evaluation_criteria`: Core linguistic keywords needed to achieve accuracy status

### Phase C: Backend API & Database Infrastructure (PyCharm)
1. Created `init_db.py` to execute a local relational schema build containing `id` (`INTEGER PRIMARY KEY AUTOINCREMENT`), `question`, `expected_answer`, `actual_answer`, and score tracking metrics.
2. Built a web routing infrastructure via FastAPI inside `main.py`.
3. Created an active `GET` route endpoint located at `/evaluate` that automatically intercepts incoming queries, executes a raw SQL `INSERT` mutation logging run details directly into the SQLite file, and returns a verified JSON packet payload.

### Phase D: Frontend Interface Dashboard Layout (VS Code)
1. Navigated out of standalone projects and initialized a full-stack project utilizing `npx create-next-app@latest frontend` inside the harness directory.
2. Integrated `shadcn/ui` layout frameworks built on top of Radix primitives and Tailwind CSS.
3. Installed structural visual layout layers via `npx shadcn@latest add table` and `npx shadcn@latest add button`.
4. Constructed `app/page.tsx` as an asynchronous Next.js Server Component that performs an internal server-to-server data fetch straight from the FastAPI engine, rendering a live telemetry interface reporting a dynamic 100% evaluation accuracy score.



## ⚠️ 4. Engineering Issues Encountered & Resolutions

### Issue 1: Missing File Extension Blockers
* **Symptom:** PyCharm terminal returned `python: can't open file 'make_sample_pdf.py': [Errno 2] No such file or directory` and the IDE flagged the script file as "Not Runnable."
* **Root Cause:** The file had accidentally been generated as a plain text string file named `make_sample_pdf` missing its explicit `.py` extension.
* **Resolution:** Performed an active file workspace refactor renaming the directory node to `make_sample_pdf.py`, turning on its Python interpreter target wrapper instantly.

### Issue 2: Local Host Server Runtime Shutdowns
* **Symptom:** Refreshing web browser pages triggered standard connection failures; localhost routes went completely dark.
* **Root Cause:** Attempting to start continuous web listening environments by clicking PyCharm's standard green play run arrow executing as an isolated, temporary processing script.
* **Resolution:** Shifted execution to the dedicated Terminal pane utilizing the direct command-line execution string `uvicorn main:app --reload`.

### Issue 3: Node.js Runtime Framework Rejection
* **Symptom:** Next.js installer threw a fatal error block warning: `You are using Node.js 18.20.8. For Next.js, Node.js version ">=20.9.0" is required.`
* **Root Cause:** The computer's operating system environment was operating on an outdated Node version that lacked structural library bindings.
* **Resolution:** Downloaded and installed the updated Node.js 22 LTS environment package, restarted the development apps, and cleanly verified the execution path.

### Issue 4: Mismatched Native Library Bindings
* **Symptom:** Web browser threw a massive red system crash warning screen reading: `Cannot find native binding... Error: Cannot find module '@tailwindcss/oxide-win32-x64-msvc'`.
* **Root Cause:** Upgrading the underlying system's Node engine mid-flight left old compilation folders (`node_modules`) caching library files compiled for the wrong machine engine.
* **Resolution:** Used PowerShell terminal operations to drop the legacy folder paths via `Remove-Item -Recurse -Force .next, node_modules`, then re-fetched correct operating system binaries using `npm install`.

### Issue 5: Uvicorn Reloader Folder Recursion Crash
* **Symptom:** Python web server crashed out with a massive stream of `FileNotFoundError` logs pointing inside the front-end directory paths.
* **Root Cause:** Next.js creates hundreds of thousands of package assets within `frontend/node_modules/`. The standard Uvicorn `--reload` watcher tried scanning all of them, running out of file handles and crashing.
* **Resolution:** Modified the terminal launch script to run cleanly without the folder-scanning file watcher by passing a direct command execution structure: `uvicorn main:app`.

### Issue 6: Truncated Data Fetch Network Request
* **Symptom:** The Next.js dashboard banner read: `System Status Notice: Backend server connection error` and accuracy charts dropped to 0%.
* **Root Cause:** A critical string typo in the fetch request URL on line 10 of `page.tsx` truncated the query statement path down to `"http://127.0.0"`, dropping the port identifier and trailing routes entirely.
* **Resolution:** Corrected the route parameters inside VS Code to target the active server address: `http://127.0.0.1:8000` (or your exact target backend port). This restored cross-app network data parsing.

---

## 🏗️ 5. Architectural Flow Diagram

```text
[ Browser / Client Navigation ]
               │
               ▼
┌────────────────────────────────────────┐
│  Next.js Frontend (Port 3000)          │
│  - Asynchronous Server Component       │
│  - Requests telemetry via HTTP Fetch   │
└──────────────┬─────────────────────────┘
               │
               │ HTTP GET /evaluate
               ▼
┌────────────────────────────────────────┐
│  FastAPI Backend (Port 8000)           │
│  - Captures test parameters            │
│  - Triggers SQLite database mutation   │
└──────────────┬─────────────────────────┘
               │
               │ SQL INSERT
               ▼
┌────────────────────────────────────────┐
│  SQLite Local Database (ai_eval.db)    │
│  - Logs persistent historical scores   │
└────────────────────────────────────────┘
```


