# Quick Start Guide

## 🚀 Installation & Setup

### 1. Prerequisites Check

```bash
# Verify Python version (need 3.8+)
python --version

# Verify CUDA is available
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```

### 2. Install Dependencies

```bash
# Navigate to project directory
cd c:\Users\adity\OneDrive\Desktop\huggingface

# Install all requirements
pip install -r requirements.txt
```

**First run will download the model (~3.5 GB) from Hugging Face.**

### 3. Test Installation

```bash
# Quick test
python -c "from generate_image import SDTurboGenerator; print('✓ Import successful')"
```

### 4. Generate Your First Image

```bash
# Run the demo script
python generate_image.py
```

This will generate 3 sample images in the `outputs/` folder.

---

## 🎯 Quick Examples

### Example 1: Single Image

```python
from generate_image import SDTurboGenerator

generator = SDTurboGenerator()
image = generator.generate(
    prompt="A beautiful sunset over mountains",
    num_inference_steps=1,
)
image.save("my_image.png")
```

### Example 2: Anime Content Generation Use Case

```bash
python anime_usecase.py
```

Generates anime-style characters, scenes, and effects in `anime_outputs/`.

---

## ⚙️ Configuration

### Adjust Speed vs Quality

```python
# Fastest (1 step, ~50-100ms)
image = generator.generate(prompt, num_inference_steps=1)

# Better quality (2 steps, ~100-150ms)
image = generator.generate(prompt, num_inference_steps=2)

# Best quality (4 steps, ~200-300ms)
image = generator.generate(prompt, num_inference_steps=4)
```

### Custom Resolution

```python
# Higher resolution (needs more VRAM)
image = generator.generate(
    prompt="A serene lake",
    width=768,
    height=768,
    num_inference_steps=2
)
```

---

## 🐛 Troubleshooting

### "CUDA out of memory"
- Reduce image resolution
- Close other GPU applications
- Use batch_size=1

### "xFormers not available"
- Not critical - code will still work
- To install: `pip install xformers`

### Model download is slow
- First run downloads 3.5 GB
- Model is cached at `~/.cache/huggingface/`
- Subsequent runs are instant

---

## 📚 Next Steps

1. **Read the README**: Full documentation in `README.md`
2. **Deep dive**: Technical explanation in brain artifacts
3. **Customize**: Modify prompts for your use case
4. **Deploy**: See production tips in README

---

**Happy generating! 🎨**
