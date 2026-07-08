"""
Entrypoint. Run with: python main.py
"""
import logging

from ui.app import launch

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

if __name__ == "__main__":
    launch()
