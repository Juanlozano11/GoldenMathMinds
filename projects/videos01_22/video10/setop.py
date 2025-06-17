## path : cd Desktop/Math/GoldenMathMinds/projects/video10
## run :  manim -pql setop.py UnionSetOperation


from manim import *

class UnionSetOperation(Scene):
    def construct(self):
        # Title
        title = Text("Set Operation: Union", font_size=48, color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Circles representing sets
        circle_A = Circle(radius=2, color=RED).shift(LEFT * 1)
        label_A = Text("A", color=RED).next_to(circle_A, UP)
        circle_B = Circle(radius=2, color=GREEN).shift(RIGHT * 1)
        label_B = Text("B", color=GREEN).next_to(circle_B, UP)

        # Display circles
        self.play(Create(circle_A), Create(circle_B))
        self.play(Write(label_A), Write(label_B))
        self.wait(1)

        # Highlight set A
        set_A = circle_A.copy().set_fill(RED, opacity=0.5)
        label_set_A = Text("A", font_size=36, color=RED).shift(DOWN * 3)
        self.play(FadeIn(set_A))
        self.play(Write(label_set_A))
        self.wait(1)
        self.play(FadeOut(set_A), FadeOut(label_set_A))

        # Highlight set B
        set_B = circle_B.copy().set_fill(GREEN, opacity=0.5)
        label_set_B = Text("B", font_size=36, color=GREEN).shift(DOWN * 3)
        self.play(FadeIn(set_B))
        self.play(Write(label_set_B))
        self.wait(1)
        self.play(FadeOut(set_B), FadeOut(label_set_B))

        # Highlight union of A and B
        union_A_B = VGroup(
            circle_A.copy().set_fill(RED, opacity=0.3),
            circle_B.copy().set_fill(GREEN, opacity=0.3),
        )
        union_label = Text("A ∪ B", font_size=36, color=YELLOW).shift(DOWN * 3)

        self.play(FadeIn(union_A_B))
        self.play(Write(union_label))
        self.wait(2)

        # Explaining union
        explanation = Text(
            "",
            font_size=24
        ).next_to(union_label, DOWN)

        self.play(Write(explanation))
        self.wait(3)

        # Closing animation
        self.play(FadeOut(union_A_B), FadeOut(union_label), FadeOut(explanation))
        self.play(FadeOut(circle_A), FadeOut(circle_B), FadeOut(label_A), FadeOut(label_B), FadeOut(title))
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

