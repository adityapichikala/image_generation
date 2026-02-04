# 🎨 Web Frontend - Quick Demo

## Overview
Beautiful web interface with **intelligent anime domain validation** that prevents out-of-domain requests.

---

## 🚀 Launch in 3 Steps

```bash
# 1. Ensure Flask is installed
pip install flask

# 2. Start the server
python app.py

# 3. Open browser
# Visit: http://localhost:5000
```

---

## ✨ Key Features

### 1. **Domain Validation**
Automatically detects and blocks non-anime prompts:

**Example:**
- ❌ User enters: `"realistic photo of New York street"`
- 🔔 **Notification appears**: "Out of Domain Detected!"
- 💡 **Suggestion shown**: `"anime style, New York street"`
- ✅ User clicks "Use This Prompt" → Generates anime version

### 2. **Smart Suggestions**
System provides anime alternatives for all out-of-domain requests.

### 3. **Beautiful UI**
- Modern dark theme with purple/pink gradients  
- Mobile-responsive design
- Real-time generation preview
- One-click download

---

## 📸 Interface Preview

![Web UI Mockup](../../artifacts/web_ui_mockup.webp)
*Modern anime generator interface with gradient accents*

![Domain Notification](../../artifacts/domain_notification.webp)
*Out-of-domain warning with smart suggestion*

---

## 🎯 Example Workflows

### Valid Anime Generation ✅
1. Enter: `"anime magical girl with sparkles"`
2. Click "Generate"
3. View result in ~140ms
4. Download image

### Out-of-Domain Detection ⚠️
1. Enter: `"professional DSLR photo of street"`
2. System detects "DSLR photo" (realistic keyword)
3. Notification: "Out of Domain Detected!"
4. Suggestion: `"anime style, street"`
5. Click "Use This Prompt"
6. Generates anime-style street scene ✨

---

## 🎨 Domain Rules

**Anime Keywords** (Accepted):
- anime, manga, cartoon, character
- chibi, kawaii, magical girl
- fantasy, elf, dragon, spirit

**Realistic Keywords** (Blocked):
- photograph, photo, realistic
- DSLR, camera, candid
- photographic, portrait photo

---

## 🛠️ Customization

### Change Port
Edit `app.py`:
```python
app.run(debug=True, port=8080)  # Use port 8080
```

### Modify Colors
Edit `static/style.css`:
```css
:root {
    --primary: #7C3AED;  /* Change to your color */
}
```

### Adjust Validation
Edit `is_anime_domain()` in `app.py` to customize keywords.

---

## 📱 Mobile Support
Fully responsive - works on:
- ✅ Desktop
- ✅ Tablet  
- ✅ Mobile phones

---

## 🎉 Ready to Use!

```bash
python app.py
```

**Then visit:** http://localhost:5000

Start generating anime art with intelligent domain protection! 🚀
