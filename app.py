"""
Flask Web Application for Anime Image Generation
-------------------------------------------------
Features:
- Beautiful web interface for anime content generation
- Domain validation - detects non-anime prompts
- Real-time notifications for out-of-domain requests
- Image gallery display
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
from generate_image import SDTurboGenerator
from pathlib import Path
import base64
from io import BytesIO
import re

app = Flask(__name__)

# Initialize generator (loads model once)
print("Loading SD-Turbo model...")
generator = SDTurboGenerator()
print("Model ready!\n")

# Output directory
OUTPUT_DIR = Path("web_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def is_anime_domain(prompt: str) -> tuple[bool, str]:
    """
    Check if prompt is within anime/animated domain.
    
    Returns:
        (is_valid, suggestion) - is_valid=True if anime-related, 
                                 suggestion provides anime alternative
    """
    prompt_lower = prompt.lower()
    
    # Keywords that indicate anime/animation domain
    anime_keywords = [
        'anime', 'manga', 'cartoon', 'animated', 'chibi', 'kawaii',
        'character', 'hero', 'villain', 'magical girl', 'mecha',
        'fantasy', 'elf', 'dragon', 'spirit', 'creature',
        'cel shaded', 'illustrated', 'comic', 'stylized'
    ]
    
    # Keywords that indicate out-of-domain (realistic/photographic)
    realistic_keywords = [
        'photograph', 'photo', 'realistic', 'real life', 'photographic',
        'portrait photo', 'candid', 'documentary', 'street photography',
        'professional photo', 'hdr photo', 'dslr', 'camera'
    ]
    
    # Check for explicit realistic requests
    for keyword in realistic_keywords:
        if keyword in prompt_lower:
            # Generate anime alternative suggestion
            anime_version = prompt.replace(keyword, '').strip()
            if not anime_version:
                anime_version = "an anime scene"
            suggestion = f"anime style, {anime_version}"
            return False, suggestion
    
    # Check if explicitly anime-themed
    has_anime_keyword = any(keyword in prompt_lower for keyword in anime_keywords)
    
    # If no anime keywords and contains specific non-anime terms
    non_anime_indicators = ['real', 'actual', 'photorealistic', 'lifelike']
    has_non_anime = any(indicator in prompt_lower for indicator in non_anime_indicators)
    
    if has_non_anime and not has_anime_keyword:
        suggestion = f"anime style, {prompt}"
        return False, suggestion
    
    # If neutral prompt (no clear indication), allow but suggest anime enhancement
    if not has_anime_keyword:
        suggestion = f"anime style, {prompt}"
        return True, suggestion  # Allow but provide suggestion
    
    # Valid anime prompt
    return True, prompt


@app.route('/')
def index():
    """Serve the main web interface."""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """
    Generate anime image from prompt.
    Validates domain and returns appropriate response.
    """
    data = request.json
    prompt = data.get('prompt', '').strip()
    steps = int(data.get('steps', 2))
    
    if not prompt:
        return jsonify({
            'error': True,
            'message': 'Please enter a prompt!'
        }), 400
    
    # Domain validation
    is_valid, suggestion = is_anime_domain(prompt)
    
    if not is_valid:
        return jsonify({
            'error': True,
            'out_of_domain': True,
            'message': 'WARNING: Out of Domain Detected!',
            'details': 'This system is specialized for <strong>anime and animated content</strong>. Your prompt appears to request realistic/photographic imagery.',
            'suggestion': suggestion,
            'original_prompt': prompt
        }), 400
    
    try:
        # Generate image
        image = generator.generate(
            prompt=prompt,
            num_inference_steps=steps,
        )
        
        # Save to disk first (more reliable on Windows)
        filename = f"anime_{len(list(OUTPUT_DIR.glob('*.png'))) + 1}.png"
        filepath = OUTPUT_DIR / filename
        
        # Save using string path for Windows compatibility
        image.save(str(filepath), format="PNG")
        
        # Convert to base64 for web display
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        buffered.seek(0)  # Ensure we're at the start of the buffer
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return jsonify({
            'success': True,
            'image': f'data:image/png;base64,{img_str}',
            'prompt': prompt,
            'steps': steps,
            'filename': filename
        })
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"ERROR in generate: {error_details}")
        return jsonify({
            'error': True,
            'message': f'Generation failed: {str(e)}'
        }), 500


@app.route('/suggest', methods=['POST'])
def suggest_anime_prompt():
    """Convert user's prompt to anime-style suggestion."""
    data = request.json
    prompt = data.get('prompt', '').strip()
    
    is_valid, suggestion = is_anime_domain(prompt)
    
    return jsonify({
        'suggestion': suggestion,
        'is_anime': is_valid
    })


@app.route('/outputs/<filename>')
def serve_image(filename):
    """Serve generated images."""
    return send_from_directory(OUTPUT_DIR, filename)


if __name__ == '__main__':
    print("=" * 60)
    print("ANIME IMAGE GENERATOR - Web Interface")
    print("=" * 60)
    print("\nServer starting at: http://localhost:5000")
    print("\nFeatures:")
    print("  - Anime domain validation")
    print("  - Out-of-domain notifications")
    print("  - Real-time image generation")
    print("  - Beautiful modern UI")
    print("\nModel: SD-Turbo (loaded and ready)")
    print("\nPress Ctrl+C to stop\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
