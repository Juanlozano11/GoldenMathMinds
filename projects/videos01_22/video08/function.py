## path : cd Desktop/Math/GoldenMathMinds/projects/video08
## run :  manim -pql function.py AnimatedLissajousCurve


from manim import *
import numpy as np

class AnimatedHeartCurve(Scene):
    def construct(self):
        # Define the heart curve parametric function
        heart_curve = ParametricFunction(
            lambda t: np.array([
                16 * np.sin(t)**3,  # x-coordinate
                13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t),  # y-coordinate
                0  # z-coordinate
            ]),
            t_range=[0, 2 * PI],  # Full range for the heart shape
            stroke_width=5,  # Thickness of the curve
            color=RED  # Heart color
        ).scale(0.15).shift(UP * 2)  # Reduced size and shifted slightly up

        # Add a title at the top
        title = Tex("Heart Curve").to_edge(UP)
        title.set_color_by_gradient(RED, PINK)

        # Display the equations at the bottom of the screen
        equations = MathTex(
            r"x = 16\sin^3(t)",
            r"y = 13\cos(t) - 5\cos(2t) - 2\cos(3t) - \cos(4t)"
        )
        equations.arrange(DOWN).scale(0.5).to_edge(DOWN)

        # Add the title and equations to the scene
        self.play(Write(title), Write(equations))

        # Animate the drawing of the heart curve
        self.play(Create(heart_curve), run_time=8)

        # Add dots to emphasize the top and bottom points of the heart
        top_dot = Dot(color=YELLOW).move_to(heart_curve.get_start())
        bottom_dot = Dot(color=ORANGE).move_to(heart_curve.point_from_proportion(0.5))

        self.play(FadeIn(top_dot), FadeIn(bottom_dot))

        # Add some playful text inside the heart
        love_text = Text("Made with Love", font_size=36, color=WHITE).move_to(ORIGIN + UP * 2)
        self.play(Write(love_text))
        self.wait(2)

        # Add some sparkle animation around the heart
        sparkles = VGroup(
            *[Dot(color=YELLOW).scale(0.3).move_to(
                heart_curve.point_from_proportion(i / 20)
            ) for i in range(20)]
        )
        self.play(FadeIn(sparkles, scale=2), run_time=2)
        self.play(FadeOut(sparkles, scale=0.5))

        # Cleanup animations
        self.play(
            FadeOut(title),
            FadeOut(equations),
            FadeOut(love_text),
            Uncreate(heart_curve),
            FadeOut(top_dot),
            FadeOut(bottom_dot),
            run_time=2
        )

        self.wait(1)


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
