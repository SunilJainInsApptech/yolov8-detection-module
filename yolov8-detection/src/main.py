#!/usr/bin/env python3
"""
YOLOv8 Detection Module Main Entry Point
"""

import asyncio
import logging
import os
import sys
import argparse
import signal

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
    from .models.yolov8_detection import YOLOv8DetectionService
    logger.info("YOLOv8DetectionService imported successfully from local module.")

async def main(socket_path: str):
    """This function creates and starts a new module, after adding all desired resources."""
    module = Module(socket_path)
    module.add_model_from_registry(Vision.API, YOLOv8DetectionService.MODEL)
    await module.start()

def debug_log(msg):
    try:
        with open('/tmp/yolo_debug.log', 'a') as f:
            f.write(f"[main.py] {msg}\n")
    except Exception:
        pass

if __name__ == '__main__':
    debug_log(f"Invoked at {__import__('datetime').datetime.now()} with sys.argv: {sys.argv}")
    
    if len(sys.argv) < 2:
        raise Exception("Need socket path as command line argument")
    
    socket_path = sys.argv[1]
    debug_log(f"Socket path resolved to: {socket_path}")

    # Remove stale socket file at startup
    if os.path.isdir(socket_path):
        logger.error(f"Socket path {socket_path} is a directory, not a file. Please remove it.")
        debug_log(f"Socket path {socket_path} is a directory, not a file. Please remove it.")
        sys.exit(1)
    elif os.path.exists(socket_path):
        try:
            os.remove(socket_path)
            logger.info(f"Cleaned up socket file: {socket_path}")
            debug_log(f"Cleaned up socket file: {socket_path}")
        except Exception as e:
            logger.error(f"Failed to clean up socket file {socket_path}: {e}")
            debug_log(f"Failed to clean up socket file {socket_path}: {e}")

    debug_log("About to start module")
    try:
        asyncio.run(main(socket_path))
        debug_log("Module exited cleanly")
    except Exception as e:
        debug_log(f"Exception in module: {e}")
        raise