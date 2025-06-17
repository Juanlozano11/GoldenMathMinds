## Path: cd Desktop/Math/GoldenMathMinds/projects/video18
## run: manim -pql harmonic.py FermatLittleTheorem

from manim import *

class FermatLittleTheorem(Scene):
    def construct(self):
        # Intro message (animated pop-in)
        intro = Text("Fermat's Little Theorem", font_size=52).set_color_by_gradient(ORANGE, RED)
        intro.scale(0.7)
        self.play(GrowFromCenter(intro), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(intro, shift=UP), run_time=1.2)

        # Theorem presentation
        theorem_text = MathTex(r"a^{p-1} \equiv 1 \ (\mathrm{mod}\ p)", font_size=62)
        theorem_text.set_color_by_gradient(GREEN, BLUE)
        self.play(Write(theorem_text), run_time=2)
        self.wait(1)
        self.play(theorem_text.animate.shift(UP * 2), run_time=1)

        # Explanation appears below
        explanation = Text("For p prime and gcd(a, p) = 1", font_size=32)
        explanation.next_to(theorem_text, DOWN, buff=0.6)
        self.play(FadeIn(explanation, shift=UP), run_time=1.5)
        self.wait(2)

        # Golden Ratio Spiral
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

        # Euler's Identity
        euler_identity = MathTex("e^{i\\pi} + 1 = 0", color=WHITE).scale(1.3).next_to(trace_dot, 3 * DOWN, buff=0.3)

        # Logo text
        logo_text = Text("Golden Math Minds", font_size=44)
        logo_text.set_color_by_gradient(PINK, PURE_BLUE, BLUE_D)
        logo_text.next_to(euler_identity, 2.5 * DOWN, buff=0.3)

        self.play(FadeOut(theorem_text),
            FadeOut(explanation),)
        # Spiral and dot animation
        self.play(Create(spiral), run_time=2)
        self.add(trace_dot)
        self.play(MoveAlongPath(trace_dot, spiral, rate_func=smooth), run_time=2.5)
        self.play(trace_dot.animate.move_to(halfway_point), run_time=1)

        # Display Euler's Identity and logo
        self.play(Write(euler_identity), run_time=1.2)
        self.wait(0.5)
        self.play(FadeIn(logo_text, scale=0.8), run_time=1.3)
        self.wait(1.5)

        # Clean exit
        self.play(
            
            FadeOut(logo_text),
            FadeOut(euler_identity),
            spiral.animate.scale(0.1).move_to(ORIGIN),
            trace_dot.animate.scale(0.1).move_to(ORIGIN),
            run_time=2
        )
        self.wait(0.8)
