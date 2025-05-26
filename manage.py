#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# from dotenv import load_dotenv


def main():
    """Run administrative tasks."""

    # loaded_successfully = load_dotenv()
    # print(f"manage.py: Attempted to load .env. Success: {loaded_successfully}")
    # print(f"manage.py: GOOGLE_API_KEY after load_dotenv: {os.getenv('GOOGLE_API_KEY')}")

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
