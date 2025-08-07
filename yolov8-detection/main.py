
#!/usr/bin/env python3

import asyncio
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

print("Starting YOLOv8 Detection Module...")

from viam.module.module import Module
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.services.vision import Vision
from src.main import YOLOv8DetectionService

print(f"Loaded YOLOv8DetectionService: {YOLOv8DetectionService}")
print(f"Model definition: {YOLOv8DetectionService.MODEL}")

async def main():
    """Main entry point for the YOLOv8 detection module"""
    try:
        print("Creating module...")
        module = Module.from_args()
        
        print("Registering model...")
        Registry.register_resource_creator(
            Vision.SUBTYPE,
            YOLOv8DetectionService.MODEL,
            ResourceCreatorRegistration(
                YOLOv8DetectionService.new,
                YOLOv8DetectionService.validate_config
            )
        )
        
        print("Starting module...")
        await module.start()
    except Exception as e:
        print(f"Error starting module: {e}")
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    asyncio.run(main())
