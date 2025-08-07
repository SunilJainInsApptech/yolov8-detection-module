#!/usr/bin/env python3
"""
YOLOv8 Detection Module Main Entry Point
"""

import asyncio
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting YOLOv8 detection module...")

from viam.module.module import Module
from viam.services.vision import Vision

try:
    from models.yolov8_detection import YOLOv8DetectionService
    logger.info("YOLOv8DetectionService imported successfully.")
except ModuleNotFoundError:
    # When running as local module
    from .models.yolov8_detection import YOLOv8DetectionService
    logger.info("YOLOv8DetectionService imported successfully from local module.")

if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
