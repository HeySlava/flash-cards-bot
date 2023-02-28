from __future__ import annotations


with open('.env') as f:
    lines = f.readlines()
    TOKEN = lines[0].split('=')[-1].strip()
    ADMIN_ID = lines[1].split('=')[-1].strip()
