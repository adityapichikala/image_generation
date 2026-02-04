"""
SD-Turbo: Fast Local Image Generation
--------------------------------------
A minimal, production-ready implementation of Stable Diffusion Turbo
for ultra-fast image generation on local GPU.

Model: stabilityai/sd-turbo
Optimizations: FP16, xFormers, 1-4 inference steps
"""

import torch
from diffusers import AutoPipelineForText2Image
from PIL import Image
import time
from pathlib import Path


class SDTurboGenerator:
    """
    Fast image generator using SD-Turbo model with GPU acceleration.
    
    SD-Turbo is a distilled version of Stable Diffusion that can generate
    high-quality images in just 1-4 steps (vs 20-50 for standard SD).
    """
    
    def __init__(self, model_id: str = "stabilityai/sd-turbo", device: str = "cuda"):
        """
        Initialize the SD-Turbo pipeline with optimizations.
        
        Args:
            model_id: Hugging Face model identifier
            device: Device to run inference on ('cuda' or 'cpu')
        """
        # Auto-detect device if CUDA not available
        if device == "cuda" and not torch.cuda.is_available():
            print("WARNING: CUDA not available, using CPU (slower)")
            device = "cpu"
        
        self.device = device
        self.model_id = model_id
        
        print(f"Loading {model_id}...")
        print(f"Device: {device}")
        
        # Load pipeline with FP16 precision for faster inference (only on CUDA)
        if device == "cuda":
            self.pipe = AutoPipelineForText2Image.from_pretrained(
                model_id,
                torch_dtype=torch.float16,
                variant="fp16",
            )
        else:
            # CPU mode - use float32
            self.pipe = AutoPipelineForText2Image.from_pretrained(
                model_id,
                torch_dtype=torch.float32,
            )
        
        self.pipe = self.pipe.to(device)
        
        # Enable xFormers memory efficient attention (faster + less VRAM) - only on CUDA
        if device == "cuda":
            try:
                self.pipe.enable_xformers_memory_efficient_attention()
                print("xFormers enabled")
            except Exception as e:
                print(f"WARNING: xFormers not available: {e}")
        
        # Disable safety checker for speed (optional - enable in production)
        self.pipe.safety_checker = None
        
        print("Model loaded successfully\n")
    
    def generate(
        self,
        prompt: str,
        num_inference_steps: int = 1,
        guidance_scale: float = 0.0,
        width: int = 512,
        height: int = 512,
        seed: int = None
    ) -> Image.Image:
        """
        Generate an image from a text prompt.
        
        Args:
            prompt: Text description of desired image
            num_inference_steps: Number of denoising steps (1-4 for SD-Turbo)
            guidance_scale: Classifier-free guidance (0.0 for SD-Turbo)
            width: Output image width (default 512)
            height: Output image height (default 512)
            seed: Random seed for reproducibility
            
        Returns:
            PIL Image object
        """
        # Set random seed if provided
        generator = None
        if seed is not None:
            generator = torch.Generator(device=self.device).manual_seed(seed)
        
        start_time = time.time()
        
        # Generate image
        image = self.pipe(
            prompt=prompt,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            width=width,
            height=height,
            generator=generator,
        ).images[0]
        
        elapsed = time.time() - start_time
        print(f"Generated in {elapsed:.2f}s ({num_inference_steps} steps)")
        
        return image
    
    def generate_batch(
        self,
        prompts: list[str],
        num_inference_steps: int = 1,
        guidance_scale: float = 0.0,
        width: int = 512,
        height: int = 512,
    ) -> list[Image.Image]:
        """
        Generate multiple images in parallel (batch processing).
        
        Args:
            prompts: List of text prompts
            num_inference_steps: Number of denoising steps
            guidance_scale: Classifier-free guidance scale
            width: Output image width
            height: Output image height
            
        Returns:
            List of PIL Image objects
        """
        start_time = time.time()
        
        images = self.pipe(
            prompt=prompts,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            width=width,
            height=height,
        ).images
        
        elapsed = time.time() - start_time
        print(f"Generated {len(images)} images in {elapsed:.2f}s")
        
        return images


def main():
    """Demo: Generate sample images using SD-Turbo."""
    
    # Initialize generator
    generator = SDTurboGenerator()
    
    # Create output directory
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    
    # Example prompts
    prompts = [
        "A futuristic city at sunset, cyberpunk style, highly detailed",
        "A serene mountain landscape with a crystal clear lake",
        "A cute robot reading a book in a cozy library",
    ]
    
    print("=" * 60)
    print("GENERATING SAMPLE IMAGES")
    print("=" * 60)
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\n[{i}/{len(prompts)}] Prompt: {prompt}")
        
        # Generate image (1 step = fastest, 4 steps = better quality)
        image = generator.generate(
            prompt=prompt,
            num_inference_steps=1,  # Ultra-fast: 1 step
            seed=42 + i,  # Reproducible results
        )
        
        # Save image
        output_path = output_dir / f"sample_{i}.png"
        image.save(output_path)
        print(f"Saved to: {output_path}")
    
    print("\n" + "=" * 60)
    print("COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
