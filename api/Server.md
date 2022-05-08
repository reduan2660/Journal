### Gunicorn Server

```bash
gunicorn base.wsgi --bind=0000:8000 --reload --workers=2
```

--reload is only for development environment
