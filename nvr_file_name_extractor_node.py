import os

class NVRFileNameExtractorNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "extract_filename"

    CATEGORY = "File Operations"

    def extract_filename(self, file_path):
        # Extract the base filename without extension
        filename = os.path.basename(file_path)
        filename_without_extension = os.path.splitext(filename)[0]
        return (filename_without_extension,)

# This function needs to be added to register the node in ComfyUI
NODE_CLASS_MAPPINGS = {
    "NVRFileNameExtractor": NVRFileNameExtractorNode
}

# This function is needed to display the node in the UI with a custom name
NODE_DISPLAY_NAME_MAPPINGS = {
    "NVRFileNameExtractor": "NVR File Name Extractor"
}