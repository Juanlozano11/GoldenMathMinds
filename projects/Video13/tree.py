## Path: cd Desktop/Math/GoldenMathMinds/projects/video13
## run: manim -pql tree.py NatureTree
from manim import *

class ViolentTransitionTree(Scene):
    def construct(self):
        # Create peaceful tree and environment
        trunk = self.create_trunk()
        leaves = self.create_leaves()
        tree = VGroup(trunk, leaves)
        grass = self.create_grass()
        sun = self.create_sun()
        cloud1 = self.create_cloud(UP * 2.5 + LEFT * 2, LEFT)
        cloud2 = self.create_cloud(UP * 2.3 + RIGHT * 2, RIGHT)
        peaceful_environment = VGroup(tree, grass, sun, cloud1, cloud2)

        # Animate peaceful environment
        self.animate_peaceful_scene(trunk, leaves, grass, sun, cloud1, cloud2)

        # Transition to violent environment
        self.transition_to_violence(tree, grass, sun, cloud1, cloud2)

        # Fade out the violent scene
        self.play(FadeOut(VGroup(tree, grass, sun, cloud1, cloud2)), run_time=2)

    def create_trunk(self):
        trunk = Rectangle(width=0.5, height=2, color=DARK_BROWN, fill_opacity=1)
        trunk.shift(DOWN * 2)
        return trunk

    def create_leaves(self):
        leaves = VGroup(
            Circle(radius=1.5, color=GREEN, fill_opacity=0.8).shift(+ LEFT * 1.5),
            Circle(radius=1.5, color=GREEN, fill_opacity=0.8).shift(+ RIGHT * 1.5),
            Circle(radius=2, color=GREEN, fill_opacity=0.9).shift(UP )
        )
        return leaves

    def create_grass(self):
        base_line = Line(LEFT * 7 + DOWN * 2.5, RIGHT * 7 + DOWN * 2.5, color=GREEN)
        blades = [
            Line(LEFT * 7 + DOWN * 2.5 + RIGHT * i, LEFT * 6.9 + DOWN * 2.4 + RIGHT * i, color=GREEN)
            for i in range(-7, 8)
        ]
        grass = VGroup(base_line, *blades)
        return grass

    def create_sun(self):
        sun = Circle(radius=0.8, color=YELLOW, fill_opacity=1)
        sun.shift(UP * 3 + RIGHT * 4)
        return sun

    def create_cloud(self, position, direction):
        cloud = VGroup(
            Circle(radius=0.4, color=WHITE, fill_opacity=1).shift(position + direction * 0.3),
            Circle(radius=0.5, color=WHITE, fill_opacity=1).shift(position + direction * 0.6 + UP * 0.2),
            Circle(radius=0.4, color=WHITE, fill_opacity=1).shift(position + direction * 0.9)
        )
        return cloud

    def animate_peaceful_scene(self, trunk, leaves, grass, sun, cloud1, cloud2):
        self.play(Create(trunk), run_time=2)
        self.play(Create(leaves), run_time=2)
        self.play(Create(grass), run_time=2)
        self.play(Create(sun), run_time=2)
        self.play(Create(cloud1), Create(cloud2), run_time=2)
        self.wait(2)  # Pause to show the peaceful scene

    def transition_to_violence(self, tree, grass, sun, cloud1, cloud2):
        # Transform the sun to dim and the tree to gray
        self.play(sun.animate.set_color(GRAY).set_fill(opacity=0.3), 
                  tree.animate.set_color(GRAY), 
                  run_time=1.5)

        # Replace clouds with dark clouds
        dark_cloud1 = self.create_cloud(UP * 2.5 + LEFT * 2, LEFT)
        dark_cloud2 = self.create_cloud(UP * 2.3 + RIGHT * 2, RIGHT)
        dark_cloud1.set_color(DARK_GRAY)
        dark_cloud2.set_color(DARK_GRAY)
        self.play(Transform(cloud1, dark_cloud1), Transform(cloud2, dark_cloud2), run_time=1.5)
        self.wait()
        text1 = Text("", font_size=36, color=BLUE)
        text = Text("La naturaleza es hermosa pero el contexto determinar su color", font_size=36, color=BLUE)
        self.play(Create(text1))
        self.play(Create(text))
        