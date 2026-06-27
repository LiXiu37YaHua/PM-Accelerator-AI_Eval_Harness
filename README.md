# PM-Accelerator-AI_Eval_Harness

## 📊 Application Dashboard
<img width="1891" height="705" alt="Success USE" src="https://github.com/user-attachments/assets/7f5dab65-5529-44b9-9a6a-d3d7190e201a" />
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
