"""
USE CASE: Anime & Animated Visual Content Generation
----------------------------------------------------
Generate anime-style characters, scenes, and visual assets for:
- Animation studios and indie creators
- Game development (character concepts, backgrounds)
- Manga and comic book artists (reference materials)
- Content creators and streamers (custom avatars, thumbnails)

This demonstrates how SD-Turbo enables FAST iteration for creative workflows,
allowing artists to rapidly prototype ideas and generate reference materials.
"""

from generate_image import SDTurboGenerator
from pathlib import Path
import time


def generate_anime_assets():
    """
    Generate a diverse set of anime-style visual assets.
    
    Use Case: Rapid prototyping for animation and game development
    - Fast iteration allows artists to explore multiple concepts
    - No internet required - works in offline studios
    - Free - eliminates concept art licensing costs
    - Consistent style - helps maintain visual coherence
    """
    
    print("=" * 70)
    print("🎨 ANIME & ANIMATED CONTENT GENERATION SYSTEM")
    print("=" * 70)
    print("\nInitializing SD-Turbo generator...")
    
    # Initialize generator
    generator = SDTurboGenerator()
    
    # Create output directory
    output_dir = Path("anime_outputs")
    output_dir.mkdir(exist_ok=True)
    
    # Anime-focused prompts across different categories
    anime_prompts = {
        # Character Concepts
        "hero_character": "anime hero character with spiky blue hair, determined expression, action pose, vibrant colors",
        "magical_girl": "magical girl anime character, pastel pink dress, sparkles and stars, cute aesthetic",
        "villain_design": "anime villain character design, dark purple coat, mysterious aura, dramatic lighting",
        "chibi_mascot": "cute chibi mascot character, big eyes, cheerful expression, kawaii style",
        
        # Scene Backgrounds
        "tokyo_street": "anime style Tokyo street at night, neon signs, vibrant colors, cyberpunk aesthetic",
        "fantasy_castle": "anime fantasy castle on clouds, magical atmosphere, sunset sky, detailed architecture",
        "school_courtyard": "anime school courtyard with cherry blossoms, spring day, peaceful atmosphere",
        
        # Action & Effects
        "energy_blast": "anime energy blast effect, blue lightning, dynamic motion, action scene",
        "transformation": "magical girl transformation sequence, sparkles and ribbons, bright colors",
        
        # Creatures & Companions
        "spirit_creature": "cute anime spirit creature, glowing eyes, ethereal appearance, fantasy design",
        "dragon_companion": "anime style baby dragon, colorful scales, friendly expression, adventure theme",
        
        # Environmental Elements
        "sunset_vista": "anime style sunset over ocean, vibrant orange and pink sky, peaceful scenery",
    }
    
    print(f"\n🎬 Generating {len(anime_prompts)} anime-style assets...")
    print("Use: Concept art, character design, game development, animation reference\n")
    
    start_time = time.time()
    
    for i, (category, prompt) in enumerate(anime_prompts.items(), 1):
        print(f"[{i}/{len(anime_prompts)}] Category: {category}")
        print(f"    Prompt: {prompt}")
        
        # Generate image with 2 steps for better quality
        image = generator.generate(
            prompt=prompt,
            num_inference_steps=2,  # Balance speed and quality
            seed=200 + i,
        )
        
        # Save with descriptive filename
        output_path = output_dir / f"{category}.png"
        image.save(output_path)
        print(f"    ✓ Saved: {output_path}\n")
    
    total_time = time.time() - start_time
    avg_time = total_time / len(anime_prompts)
    
    print("=" * 70)
    print("✓ ASSET GENERATION COMPLETE")
    print("=" * 70)
    print(f"Total assets: {len(anime_prompts)}")
    print(f"Total time: {total_time:.2f}s")
    print(f"Average time per asset: {avg_time:.2f}s")
    print(f"\n💡 USE CASE BENEFITS:")
    print("  • RAPID ITERATION: Generate dozens of concepts in minutes")
    print("  • STYLE EXPLORATION: Test different aesthetics instantly")
    print("  • REFERENCE LIBRARY: Build custom visual reference collections")
    print("  • COST SAVINGS: Eliminate stock image and concept art licensing")
    print("  • OFFLINE WORKFLOW: Perfect for studios without constant internet")
    print("  • REAL-TIME COLLABORATION: Show clients concepts during meetings")
    print("\n📁 Output directory: anime_outputs/")
    print("=" * 70)


