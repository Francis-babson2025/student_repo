import sys

sys.path.insert(0, './student_code')   # Preferred override
sys.path.insert(1, './default_code')   # Fallback default

from play_game import play_game

play_game()
