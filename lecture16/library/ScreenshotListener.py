import os
import time

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


class ScreenshotListener:
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, path_to_screenshots):
        self.path_to_screenshots = path_to_screenshots

    def _take_screenshot(self, name):
        my_library = BuiltIn().get_library_instance('MyLibrary')
        file_name = f'screenshot_{name.replace(" ", "_").replace(".", "_")}_{int(time.time())}.png'
        path = os.path.join(self.path_to_screenshots, file_name)
        is_screenshot_created = my_library.driver.save_screenshot(path)
        logger.info(f'Screenshot saved to {path}. Result {is_screenshot_created}')

    def end_keyword(self, name, attrs):
        if 'screenshot' in attrs['tags']:
            self._take_screenshot(name)
