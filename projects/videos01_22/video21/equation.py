## path : cd Desktop/Math/GoldenMathMinds/projects/video21
## run :  manim -pql equation.py ParametricCurveScene

from manim import *

class FancyParametricCurve(Scene):
    def construct(self):
        # Define the fancy parametric curve
        curve = ParametricFunction(
            lambda t: np.array([
                -35 * np.cos(t) + 65 * np.cos(-0.35 * t),  # x(t)
                -35 * np.sin(t) - 65 * np.sin(-0.35 * t),  # y(t)
                0
            ]),
            t_range=[0, 40 * PI], 
            stroke_width=2
        ).scale(0.02)  # Because 35 and 65 are big

        # Center the curve
        curve.move_to(ORIGIN)

        # Title at the top
        title = Tex("Parametric Curves").scale(1.4)
        title.set_color_by_gradient(BLUE, PURPLE, PINK)
        title.to_edge(UP)

        # Equations below the curve
        equations = VGroup(
            MathTex(r"x(t) = -35\cos(t) + 65\cos(-0.35t)"),
            MathTex(r"y(t) = -35\sin(t) - 65\sin(-0.35t)")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        equations.next_to(curve, DOWN, buff=0.8)


        # Animations
        self.play(Write(title))
        self.play(Write(equations))
        self.play(Create(curve.set_color_by_gradient(RED, ORANGE, PINK)), run_time=10) 
        self.wait(1)
        self.play(FadeOut(curve), FadeOut(title), FadeOut(equations))


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
