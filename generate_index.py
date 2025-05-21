import os
import json

PHOTO_DIR = "photos"
OUTPUT_FILE = "index.html"

# Collect all image files (jpg, jpeg, png, webp)
photo_files = sorted(
    f for f in os.listdir(PHOTO_DIR)
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Photo Viewer</title>
  <style>
    body {{
      text-align: center;
      font-family: Arial, sans-serif;
      margin: 2rem;
    }}
    img {{
      max-width: 60vw;
      max-height: 60vh;
      object-fit: contain;
      border: 2px solid #ccc;
      border-radius: 8px;
      transition: transform 0.3s ease;
    }}
    button {{
      margin: 1rem 0.5rem;
      padding: 0.6rem 1.2rem;
      font-size: 1rem;
      cursor: pointer;
      border-radius: 5px;
      border: 1px solid #888;
      background: #eee;
      transition: background 0.2s;
    }}
    button:hover {{
      background: #ddd;
    }}
  </style>
</head>
<body>

<h1>Photo Viewer</h1>

<img id="photo" src="" alt="Photo" />

<div>
  <button onclick="prevPhoto()">⟵ Prev</button>
  <button onclick="nextPhoto()">Next ⟶</button>
  <button onclick="randomPhoto()">🎲 Random</button>
</div>

<script>
  const photos = {json.dumps(photo_files)};
  let index = 0;

  function showPhoto() {{
    const photoEl = document.getElementById("photo");
    photoEl.src = "{PHOTO_DIR}/" + photos[index];
  }}

  function nextPhoto() {{
    index = (index + 1) % photos.length;
    showPhoto();
  }}

  function prevPhoto() {{
    index = (index - 1 + photos.length) % photos.length;
    showPhoto();
  }}

  function randomPhoto() {{
    index = Math.floor(Math.random() * photos.length);
    showPhoto();
  }}

  // Listen for arrow key presses
  document.addEventListener("keydown", (e) => {{
    if (e.target.tagName === 'TEXTAREA' || e.target.tagName === 'INPUT') return; // ignore typing
    switch(e.key) {{
      case "ArrowLeft":
        prevPhoto();
        break;
      case "ArrowRight":
        nextPhoto();
        break;
      case "ArrowUp":
      case "ArrowDown":
        randomPhoto();
        break;
    }}
  }});

  // Show the first photo after DOM is loaded
  document.addEventListener("DOMContentLoaded", () => {{
    if (photos.length > 0) {{
      showPhoto();
    }} else {{
      document.getElementById("photo").alt = "No photos found";
    }}
  }});
</script>

</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ {OUTPUT_FILE} generated with {len(photo_files)} photos.")

