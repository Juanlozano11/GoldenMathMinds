## Path: cd Desktop/Math/GoldenMathMinds/projects/video16
## run: manim -pql solution.py AnotherMathVisualization

from manim import *

class AnotherMathVisualization(Scene):
    def construct(self):
        # Title text: "Ready for a challenge?" with gradient color
        title = Text("Solution!!", font_size=48).set_color_by_gradient(PINK, PURE_BLUE, BLUE_D)
        self.play(Write(title))
        
        # Move title up and enlarge it slightly
        self.play(title.animate.shift(UP * 2).scale(1.3))

       # Display a new math equation with gradient color
        problem = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=48).set_color_by_gradient(BLUE, PURPLE, PINK)
        self.play(FadeIn(problem, shift=DOWN))
        self.play(problem.animate.scale(1.3))
        self.wait(3)


        # Remove title and problem with a fading effect
        self.play(FadeOut(title), FadeOut(problem))

    




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
        logo_text = Text("Golden Math Minds", font_size=44, gradient=(PINK, PURE_BLUE, BLUE_D))
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

