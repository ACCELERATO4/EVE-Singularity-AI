import signal
import pickle
import time
import logging
from dotenv import load_dotenv
from bot.mining import MiningModule
from bot.navigation import NavigationModule
from bot.security import SecuritySystem
from bot.anti_detect import AntiDetectionSystem

load_dotenv()

class EVEBot:
    def __init__(self):
        self._setup_logging()
        self._load_state()
        self.mining = MiningModule(self)
        self.navigation = NavigationModule(self)
        self.security = SecuritySystem(self)
        self.anti_detect = AntiDetectionSystem(self)
        self.running = False
        signal.signal(signal.SIGINT, self._handle_signal)

    def _setup_logging(self):
        self.logger = logging.getLogger('EVEBot')
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler('bot.log')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def _handle_signal(self, signum, frame):
        self.logger.info("Received shutdown signal")
        self.stop()

    def start(self):
        self.running = True
        self.logger.info("Starting EVE Singularity AI")
        try:
            while self.running:
                self._main_loop()
        except Exception as e:
            self.logger.error(f"Critical error: {str(e)}")
            self._save_state()
            self._emergency_shutdown()

    def _main_loop(self):
        self.anti_detect.randomize_behavior()
        self.security.check_dangers()
        
        if self.mining.should_mine():
            self.mining.execute()
        
        self.navigation.update()
        time.sleep(1)

    def stop(self):
        self.running = False
        self._save_state()
        self.logger.info("Shutting down gracefully")
        self.anti_detect.cleanup()

    def _save_state(self):
        state = {
            'mining': self.mining.get_state(),
            'navigation': self.navigation.waypoints
        }
        with open('state/last_state.dat', 'wb') as f:
            pickle.dump(state, f)

    def _load_state(self):
        try:
            with open('state/last_state.dat', 'rb') as f:
                state = pickle.load(f)
                self.mining_state = state.get('mining', {})
                self.waypoints = state.get('navigation', [])
        except FileNotFoundError:
            self.logger.info("No previous state found")

    def _emergency_shutdown(self):
        self.logger.warning("Performing emergency shutdown")
        pyautogui.moveTo(100, 100)
        self.stop()
        sys.exit(1)