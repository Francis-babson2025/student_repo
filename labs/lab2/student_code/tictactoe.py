import sys
from pathlib import Path

# Resolve absolute paths
base_dir = Path(__file__).parent.resolve()
student_code = base_dir
default_code = base_dir.parent / 'default_code'

# Add both to sys.path (student_code first)
sys.path.insert(0, str(student_code))
sys.path.insert(1, str(default_code))

# Import and run


from play_game import play_game
play_game()

