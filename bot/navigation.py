import logging
import time
import random
import pyautogui

class NavigationModule:
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)
        self.waypoints = []

    def add_waypoint(self, coordinates):
        """Добавление точки маршрута"""
        self.waypoints.append(coordinates)
        self.logger.info(f"Added waypoint: {coordinates}")

    def navigate_to_next(self):
        """Навигация к следующей точке"""
        if not self.waypoints:
            self.logger.warning("No waypoints set!")
            return False

        target = self.waypoints.pop(0)
        self.logger.info(f"Navigating to: {target}")
        
        try:
            # Имитация навигации
            time.sleep(random.uniform(2.0, 3.0))
            return True
        except Exception as e:
            self.logger.error(f"Navigation error: {str(e)}")
            return False