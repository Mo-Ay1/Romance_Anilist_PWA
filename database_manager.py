# Romance AniList PWA

A basic but functional Progressive Web App built with **Python (Flask)**, **HTML**, **CSS**, **JavaScript**, and **SQLite**.

## Features

- Home page inspired by the storyboard layout
- Romance anime index page with search and filters
- Individual anime detail pages
- FAQ page
- SQLite-backed catalogue data
- Service worker for offline support
- Web app manifest for installability
- Local favourites using browser storage

## Run locally

```bash
pip install -r requirements.txt
python main.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## Main files

- `main.py` - Flask routes
- `database_manager.py` - SQLite setup and queries
- `database/setup.sql` - SQL schema
- `templates/` - HTML pages
- `static/css/style.css` - styling
- `static/js/app.js` - front-end behaviour
- `static/js/serviceworker.js` - offline caching
- `static/manifest.json` - PWA metadata
