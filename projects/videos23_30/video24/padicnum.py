## path : cd Desktop/Math/GoldenMathMinds/projects/videos23_30/video23/
## run :  manim -pql padicnum.py PadicNumberDefinition


from manim import *

class PadicNumberDefinition(Scene):
    def construct(self):
        # Title
        title = Tex("Understanding $p$-adic Numbers").scale(1.3).set_color_by_gradient(BLUE, TEAL)
        title.move_to(UP * 2)
        self.play(GrowFromCenter(title), run_time=2)
        self.wait(0.5)

        # Definition text
        definition_text = VGroup(
            Tex(r"Given a prime $p$, a \textbf{$p$-adic number} is an infinite series of the form:").set_color(BLUE),
            MathTex(r"s = \sum_{i=k}^{\infty} a_i p^i = a_k p^k + a_{k+1} p^{k+1} + a_{k+2} p^{k+2} + \cdots").set_color(GREEN),
            Tex(r"where $k \in \mathbb{Z}$ and $0 \leq a_i < p$ for all $i$.").set_color(RED),
        ).arrange(DOWN, center=True).scale(0.85)
        definition_text.next_to(title, DOWN, buff=0.8)

        self.play(LaggedStartMap(FadeIn, definition_text, lag_ratio=0.7, run_time=8))
        self.wait(1.5)

        # Fade out all previous elements
        self.play(FadeOut(VGroup(title, definition_text)))
        self.wait(0.5)

        # Example of a p-adic number
        example_title = Tex(r"Example: $5$-adic Number").scale(1.0).to_edge(UP).set_color(TEAL)
        self.play(Write(example_title), run_time=2)

        # Visual representation
        example_series = MathTex(
            r"3 + 4\cdot 5 + 2\cdot 5^2 + 1\cdot 5^3 + \cdots"
        ).scale(1.2).next_to(example_title, DOWN, buff=0.8).set_color(PURPLE)

        self.play(Write(example_series), run_time=3)
        self.play(example_series.animate.shift(UP * 0.1).shift(DOWN * 0.1), run_time=0.5)
        self.wait(1.5)

        # Enhanced explanation with visuals and colors
        zoom_idea = VGroup(
            Tex("Think of it like a microscope for numbers!").scale(0.9).set_color(YELLOW),
            Tex(r"Each term adds a new 'digit' in base-$5$ from right to left.")
                .scale(0.85).set_color(BLUE),
            Tex(r"The further you go, the \textit{more precise} the number becomes.")
                .scale(0.85).set_color(GREEN)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).next_to(example_series, DOWN, buff=0.8)

        for i, item in enumerate(zoom_idea):
            self.play(FadeIn(item, shift=UP), run_time=1.5)
        self.wait(5)

        # Final summary with a fade out
        closing_text = Tex("This is the magic of $p$-adic numbers!").scale(1.1).set_color_by_gradient(ORANGE, YELLOW)
        closing_text.move_to(ORIGIN)

        self.play(FadeOut(VGroup(example_title, example_series, zoom_idea)))
        self.play(FadeIn(closing_text))
        self.wait(4)
        self.play(FadeOut(closing_text))
        self.wait(0.5)


## Golden Math Minds Outro (keep it same)

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
