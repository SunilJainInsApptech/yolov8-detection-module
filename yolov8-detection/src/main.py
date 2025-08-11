#!/usr/bin/env python3
"""
YOLOv8 Detection Module Main Entry Point
"""

import asyncio
import logging

import os

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

import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--socket-path', type=str, default='/tmp/yolov8_module.sock')
    args = parser.parse_args()
    sock_path = args.socket_path
    # Clean up leftover socket file if it exists
    if os.path.exists(sock_path):
        try:
            os.remove(sock_path)
            logger.info(f"Removed stale socket file: {sock_path}")
        except Exception as e:
            logger.error(f"Failed to remove stale socket file {sock_path}: {e}")
    asyncio.run(Module.run_from_registry())
