Railway deployment notes

1) Connect repo: In Railway, create a new project and connect your GitHub repo.

2) Environment variables: in Railway project settings add:
- SECRET_KEY: your secure secret
- DATABASE_URL: (use Railway Postgres add-on) e.g., postgresql://user:pass@host:port/dbname
- UPLOAD_FOLDER: optional if using external storage (see notes)

3) Add a Postgres plugin (recommended) and copy the DATABASE_URL into env vars.

4) Build & Start: Railway will detect the Procfile; start command is:

    web: gunicorn -k eventlet -w 1 wsgi:application

5) Database initialization:
- Run `python init_db.py` from Railway's run console or using the Railway CLI to create tables.

6) File uploads & static files:
- Railway's filesystem is ephemeral; uploaded files will not persist between deploys.
- For persistent uploads, configure S3 (or other object storage) and set `UPLOAD_FOLDER` to use S3 paths, or modify the app to upload files to S3.

7) WebSockets:
- Gunicorn with the `eventlet` worker supports Flask-SocketIO real-time features.

8) Debug/production:
- Ensure `SECRET_KEY` is set and avoid running with debug enabled in production.

9) Troubleshooting:
- If the app fails to start, check Railway deploy logs and the `web` service logs.
- If packages fail to install due to size, consider slimming `requirements.txt` or use Railway's disk upgrade.

If you want, I can:
- Add basic S3 upload support to the app (requires AWS credentials env vars).
- Prepare a small `railway` CLI script to initialize DB and push migrations.

Which would you like next?