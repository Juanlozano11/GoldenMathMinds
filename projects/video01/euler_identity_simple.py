## Path: cd Desktop/Math/GoldenMathMinds/projects/video01
## run: manim -pql euler_identity_simple.py EulerIdentityExplanation

from manim import *
import numpy as np

class EulerIdentityWithClearFocus(Scene):
    def construct(self):
        # Step 1: Set up the complex plane
        plane = ComplexPlane().add_coordinates()
        self.play(Create(plane))
        
        # Step 2: Introduce Euler's Formula with introductory text
        intro_text = Text("Let's see how this equation looks on a graph!", font_size=36).to_edge(UP)
        self.play(Write(intro_text))
        
        euler_formula = MathTex("e^{ix} = \\cos(x) + i \\sin(x)", font_size=48)
        euler_formula.next_to(intro_text, DOWN)
        self.play(Write(euler_formula))
        
        # Step 3: Trace e^(ix) as x varies from 0 to 2π
        angle_tracker = ValueTracker(0)
        rotating_dot = Dot(color=YELLOW).move_to(plane.c2p(1, 0))  # Start at (1,0)
        trace_path = TracedPath(rotating_dot.get_center, stroke_color=BLUE, stroke_width=4)

        # Angle label
        angle_label = always_redraw(lambda: MathTex(
            f"e^{{i{np.round(angle_tracker.get_value(), 2)} }}",
            font_size=36,
            color=WHITE).next_to(rotating_dot, UP)
        )

        # Animate rotation and trace path
        self.add(trace_path, rotating_dot, angle_label)
        self.play(angle_tracker.animate.set_value(2 * np.pi), Rotate(rotating_dot, angle=2 * np.pi, about_point=plane.c2p(0, 0)), run_time=6)
        
        # Step 4: Replace x with π and show e^(iπ) = -1
        self.play(FadeOut(intro_text), FadeOut(trace_path), FadeOut(angle_label))
        pi_text = Text("Now, let's replace x with π.", font_size=36).to_edge(UP)
        self.play(Write(pi_text))
        
        self.play(angle_tracker.animate.set_value(np.pi), Rotate(rotating_dot, angle=np.pi, about_point=plane.c2p(0, 0)), run_time=3)
        
        # Show point at -1 and clear the screen for focus
        pi_point = Dot(plane.c2p(-1, 0), color=RED)
        self.play(FadeOut(euler_formula), FadeOut(plane), FadeIn(pi_point))
        
        # Step 5: Display e^(iπ) = -1
        final_step = MathTex("e^{i \\pi} = -1", font_size=72).to_edge(DOWN)
        self.play(Write(final_step))
        
        # Step 6: Add 1 to both sides
        add_one_text = Text("Adding 1 to both sides...", font_size=36).next_to(final_step, UP)
        self.play(Write(add_one_text))
        
        final_equation = MathTex("e^{i \\pi} + 1 = 0", font_size=72)
        self.play(Transform(final_step, final_equation), FadeOut(add_one_text))
        
        # Step 7: Explanation text of significance
        explanation = Text("This equation relates the 5 most important numbers in math", font_size=36, color=YELLOW).to_edge(UP)
        beauty_text = Text("It's a beautiful balance between different areas of math!", font_size=32).next_to(explanation, DOWN)
        
        self.play(Write(explanation))
        self.play(Write(beauty_text))
        
        # Step 8: Emphasize the final result
        box = SurroundingRectangle(final_equation, color=GOLD, buff=0.5)
        self.play(Create(box))
        self.wait(2)
        
        # Fade out to end
        self.play(FadeOut(VGroup(final_step, box, pi_point, explanation, beauty_text)))
