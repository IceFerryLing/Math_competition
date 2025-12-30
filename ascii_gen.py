from PIL import Image, ImageDraw, ImageFont
import itertools

text_lines = [
"╔══════════════════════════════════════════════════╗",
"║                                                  ║",
"║   ███╗   ███╗ █████╗ ████████╗██╗  ██╗           ║",
"║   ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║           ║",
"║   ██╔████╔██║███████║   ██║   ███████║           ║",
"║   ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║           ║",
"║   ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║           ║",
"║   ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝           ║",
"║                                                  ║",
"║   ███████╗████████╗ █████╗ ██████╗ ████████╗     ║",
"║   ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝     ║",
"║   ███████╗   ██║   ███████║██████╔╝   ██║        ║",
"║   ╚════██║   ██║   ██╔══██║██╔══██╗   ██║        ║",
"║   ███████║   ██║   ██║  ██║██║  ██║   ██║        ║",
"║   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ║",
"║                                                  ║",
"╚══════════════════════════════════════════════════╝",
]

font = ImageFont.load_default()
line_height = 16
padding = 12
width = max(font.getbbox(line)[2] for line in text_lines) + padding * 2
height = line_height * len(text_lines) + padding * 2

frames = []
colors = ["#ff6b6b", "#feca57", "#48dbfb", "#5f27cd"]

for i, color in enumerate(itertools.cycle(colors)):
    if i >= 20:
        break
    img = Image.new("RGB", (width, height), color="#0b0b10")
    draw = ImageDraw.Draw(img)
    for idx, line in enumerate(text_lines):
        y = padding + idx * line_height
        draw.text((padding, y), line, font=font, fill=color)
    frames.append(img)

durations = [80] * len(frames)
frames[0].save(
    "ascii-animated.gif",
    save_all=True,
    append_images=frames[1:],
    duration=durations,
    loop=0,
    disposal=2,
)
print("gif generated", width, height, len(frames))
