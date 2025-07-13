# GB Backend - Free Power BI PDF Course

This is a Flask backend service to email your Power BI PDF course on form submission.

## Deployment Steps
1. Upload this repo to GitHub
2. Connect GitHub repo to Render.com
3. In Render, set ENV variables:
   - `EMAIL` → your Gmail address
   - `EMAIL_PASS` → Gmail App Password (not normal password)
4. Start command: `python3 powerbi_server.py`
5. Add `Power_BI_Course.pdf` to the root folder
