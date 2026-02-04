"""
USE CASE: Smart Agriculture - Crop Disease Visualization
---------------------------------------------------------
Generate visual references for crop diseases and healthy crops
to train farmers and agricultural workers.

This demonstrates how SD-Turbo can be used for rapid generation
of educational and reference materials in agriculture.
"""

from generate_image import SDTurboGenerator
from pathlib import Path
import time


def generate_agriculture_dataset():
    """
    Generate a dataset of crop images for agricultural education.
    
    Use Case: Training farmers to identify crop diseases and optimal conditions
    - Fast generation allows real-time visual aids during training
    - No internet required - works in remote farming areas
    - Free and open-source - accessible to all farmers
    """
    
    print("=" * 70)
    print("SMART AGRICULTURE: Crop Disease Visualization System")
    print("=" * 70)
    print("\nInitializing SD-Turbo generator...")
    
    # Initialize generator
    generator = SDTurboGenerator()
    
    # Create output directory
    output_dir = Path("agriculture_outputs")
    output_dir.mkdir(exist_ok=True)
    
    # Agricultural prompts - diseases and healthy references
    agriculture_prompts = {
        "healthy_tomato": "healthy tomato plant with ripe red tomatoes, vibrant green leaves, agricultural photo",
        "tomato_blight": "tomato plant with late blight disease, brown spots on leaves, agricultural reference photo",
        "healthy_wheat": "healthy golden wheat field ready for harvest, agricultural landscape",
        "wheat_rust": "wheat plant affected by rust disease, orange pustules on leaves, agricultural closeup",
        "healthy_corn": "healthy corn stalks with green leaves in a field, agricultural photo",
        "corn_smut": "corn plant with corn smut disease, black galls on ears, agricultural reference",
        "irrigation_system": "modern drip irrigation system in a vegetable farm, efficient water management",
        "soil_health": "rich dark healthy soil with earthworms, good agricultural soil texture",
    }
    
    print(f"\n📊 Generating {len(agriculture_prompts)} reference images...")
    print("Use: Educational material for farmer training programs\n")
    
    start_time = time.time()
    
    for i, (category, prompt) in enumerate(agriculture_prompts.items(), 1):
        print(f"[{i}/{len(agriculture_prompts)}] Category: {category}")
        print(f"    Prompt: {prompt}")
        
        # Generate image with 2 steps for better quality (still very fast)
        image = generator.generate(
            prompt=prompt,
            num_inference_steps=2,  # 2 steps for better quality
            seed=100 + i,
        )
        
        # Save with descriptive filename
        output_path = output_dir / f"{category}.png"
        image.save(output_path)
        print(f"    ✓ Saved: {output_path}\n")
    
    total_time = time.time() - start_time
    avg_time = total_time / len(agriculture_prompts)
    
    print("=" * 70)
    print("✓ DATASET GENERATION COMPLETE")
    print("=" * 70)
    print(f"Total images: {len(agriculture_prompts)}")
    print(f"Total time: {total_time:.2f}s")
    print(f"Average time per image: {avg_time:.2f}s")
    print(f"\n💡 USE CASE BENEFITS:")
    print("  • Fast generation enables real-time training sessions")
    print("  • Works offline - critical for remote farming areas")  
    print("  • Free - no API costs for resource-constrained farmers")
    print("  • Customizable - generate specific crop/disease combinations")
    print("  • Scalable - can generate thousands of reference images")
    print("\n📁 Output directory: agriculture_outputs/")
    print("=" * 70)


def interactive_mode():
    """
    Interactive mode for farmers to generate custom crop references.
    """
    print("\n" + "=" * 70)
    print("INTERACTIVE MODE: Custom Crop Visualization")
    print("=" * 70)
    
    generator = SDTurboGenerator()
    output_dir = Path("agriculture_outputs")
    output_dir.mkdir(exist_ok=True)
    
    print("\nEnter crop descriptions to generate reference images.")
    print("Example: 'healthy rice paddy field with water' or 'type 'quit' to exit\n")
    
    counter = 1
    while True:
        user_prompt = input(f"\n[Image {counter}] Enter description: ").strip()
        
        if user_prompt.lower() in ['quit', 'exit', 'q']:
            print("\n✓ Exiting interactive mode")
            break
        
        if not user_prompt:
            continue
        
        # Generate image
        image = generator.generate(
            prompt=user_prompt,
            num_inference_steps=2,
        )
        
        # Save image
        output_path = output_dir / f"custom_{counter}.png"
        image.save(output_path)
        print(f"✓ Saved: {output_path}")
        
        counter += 1


if __name__ == "__main__":
    # Generate predefined agriculture dataset
    generate_agriculture_dataset()
    
    # Optional: Uncomment to enable interactive mode
    # interactive_mode()
