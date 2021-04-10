from pygame.math import Vector2 #imports vector class

class GameObject: #represents all the game objects
    def __init__(self, position, sprite, velocity): #Constructor of those objects based on position, sprite, and velocity.
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2 #radius needs to be half the sprite image
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self):
        self.position = self.position + self.velocity

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius
    