import Sapienza.masonry_panels as mp


# Specify the geometry of the problem
brick_length = 60.0
brick_height = 60.0
hor_bricks = 32
ver_bricks = 48

# Creation of stack bond masonry panel
# mp.stack(brick_length, brick_height, hor_bricks, ver_bricks)

# Creation of running bond masonry panel
# mp.running(brick_length, brick_height, hor_bricks, ver_bricks)

# Creation of english bond masonry panel
# mp.english(brick_length, brick_height, hor_bricks, ver_bricks)

# Creation of flemish bond masonry panel
mp.flemish(brick_length, brick_height, hor_bricks, ver_bricks)