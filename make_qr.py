"""QR 12장(PNG+SVG) 만들기:  python -X utf8 make_qr.py https://주소  저장폴더"""
import sys, pathlib, re, qrcode, qrcode.image.svg
base = sys.argv[1].rstrip("/") + "/app/?book="
out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
src = (pathlib.Path(__file__).parent / "app" / "books.js").read_text(encoding="utf-8")
for i, t in re.findall(r'id: "(\d\d)", title: "([^"]+)"', src):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=30, border=4)
    q.add_data(base + i); q.make(fit=True)
    n = f"QR_{i}_{t}".replace(" ", "_").replace(",", "")
    q.make_image(fill_color="black", back_color="white").save(out / f"{n}.png")
    q.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(str(out / f"{n}.svg"))
print(base + "01 ~ 12")
