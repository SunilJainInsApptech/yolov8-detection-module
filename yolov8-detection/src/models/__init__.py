# Register YOLOv8DetectionService with the Viam registry
from viam.services.vision import Vision
from viam.resource.registry import Registry, ResourceCreatorRegistration
from .yolov8_detection import YOLOv8DetectionService

Registry.register_resource_creator(
	Vision.API,
	YOLOv8DetectionService.MODEL,
	ResourceCreatorRegistration(
		YOLOv8DetectionService.new,
		YOLOv8DetectionService.validate_config
	)
)
