## Path: cd Desktop/Math/GoldenMathMinds/projects/video13
## run: manim -pql tree.py NatureTree

from manim import *

class NatureTree(Scene):
    def construct(self):
        # Create tree components
        trunk = self.create_trunk()
        leaves = self.create_leaves()
        tree = VGroup(trunk, leaves)

        # Create environment components
        grass = self.create_grass()
        sun = self.create_sun()
        cloud1 = self.create_cloud(UP * 2.5 + LEFT * 2, LEFT)
        cloud2 = self.create_cloud(UP * 2.3 + RIGHT * 2, RIGHT)
        environment = VGroup(tree, grass, sun, cloud1, cloud2)

        # Animate the scene
        self.animate_scene(trunk, leaves, grass, sun, cloud1, cloud2)

    def create_trunk(self):
        """Creates the tree trunk."""
        trunk = Rectangle(width=0.5, height=2, color=DARK_BROWN, fill_opacity=1)
        trunk.shift(DOWN * 2)
        return trunk

    def create_leaves(self):
        """Creates the leaves of the tree."""
        leaves = VGroup(
            Circle(radius=1.5, color=GREEN, fill_opacity=0.8).shift(UP * 0.5 + LEFT * 1.5),
            Circle(radius=1.5, color=GREEN, fill_opacity=0.8).shift(UP * 0.5 + RIGHT * 1.5),
            Circle(radius=2, color=GREEN, fill_opacity=0.9).shift(UP * 1.5)
        )
        return leaves

    def create_grass(self):
        """Creates the grass on the ground."""
        base_line = Line(LEFT * 7 + DOWN * 2.5, RIGHT * 7 + DOWN * 2.5, color=GREEN)
        blades = [
            Line(LEFT * 7 + DOWN * 2.5 + RIGHT * i, LEFT * 6.9 + DOWN * 2.4 + RIGHT * i, color=GREEN)
            for i in range(-7, 8)
        ]
        grass = VGroup(base_line, *blades)
        return grass

    def create_sun(self):
        """Creates the sun in the sky."""
        sun = Circle(radius=0.8, color=YELLOW, fill_opacity=1)
        sun.shift(UP * 3 + RIGHT * 4)
        return sun

    def create_cloud(self, position, direction):
        """Creates a cloud at a given position and direction."""
        cloud = VGroup(
            Circle(radius=0.4, color=WHITE, fill_opacity=1).shift(position + direction * 0.3),
            Circle(radius=0.5, color=WHITE, fill_opacity=1).shift(position + direction * 0.6 + UP * 0.2),
            Circle(radius=0.4, color=WHITE, fill_opacity=1).shift(position + direction * 0.9)
        )
        return cloud

    def animate_scene(self, trunk, leaves, grass, sun, cloud1, cloud2):
        """Handles the animation for all elements with smoother transitions."""
        self.play(Create(trunk), run_time=2)  # Slower creation of the trunk
        self.wait(0.5)  # Small pause after creating the trunk
        self.play(Create(leaves), run_time=2)  # Slower creation of the leaves
        self.wait(0.5)  # Small pause after creating the leaves
        self.play(Create(grass), run_time=2)  # Slower creation of the grass
        self.wait(0.5)  # Small pause after creating the grass
        self.play(Create(sun), run_time=2)  # Slower creation of the sun
        self.wait(0.5)  # Small pause after creating the sun
        self.play(Create(cloud1), run_time=2)  # Slower creation of the first cloud
        self.wait(0.5)  # Small pause after creating the first cloud
        self.play(Create(cloud2), run_time=2)  # Slower creation of the second cloud
        self.wait()  # Wait for a moment to let the full scene settle
