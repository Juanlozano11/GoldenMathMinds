## path : cd Desktop/Math/GoldenMathMinds/projects/video04
## run :  manim -pql ParametricFunction.py AnimatedButterflyCurve


from manim import *
import numpy as np



class AnimatedButterflyCurve2(Scene):
    def construct(self):

            # Add a grid (NumberPlane) to the background
        #grid = NumberPlane()
        #self.play(Create(grid))  # Display the grid on the scene

        # Define the butterfly curve parametric function
        butterfly_curve = ParametricFunction(
            lambda t: np.array([
                np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5),
                np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5),
                0
            ]),
            t_range=[0, 12 * PI],  # Full range for the butterfly shape
            stroke_width=3  # Thickness of the curve
        )

        # Add a gradient title for "Butterfly Curve"
        title = Tex("Butterfly Curve").to_edge(UP)
        title.set_color_by_gradient(BLUE, PURPLE)

        # Display the equations at the bottom of the screen
        equations = MathTex(
            r"x = \sin(t) \left( e^{\cos(t)} - 2 \cos(4t) - \sin^5\left(\frac{t}{12}\right) \right)",
            r"y = \cos(t) \left( e^{\cos(t)} - 2 \cos(4t) - \sin^5\left(\frac{t}{12}\right) \right)"
        )
        equations.arrange(DOWN).scale(0.5).to_edge(DOWN)

        # Add the title and equations to the scene
        self.play(Write(title), Write(equations))

        # Animate the drawing of the butterfly curve with changing colors
        self.play(
            Create(
                butterfly_curve.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE),
            ),
            run_time=12
        )

       



        self.play(Uncreate(butterfly_curve), Uncreate(equations), Uncreate(title)) #Uncreate(grid))





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
