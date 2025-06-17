## path : cd Desktop/Math/GoldenMathMinds/projects/video12
## run :  manim -pql function.py ImplicitFunction

from manim import *
import numpy as np

class ImplicitFunctionWithAnimation(Scene):
    def construct(self):
        # Animated function writing
        equation = MathTex(r"y^2 = x^2 \sin(x^2 + y^2)").set_color_by_gradient(BLUE, PURPLE)
        #equation.to_edge(UP).shift(LEFT * 1)  # Adjust to the left to avoid overlapping with the y-axis
        #self.play(Write(equation), run_time=2)

        # Create axes
        axes = Axes(
            x_range=[-2, 2, 0.5],
            y_range=[-2, 2, 0.5],
            axis_config={"color": WHITE},
        ).add_coordinates()

        # Label the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        self.play(Write(axes), Write(x_label), Write(y_label))

        # Numerical approximation for the implicit function
        resolution = 200  # Higher resolution for smoother curves
        points = []

        for x in np.linspace(-2, 2, resolution):
            for y in np.linspace(-2, 2, resolution):
                if np.abs(y**2 - x**2 * np.sin(x**2 + y**2)) < 0.05:  # Threshold for approximation
                    points.append(axes.coords_to_point(x, y))

        # Create the dots representing the curve
        implicit_curve = VGroup(*[Dot(point, radius=0.02, color=TEAL) for point in points])

        # Animate the curve
        self.play(Write(implicit_curve, scale=0.5), run_time=4)
        self.wait(1)

        # Add some text to indicate the function is implicit
        implicit_text = Text("Implicit Function", font_size=36, color=YELLOW).to_edge(DOWN)
        self.play(Write(implicit_text))
        self.wait(2)

        # Cleanup
        self.play(
            #FadeOut(equation),
            FadeOut(axes),
            FadeOut(implicit_curve),
            FadeOut(implicit_text),
            FadeOut(x_label),
            FadeOut(y_label),
            run_time=2
        )
        self.wait()







         # Golden Ratio Spiral (one smooth rotation)
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
