import qrcode


def get_qrcode(url="https://google.com", name="default"):
    qr = qrcode.make(data=url)
    qr.save(stream=f"{name}.png")

    return f"QR code was created! Open the {name}.png"


def main():
    get_qrcode(url="https://youtube.com", name="youtube")


if __name__ == "__main__":
    main()
