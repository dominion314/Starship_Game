from pygame.image import load

def load_sprite(name, with_alpha=True): #This loads the images in the following directory as the background.
    path = f"assets/sprites/space.png"
    loaded_sprite = load(path)

    if with_alpha: #Loads the format to fit screen via convert alpha
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()
    
