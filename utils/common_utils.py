import json
import os, shutil

class CommonUtils:

    CONFIG_PATH = "config.ini"
    DEFAULT_WAIT_TIME = 30
    DYNAMIC_WAIT_TIME =20
    SUPPORTED_BROWSERS = ["chrome"]
    DEFAULT_URL = "https://www.flipkart.com/"
    HEADLESS = False

    @staticmethod
    def read_json_file(file_path):
        try:
            f=open(file_path, 'r')
            data = json.load(f)
        except OSError:
            print("Could not open/read file:", file_path)
        return data

    @staticmethod
    def delete_all_content_from_directory(directory_path):
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
