import random
import time
import psutil
import platform
import hashlib
from pynput import mouse, keyboard

class AntiDetectionSystem:
    def __init__(self, bot):
        self.bot = bot
        self.mouse_listener = mouse.Listener(on_move=self._record_mouse)
        self.keyboard_listener = keyboard.Listener(on_press=self._record_key)
        self.activity_log = []
        self.start_time = time.time()

    def randomize_behavior(self):
        actions = [
            self._random_delay,
            self._random_mouse_move,
            self._fake_input
        ]
        random.choice(actions)()

    def _random_delay(self):
        delay = random.uniform(0.2, 1.5)
        time.sleep(delay)

    def _random_mouse_move(self):
        x, y = pyautogui.position()
        pyautogui.moveTo(
            x + random.randint(-20, 20),
            y + random.randint(-20, 20),
            duration=random.uniform(0.1, 0.3)
        )

    def _fake_input(self):
        if random.random() < 0.1:
            pyautogui.press(random.choice(['shift', 'ctrl', 'alt']))

    def _record_mouse(self, x, y):
        self.activity_log.append(f'mouse:{x}:{y}:{time.time()}')

    def _record_key(self, key):
        self.activity_log.append(f'key:{key}:{time.time()}')

    def cleanup(self):
        self.mouse_listener.stop()
        self.keyboard_listener.stop()

    def detect_monitoring(self):
        for proc in psutil.process_iter(['name']):
            if any(s in proc.info['name'].lower() for s in ['wireshark', 'cheatengine', 'processhacker']):
                return True
        return False