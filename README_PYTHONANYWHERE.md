Deployment notes for PythonAnywhere

1) Upload project files to your PythonAnywhere account (use the Files page or git).

2) Create a virtualenv on PythonAnywhere and install dependencies:

```bash
python3 -m venv ~/.virtualenvs/social_platform
source ~/.virtualenvs/social_platform/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

3) In the web app configuration (Web tab) set the WSGI configuration file to point to this project's `wsgi.py`.

4) Set environment variables in the Web tab:
- `SECRET_KEY`: a secure secret string
- Optional: `DATABASE_URL` to override the default SQLite path (defaults to sqlite:///instance/social_platform.db)

5) Ensure the `instance` folder exists and is writable. The app stores the SQLite DB and uploads under `instance/`.

6) Initialize the database once (SSH into console or use the Bash console):

```bash
source ~/.virtualenvs/social_platform/bin/activate
python init_db.py
```

7) Static files are served by the WSGI server; uploaded media is kept in `instance/uploads`.

Notes and caveats:
- PythonAnywhere's free plans may not support WebSocket connections used by `flask-socketio`. If you require real-time sockets in production, consider a separate SocketIO-capable host (e.g., a VPS) or use a long-polling fallback.
- Make sure to set `SECRET_KEY` in the Web UI before going public.
