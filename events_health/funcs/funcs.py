import qrcode

def QR_code(event_id,guest_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f'{guest_id}')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
