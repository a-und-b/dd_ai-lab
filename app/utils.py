import os
import qrcode
from io import BytesIO


def create_job_directories(job_id):
    base_path = f"app/static/jobs/{job_id}"
    directories = [
        base_path,
        f"{base_path}/text",
        f"{base_path}/raw",
        f"{base_path}/controlnet_assets",
        f"{base_path}/ipadapter",
        f"{base_path}/masks",
        f"{base_path}/generated_images",
        f"{base_path}/final_images",
        f"{base_path}/assets"
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def generate_qr_code(job_id, job_url):
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=0)
    qr.add_data(job_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, "PNG")

    with open(f"app/static/jobs/{job_id}/assets/qr_code.png", "wb") as f:
        f.write(buffer.getvalue())
