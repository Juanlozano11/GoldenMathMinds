## path : cd Desktop/Math/GoldenMathMinds/projects/video19
## run :  manim -pql equation.py parametric

from manim import *
import numpy as np

class parametric(Scene):
    def construct(self):

        # Define the parametric curve function (hypotrochoid style)
        curve = ParametricFunction(
            lambda t: np.array([
                11 * np.cos(t) - 6 * np.cos((11 / 6) * t),
                11 * np.sin(t) - 6 * np.sin((11 / 6) * t),
                0
            ]),
            t_range=[0, 12 * PI],
            stroke_width=3
        ).scale(0.1).move_to(ORIGIN)  # scale and center

        # Title on top
        title = Tex("Parametric Curves").scale(1.2).to_edge(UP)
        title.set_color_by_gradient(BLUE, PURPLE)

        # Equations directly under the curve
        equations = MathTex(
            r"x(t) = 11 \cos(t) - 6 \cos\left(\frac{11}{6}t\right)",
            r"y(t) = 11 \sin(t) - 6 \sin\left(\frac{11}{6}t\right)"
        ).arrange(DOWN).scale(0.55)
        equations.next_to(curve, DOWN, buff=0.5)

        # Animations
        self.play(Write(title), Write(equations))
        self.play(Create(curve.set_color_by_gradient(RED, ORANGE, YELLOW, PINK)), run_time=12)
        self.wait(1.2)
        self.play(Uncreate(curve), Uncreate(equations), Uncreate(title))


## Golden math minds outro 


        spiral = ParametricFunction(
            lambda t: np.array([np.cos(t) * (1.618 ** (t / (2 * np.pi))),
                                np.sin(t) * (1.618 ** (t / (2 * np.pi))),
                                0]),
            t_range=[0, 2 * PI],
            color=TEAL_A
        ).scale(0.5).shift(LEFT)
        
        # Dot tracing part of the spiral, stopping midway
        trace_dot = Dot(color=MAROON_A).move_to(spiral.get_start())
        halfway_point = spiral.point_from_proportion(0.5)
        
        # Euler's Identity with elegant text
        euler_identity = MathTex("e^{i\\pi} + 1 = 0", color=WHITE).scale(1.3).next_to(trace_dot, 3 * DOWN, buff=0.3)

        # "Golden Math Minds" with gradient effect
        logo_text = Text("Golden Math Minds", font_size=44, gradient=(YELLOW, ORANGE, GOLD))
        logo_text.next_to(euler_identity, 2.5 * DOWN, buff=0.3)

        # Animations
        self.play(Create(spiral), MoveAlongPath(trace_dot, spiral, rate_func=linear), run_time=2.5)
        self.play(trace_dot.animate.move_to(halfway_point), run_time=1)
        self.play(Write(euler_identity), run_time=1.2)
        self.wait(0.5)
        self.play(Write(logo_text))
        self.wait(1.5)

        # Final cool ending animation
        self.play(
            FadeOut(logo_text),
            FadeOut(euler_identity),
            spiral.animate.scale(0.1).move_to(ORIGIN),
            trace_dot.animate.scale(0.1).move_to(ORIGIN),
            run_time=2
        )

        # Hold briefly
        self.wait(0.8)