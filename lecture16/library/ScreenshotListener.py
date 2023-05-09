import os

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


class ScreenshotListener:
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self._screenshot_counter = 1
        self._screenshot_directory = "C:\\Projects\\PythonLearning\\lecture16\\results"

    def _take_screenshot(self):
        my_library = BuiltIn().get_library_instance('MyLibrary')
        path = os.path.join(self._screenshot_directory, f'screenshot{self._screenshot_counter}.png')
        is_screenshot_created = my_library.driver.save_screenshot(path)
        logger.info(f'Screenshot saved to {path}. Result {is_screenshot_created}')
        self._screenshot_counter += 1

    def end_keyword(self, name, attrs):
        if 'screenshot' in attrs['tags']:
            self._take_screenshot()
