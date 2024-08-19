# resource_manager.py

class ResourceManager:
    _instance = None

    @staticmethod
    def get_instance():
        if ResourceManager._instance is None:
            ResourceManager._instance = ResourceManager()
        return ResourceManager._instance

    def __init__(self):
        if ResourceManager._instance is not None:
            raise Exception("This class is a singleton!")
        # Initialize pyvisa ResourceManager
        import pyvisa
        self.rm = pyvisa.ResourceManager()

    def list_resources(self):
        return self.rm.list_resources()
