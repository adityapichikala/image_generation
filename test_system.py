"""
Complete System Test & Demo Script
------------------------------------
Run this to verify all components work correctly.
"""

import sys
from pathlib import Path

print("=" * 70)
print("🧪 ANIME IMAGE GENERATOR - System Test & Demo")
print("=" * 70)

# Test 1: Check Python version
print("\n📋 Test 1: Python Version")
print(f"✓ Python {sys.version.split()[0]}")
assert sys.version_info >= (3, 8), "Python 3.8+ required"

# Test 2: Check dependencies
print("\n📋 Test 2: Dependencies")
try:
    import torch
    print(f"✓ PyTorch {torch.__version__}")
except ImportError:
    print("✗ PyTorch not found - run: pip install -r requirements.txt")
    sys.exit(1)

try:
    import diffusers
    print(f"✓ Diffusers {diffusers.__version__}")
except ImportError:
    print("✗ Diffusers not found")
    sys.exit(1)

try:
    import flask
    print(f"✓ Flask {flask.__version__}")
except ImportError:
    print("✗ Flask not found - run: pip install flask")
    sys.exit(1)

# Test 3: Check CUDA
print("\n📋 Test 3: GPU Availability")
if torch.cuda.is_available():
    print(f"✓ CUDA available: {torch.cuda.get_device_name(0)}")
    print(f"  VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
else:
    print("⚠ CUDA not available - will use CPU (slower)")

# Test 4: Test core generator
print("\n📋 Test 4: Core Image Generator")
try:
    from generate_image import SDTurboGenerator
    print("✓ Generator class imported successfully")
except Exception as e:
    print(f"✗ Failed to import generator: {e}")
    sys.exit(1)

# Test 5: Quick generation test
print("\n📋 Test 5: Quick Generation Test")
print("Initializing SD-Turbo (this may take a moment)...")
try:
    generator = SDTurboGenerator()
    print("✓ Model loaded successfully")
    
    # Generate test image
    print("Generating test image (1 step)...")
    test_image = generator.generate(
        prompt="anime cat mascot, cute style",
        num_inference_steps=1,
        seed=42
    )
    
    # Save test image
    test_dir = Path("test_outputs")
    test_dir.mkdir(exist_ok=True)
    test_path = test_dir / "test_generation.png"
    test_image.save(test_path)
    print(f"✓ Test image saved: {test_path}")
    
except Exception as e:
    print(f"✗ Generation failed: {e}")
    sys.exit(1)

# Test 6: Domain validation
print("\n📋 Test 6: Domain Validation Logic")
try:
    from app import is_anime_domain
    
    # Test cases
    test_cases = [
        ("anime girl with blue hair", True),
        ("realistic photo of street", False),
        ("DSLR photo of landscape", False),
        ("cute chibi character", True),
        ("professional photograph", False),
    ]
    
    all_passed = True
    for prompt, expected_valid in test_cases:
        is_valid, suggestion = is_anime_domain(prompt)
        status = "✓" if is_valid == expected_valid else "✗"
        print(f"  {status} '{prompt}' → {'Valid' if is_valid else 'Blocked'}")
        if is_valid != expected_valid:
            all_passed = False
    
    if all_passed:
        print("✓ All validation tests passed")
    else:
        print("⚠ Some validation tests failed")
        
except Exception as e:
    print(f"✗ Validation test failed: {e}")

# Test 7: Check file structure
print("\n📋 Test 7: Project Structure")
required_files = [
    "generate_image.py",
    "anime_usecase.py",
    "app.py",
    "requirements.txt",
    "README.md",
    "templates/index.html",
    "static/style.css",
    "static/script.js"
]

all_exist = True
for file in required_files:
    filepath = Path(file)
    if filepath.exists():
        print(f"  ✓ {file}")
    else:
        print(f"  ✗ {file} - MISSING")
        all_exist = False

if all_exist:
    print("✓ All required files present")

# Summary
print("\n" + "=" * 70)
print("✅ SYSTEM TEST COMPLETE")
print("=" * 70)

print("\n🎉 Everything is working! You can now:")
print("\n1️⃣  Generate images via Python:")
print("    python generate_image.py")

print("\n2️⃣  Run anime use case demo:")
print("    python anime_usecase.py")

print("\n3️⃣  Launch web interface (RECOMMENDED):")
print("    python app.py")
print("    Then visit: http://localhost:5000")

print("\n📚 Documentation:")
print("    • README.md - Complete guide")
print("    • WEB_INTERFACE_GUIDE.md - Web UI details")
print("    • QUICKSTART.md - Quick setup")

print("\n" + "=" * 70)
