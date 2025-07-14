from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

PDF_PATH = "Power_BI_Course.pdf"

@app.route("/")
def home():
    return "GB Academy Flask Backend is Running"

@app.route("/send-pdf", methods=["POST"])
def send_pdf():
    data = request.get_json()
    email = data.get("email")
    payment_id = data.get("payment_id")

    if not email or not payment_id:
        return "Missing email or payment ID", 400

    try:
        EMAIL_ADDRESS = os.environ.get("EMAIL")
        EMAIL_PASS = os.environ.get("EMAIL_PASS")

        msg = EmailMessage()
        msg["Subject"] = "Your Power BI Masterclass PDF - GB Academy"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = email
        msg.set_content("Thank you for your payment. Your Power BI PDF is attached.")

        with open(PDF_PATH, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="Power_BI_Course.pdf")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
            smtp.send_message(msg)

        return "PDF sent successfully", 200

    except Exception as e:
        return f"Failed to send PDF: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
