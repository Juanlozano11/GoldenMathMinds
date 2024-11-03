
## Path: cd Desktop/Math/GoldenMathMinds/projects/profilepicture
## run in terminal manim -pql euler_identity.py EulerIdentity

from manim import *

class EulerIdentitySimple(Scene):
    def construct(self):
        # Display Euler's identity with nice colors
        euler_identity = MathTex(r"e^{i \pi} + 1 = 0")
        
        # Style adjustments
        euler_identity.set_color_by_gradient(BLUE, PURPLE, ORANGE)  # Gradient color
        euler_identity.scale(2)  # Make it larger
        euler_identity.move_to(ORIGIN)  # Center it on the screen

        # Add the equation to the scene
        self.add(euler_identity)
