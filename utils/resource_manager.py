import pyvisa

class ResourceManager:
    @staticmethod
    def list_resources():
        try:
            rm = pyvisa.ResourceManager()
            resources = rm.list_resources()
            return resources
        except Exception as e:
            print(f"Error listing resources: {e}")
            return []

    @staticmethod
    def get_resource_info(resource):
        try:
            rm = pyvisa.ResourceManager()
            instrument = rm.open_resource(resource)
            info = instrument.query("*IDN?")
            return info
        except Exception as e:
            print(f"Error getting resource info: {e}")
            return "Unknown"
