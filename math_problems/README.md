# Math Problems
These math problems are random applications written based on weird questions or ideas with a mathematical basis. I'll try to keep this readme updated with each one that I write and its "why"

# Problems:
## The Hydra Game
see: https://www.youtube.com/watch?v=prURA1i8Qj4

An attempt to solve the Hydra Game for Y=5 as described in the video.

**Problem:** The description of the Hydra Game that I'm working on solving is described as the Rapid Growth Example at time index 16:26. However they never describe how to properly detect the right-most-leaf. 

My code assumes that the right-most-leaf is any leaf on the node with the most leaves. However, this interpretation is wrong because the expected answer for Y=4 is 983,038 and my code with the above interpretation results in 327,677. The vague definition still blows up for Y=5, 

I've optimized both the CPP and the Java versions. The CPP will overflow after mere seconds, whereas the Java version (implemented with BigInteger) will loop until the universe has passed away multiple times. The number is so ridiculously large that the bird sharpening his beak on the mountain of Svithjod will have destroyed the mountain countless times before this answer is solved by all the computers on all the planets in all the universes that exist. For reference, here's the quote by Hendrik Willem van Loon: 

>“High in the North in a land called Svithjod there is a mountain. It is a hundred miles long and a hundred miles high and once every thousand years a little bird comes to this mountain to sharpen its beak. When the mountain has thus been worn away a single day of eternity will have passed.”



## MPMP: The 1 Million Bank Balance Puzzle
see: https://www.youtube.com/watch?v=ILrqPpLpwpE

## Witness Numbers:
see: https://www.youtube.com/watch?v=_MscGSN5J6o
