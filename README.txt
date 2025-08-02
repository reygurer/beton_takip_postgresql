
Concrete Production Tracking Application (PostgreSQL Version)

This project is a desktop application developed for tracking inventory, production, and sales in concrete paving stone businesses. It is built with Python and uses PostgreSQL for data storage. The application features a simple and functional GUI built with Tkinter.

Features

- Product and material registration
- Bill of materials (production recipes)
- Automatic stock deduction during production
- Sales tracking
- PostgreSQL database integration
- User-friendly interface with Tkinter

Technologies Used

- Python
- Tkinter (GUI)
- PostgreSQL (Database)
- psycopg2-binary (PostgreSQL connector)

Setup Instructions

1. Install Required Packages

    pip install psycopg2-binary

2. Create the PostgreSQL Database

    createdb beton_takip

3. Initialize Tables

Make sure the db.py file (or equivalent setup script) exists and includes your schema creation logic:

    python db.py

4. Run the Application

    python beton_takip_postgresql.py

Project Structure

beton_takip_postgresql/
├── beton_takip_postgresql.py     # Main application script with PostgreSQL support
├── db_config.py                  # Database connection using environment variables
├── .env                          # Contains DB credentials (excluded via .gitignore)
├── .gitignore                    # Git ignore rules to exclude sensitive and unwanted files
├── README.md                     # Project overview and documentation
├── excel_kayitlari/              # Folder where Excel reports are saved


Notes

- If your PostgreSQL server does not require a password, leave the password field empty in the connection string.
- You must initialize the database before running the application.

Author

Developed by @reygurer (https://github.com/reygurer)
