## path : cd Desktop/Math/GoldenMathMinds/projects/video20
## run :  manim -pql equation.py parametric

from manim import *

class ParametricCurveScene(Scene):
    def construct(self):
        # Define the parametric curve (flower shape)
        curve = ParametricFunction(
            lambda t: np.array([
                np.sin(6 * t) * np.cos(t),  # x
                np.sin(6 * t) * np.sin(t),  # y
                0
            ]),
            t_range=[0, TAU],
            stroke_width=3
        ).scale(3)

        # Center the curve
        curve.move_to(ORIGIN)

        # Define the title
        title = Tex("Parametric Equation").scale(1.2)
        title.set_color_by_gradient(BLUE, PURPLE)
        title.to_edge(UP)  # Move to top edge

        # Play animations
        self.play(Write(title))
        self.play(Create(curve.set_color_by_gradient(RED, ORANGE, PINK)), run_time=6)
        self.wait(2)
        self.play(Uncreate(curve), Uncreate(title))
        self.wait(0.2)


        ## Golden Math Minds Outro (No need to change)

        spiral = ParametricFunction(
            lambda t: np.array([
                np.cos(t) * (1.618 ** (t / (2 * np.pi))),
                np.sin(t) * (1.618 ** (t / (2 * np.pi))),
                0]),
            t_range=[0, 2 * PI],
            color=TEAL_A
        ).scale(0.5).shift(LEFT)
        
        trace_dot = Dot(color=MAROON_A).move_to(spiral.get_start())
        halfway_point = spiral.point_from_proportion(0.5)

        euler_identity = MathTex("e^{i\\pi} + 1 = 0", color=WHITE).scale(1.3).next_to(trace_dot, 3 * DOWN, buff=0.3)

        logo_text = Text("Golden Math Minds", font_size=44, gradient=(YELLOW, ORANGE, GOLD))
        logo_text.next_to(euler_identity, 2.5 * DOWN, buff=0.3)




        # Outro Animations
        self.play(Create(spiral), MoveAlongPath(trace_dot, spiral, rate_func=linear), run_time=2.5)
        self.play(trace_dot.animate.move_to(halfway_point), run_time=1)
        self.play(Write(euler_identity), run_time=1.2)
        self.wait(0.5)
        self.play(Write(logo_text))
        self.wait(1.5)

        # Final ending animation
        self.play(
            FadeOut(logo_text),
            FadeOut(euler_identity),
            spiral.animate.scale(0.1).move_to(ORIGIN),
            trace_dot.animate.scale(0.1).move_to(ORIGIN),
            run_time=2
        )
        self.wait(0.8)
