
#!/usr/bin/env python3

import asyncio
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

print("Starting YOLOv8 Detection Module...")
print(f"Python path: {sys.path}")
print(f"Current working directory: {os.getcwd()}")

from viam.module.module import Module
from src.main import YOLOv8DetectionService

print(f"Loaded YOLOv8DetectionService: {YOLOv8DetectionService}")
print(f"Model definition: {YOLOv8DetectionService.MODEL}")

async def main():
    """Main entry point for the YOLOv8 detection module"""
    print("Creating module...")
    module = Module.from_args()
    print("Adding model to registry...")
    module.add_model_from_registry(YOLOv8DetectionService.MODEL, YOLOv8DetectionService)
    print("Starting module...")
    await module.start()

if __name__ == "__main__":
    asyncio.run(main())
