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

def debug_log(msg):
    try:
        with open('/tmp/yolo_debug.log', 'a') as f:
            f.write(f"[main.py] {msg}\n")
    except Exception:
        pass

if __name__ == '__main__':
    debug_log(f"Invoked at {__import__('datetime').datetime.now()} with sys.argv: {sys.argv}")
    parser = argparse.ArgumentParser()
    parser.add_argument('--socket-path', type=str, required=True)
    args = parser.parse_args()
    sock_path = args.socket_path
    debug_log(f"Socket path resolved to: {sock_path}")
    # Clean up leftover socket file if it exists
    if os.path.exists(sock_path):
        try:
            os.remove(sock_path)
            logger.info(f"Removed stale socket file: {sock_path}")
            debug_log(f"Removed stale socket file: {sock_path}")
        except Exception as e:
            logger.error(f"Failed to remove stale socket file {sock_path}: {e}")
            debug_log(f"Failed to remove stale socket file {sock_path}: {e}")
    else:
        debug_log(f"No stale socket file found at: {sock_path}")
    debug_log("About to start Module.run_from_registry()")
    try:
        # Pass the socket path to the Viam SDK if supported
        asyncio.run(Module.run_from_registry())
        debug_log("Module.run_from_registry() exited cleanly")
    except Exception as e:
        debug_log(f"Exception in Module.run_from_registry(): {e}")
        raise
