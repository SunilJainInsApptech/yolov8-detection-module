
#!/usr/bin/env python3

import asyncio
import sys
import os
import traceback

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("🚀 STARTING YOLOv8 Detection Module")
print("=" * 60)
print(f"📍 Current working directory: {os.getcwd()}")
print(f"🐍 Python executable: {sys.executable}")
print(f"📚 Python version: {sys.version}")
print(f"🛤️  Python path: {sys.path}")
print(f"🌍 Environment variables:")
for key, value in sorted(os.environ.items()):
    if "VIAM" in key:
        print(f"   {key}={value}")

print("\n🔍 Checking imports...")
try:
    print("   ✓ Importing viam.module.module...")
    from viam.module.module import Module
    print("   ✓ Module imported successfully")
    
    print("   ✓ Importing viam.resource.registry...")
    from viam.resource.registry import Registry, ResourceCreatorRegistration
    print("   ✓ Registry imported successfully")
    
    print("   ✓ Importing viam.services.vision...")
    from viam.services.vision import Vision
    print("   ✓ Vision imported successfully")
    
    print("   ✓ Importing src.main...")
    from src.main import YOLOv8DetectionService
    print("   ✓ YOLOv8DetectionService imported successfully")
    
    print(f"   📊 YOLOv8DetectionService class: {YOLOv8DetectionService}")
    print(f"   🏷️  Model definition: {YOLOv8DetectionService.MODEL}")
    print(f"   🔧 Model family: {YOLOv8DetectionService.MODEL.model_family}")
    print(f"   📝 Model repr: {repr(YOLOv8DetectionService.MODEL)}")
    print(f"   🔍 Model attributes: {dir(YOLOv8DetectionService.MODEL)}")
    
except Exception as e:
    print(f"   ❌ Import failed: {e}")
    traceback.print_exc()
    raise

async def main():
    """Main entry point for the YOLOv8 detection module"""
    print("\n🏗️  Creating module...")
    try:
        print("   📋 Parsing command line arguments...")
        module = Module.from_args()
        print("   ✓ Module created successfully")
        
        print("   🔧 Registering YOLOv8 detection service...")
        print(f"   🏷️  Service MODEL: {YOLOv8DetectionService.MODEL}")
        print(f"   📝 Model name: {YOLOv8DetectionService.MODEL.name}")
        
        print("   🔧 Attempting module registration...")
        module.add_model_from_registry(YOLOv8DetectionService.MODEL, YOLOv8DetectionService)
        print("   ✓ Service registered successfully")
        
        print("\n🚀 Starting module...")
        await module.start()
        print("   ✓ Module started successfully")
        
    except Exception as e:
        print(f"   ❌ Error in main(): {e}")
        print("   📋 Full traceback:")
        traceback.print_exc()
        raise

if __name__ == "__main__":
    print("\n🎯 Running main function...")
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        traceback.print_exc()
        sys.exit(1)