def character_variations():
    """
    Generate variations of a single character concept.
    Useful for exploring different designs quickly.
    """
    print("\n" + "=" * 70)
    print("🎭 CHARACTER VARIATION GENERATOR")
    print("=" * 70)
    
    generator = SDTurboGenerator()
    output_dir = Path("anime_outputs/character_variations")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Base character concept
    base_concept = "anime warrior character"
    
    # Different style variations
    variations = {
        "classic": f"{base_concept}, traditional anime style, clean lines",
        "cyberpunk": f"{base_concept}, cyberpunk aesthetic, neon accents, futuristic",
        "fantasy": f"{base_concept}, fantasy RPG style, magical armor, ethereal",
        "dark": f"{base_concept}, dark fantasy, gothic aesthetic, dramatic shadows",
        "cute": f"{base_concept}, chibi cute style, soft colors, friendly",
    }
    
    print(f"\n🎨 Generating {len(variations)} variations of: '{base_concept}'\n")
    
    for style, prompt in variations.items():
        print(f"Style: {style}")
        image = generator.generate(prompt, num_inference_steps=2, seed=300)
        output_path = output_dir / f"warrior_{style}.png"
        image.save(output_path)
        print(f"✓ Saved: {output_path}\n")
    
    print("=" * 70)
    print("✓ VARIATIONS COMPLETE")
    print(f"📁 Check: {output_dir}/")
    print("=" * 70)


def interactive_anime_mode():
    """
    Interactive mode for anime creators to generate custom concepts.
    """
    print("\n" + "=" * 70)
    print("🎨 INTERACTIVE ANIME CREATOR")
    print("=" * 70)
    
    generator = SDTurboGenerator()
    output_dir = Path("anime_outputs")
    output_dir.mkdir(exist_ok=True)
    
    print("\nGenerate custom anime-style images from your prompts!")
    print("Tips:")
    print("  - Include 'anime style' in your prompt for best results")
    print("  - Describe character features, colors, mood, setting")
    print("  - Example: 'anime girl with silver hair in futuristic city, neon lights'")
    print("\nType 'quit' to exit\n")
    
    counter = 1
    while True:
        user_prompt = input(f"\n[Image {counter}] Anime prompt: ").strip()
        
        if user_prompt.lower() in ['quit', 'exit', 'q']:
            print("\n✓ Exiting interactive mode")
            break
        
        if not user_prompt:
            continue
        
        # Auto-add anime style if not mentioned
        if 'anime' not in user_prompt.lower():
            user_prompt = f"anime style, {user_prompt}"
        
        print(f"Generating: {user_prompt}")
        
        # Generate image
        image = generator.generate(
            prompt=user_prompt,
            num_inference_steps=2,
        )
        
        # Save image
        output_path = output_dir / f"custom_anime_{counter}.png"
        image.save(output_path)
        print(f"✓ Saved: {output_path}")
        
        counter += 1


def batch_thumbnail_generation():
    """
    Generate anime-style thumbnails for content creators.
    Perfect for YouTube, Twitch, social media.
    """
    print("\n" + "=" * 70)
    print("🖼️ ANIME THUMBNAIL GENERATOR")
    print("=" * 70)
    
    generator = SDTurboGenerator()
    output_dir = Path("anime_outputs/thumbnails")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Thumbnail concepts for different content types
    thumbnails = {
        "gaming": "anime gamer character with headphones, excited expression, vibrant colors",
        "tutorial": "anime teacher character pointing at screen, friendly smile, educational vibe",
        "reaction": "anime character shocked expression, dramatic lighting, bold colors",
        "review": "anime character with stars and sparkles, happy expression, colorful background",
    }
    
    print("\n🎬 Generating content creator thumbnails...\n")
    
    for content_type, prompt in thumbnails.items():
        print(f"Type: {content_type}")
        image = generator.generate(prompt, num_inference_steps=2)
        output_path = output_dir / f"thumbnail_{content_type}.png"
        image.save(output_path)
        print(f"✓ Saved: {output_path}\n")
    
    print("=" * 70)
    print("✓ THUMBNAILS READY")
    print(f"📁 Output: {output_dir}/")
    print("=" * 70)


if __name__ == "__main__":
    # Generate comprehensive anime asset library
    generate_anime_assets()
    
    # Optional: Uncomment to explore additional features
    # character_variations()
    # batch_thumbnail_generation()
    # interactive_anime_mode()
