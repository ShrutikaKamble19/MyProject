import qrcode

def generate_qr_code(data, filename="qr_code.png"):
    """
    Generates a QR code for the provided data and saves it as an image file.
    
    Parameters:
        data (str): The data or link to encode in the QR code.
        filename (str): The filename for the saved QR code image (default: 'qr_code.png').

    Returns:
        None
    """
    # Create a QR code instance with default settings
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the image for the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the generated QR code image to a file
    img.save(filename)
    print(f"QR code saved as {filename}")

# Example usage
data = "https://www.example.com"
generate_qr_code(data)
