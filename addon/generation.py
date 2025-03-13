import bpy
import random
from mathutils import Vector

# Constantes
MIN_DISTANCE = 1.0  # Distance minimale entre les diamants
MAX_ATTEMPTS = 100  # Nombre maximal de tentatives pour placer un diamant

def generate_diamonds_on_surface(surface_obj, diamond_sizes, density=0.5):
    """
    Génère des diamants sur une surface donnée.

    :param surface_obj: Objet Blender représentant la surface.
    :param diamond_sizes: Liste des tailles des diamants (rayons).
    :param density: Densité de distribution (0.0 à 1.0).
    """
    # Récupérer les vertices de la surface
    vertices = [v.co for v in surface_obj.data.vertices]
    
    # Liste pour stocker les positions des diamants
    diamond_positions = []
    
    # Nombre de diamants à placer
    num_diamonds = int(len(vertices) * density)
    
    # Placer les diamants
    for _ in range(num_diamonds):
        size = random.choice(diamond_sizes)  # Choisir une taille aléatoire
        position = find_valid_position(vertices, diamond_positions, size)
        
        if position:
            diamond_positions.append((position, size))
            create_diamond_at_position(position, size)

def find_valid_position(vertices, diamond_positions, size):
    """
    Trouve une position valide pour un diamant.

    :param vertices: Liste des vertices de la surface.
    :param diamond_positions: Liste des positions des diamants déjà placés.
    :param size: Taille du diamant à placer.
    :return: Position valide (Vector) ou None si aucune position n'est trouvée.
    """
    for _ in range(MAX_ATTEMPTS):
        # Choisir un vertex aléatoire
        position = random.choice(vertices)
        
        # Vérifier la distance avec les autres diamants
        if is_position_valid(position, diamond_positions, size):
            return position
    
    return None

def is_position_valid(position, diamond_positions, size):
    """
    Vérifie si une position est valide pour un diamant.

    :param position: Position à vérifier (Vector).
    :param diamond_positions: Liste des positions des diamants déjà placés.
    :param size: Taille du diamant à placer.
    :return: True si la position est valide, False sinon.
    """
    for existing_position, existing_size in diamond_positions:
        distance = (position - existing_position).length
        if distance < (size + existing_size + MIN_DISTANCE):
            return False
    return True

def create_diamond_at_position(position, size):
    """
    Crée un diamant à une position donnée.

    :param position: Position du diamant (Vector).
    :param size: Taille du diamant.
    """
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3, radius=size, location=position)
    diamond = bpy.context.object
    diamond.name = "Diamond"
    diamond.data.name = "DiamondMesh"