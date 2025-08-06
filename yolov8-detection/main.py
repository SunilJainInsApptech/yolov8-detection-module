
# Module entry point
async def main():
    """Main entry point for the YOLOv8 detection module"""
    from viam.module.module import Module
    module = Module.from_args()
    module.add_model_from_registry(YOLOv8DetectionService.MODEL, YOLOv8DetectionService)
    await module.start()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
