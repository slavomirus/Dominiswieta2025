import qrcode
import sys

def generate_qr(url, output_file="site_qr.png"):
    """
    Generuje kod QR dla podanego linku.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"Kod QR został zapisany jako {output_file}")

if __name__ == "__main__":
    # Domyślny link - użytkownik powinien go zmienić na swój link do GitHub Pages
    # np. https://twojanazwa.github.io/nazwa-repozytorium/
    target_url = "https://slavomirus.github.io/Dominiswieta2025"
    
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
        
    print(f"Generowanie kodu QR dla: {target_url}")
    generate_qr(target_url)
