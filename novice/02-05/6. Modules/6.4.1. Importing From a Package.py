# dibawah ini merupakan contoh import file double yang tergabung dengan file 6.4. package
# 6.4.1 Importing * from a packagae

__all__ = ["echo", "surround", "reverse"]

import sound.effects.echo
import sound.effects.surround
from sound.effects import *
