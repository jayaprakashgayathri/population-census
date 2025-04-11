# Population Census Data Portal

This project is a web-based application designed to visualize and manage population census data. Built with Python and Flask, it provides interactive dashboards and tools for analyzing demographic metrics such as birth rate, mortality, income, and sex ratio.

## Features

- Interactive Dashboards: Visual representations of various demographic metrics.
- Data Management: Add, edit, and manage census data through a user-friendly interface.
- Authentication: Secure login system for authorized data access.
- Responsive Design: Clean and responsive UI using HTML, CSS, and JavaScript.

## Project Structure

```
├── app.py                 # Main Flask application
├── create-db.py           # Script to initialize the SQLite database
├── census.db              # SQLite database file
├── world_population.csv   # Dataset containing world population data
├── templates/             # HTML templates for different pages
│   ├── index.html
│   ├── homepage.html
│   ├── birthrate.html
│   ├── mortality.html
│   ├── income.html
│   ├── sexratio.html
│   └── add-edit-data.html
├── static/                # Static files (CSS, JS)
│   ├── styles.css
│   ├── sidebar.js
│   ├── birthrate.css
│   ├── mortality.css
│   ├── income.css
│   ├── sexratio.css
│   └── add-edit-data.css
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jayaprakashgayathri/population-census.git
cd population-census
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Initialize the database:

```bash
python create-db.py
```

5. Run the application:

```bash
python app.py
```

6. Access the application:

Open your browser and navigate to `http://127.0.0.1:5000/`

## Data Source

The application utilizes the `world_population.csv` dataset, which contains global population statistics. Ensure this file is present in the project directory for the application to function correctly.

## requirements.txt

```txt
Flask==2.2.5
pandas==2.1.4
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is open-source and available under the MIT License.
