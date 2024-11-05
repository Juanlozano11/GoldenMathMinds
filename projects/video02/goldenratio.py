## Path: cd Desktop/Math/GoldenMathMinds/projects/video02
## run: manim -pql goldenratio.py GoldenRatio
## Use code form https://gitlab.com/cw-manim/fibonacci-sequence

from manim import *

class GoldenRatioFibonacciSpiral(Scene):
    def construct(self):
        # Step 1: Title Introduction
        title = Text("The Golden Ratio", font_size=44, gradient=(YELLOW, ORANGE, GOLD))
        self.play(Write(title))
        self.wait(1)

        # Step 2: Show the Golden Ratio Identity
        identity = MathTex(r"\frac{a+b}{a} = \frac{a}{b} = \varphi \approx 1.618", font_size=48)
        identity.next_to(title, DOWN)
        explanation = Text("This number is the only one that makes this ratio true", font_size=24)
        explanation.next_to(identity, DOWN)
        
        # Display the Golden Ratio identity and explanation
        self.play(Write(identity))
        self.wait(1)
        self.play(Write(explanation))
        self.wait(1)
        
        # Step 3: Transition to Fibonacci Sequence
        fib_title = Text("This number appears in the Fibonacci Sprial", font_size=36).to_edge(UP)
        self.play(ReplacementTransform(title, fib_title), FadeOut(identity), FadeOut(explanation))
        self.wait(2)
        self.play(FadeOut(fib_title))

        

        squares = VGroup(Square(1 * 0.3))
        next_dir = [RIGHT, UP, LEFT, DOWN]
        FSeq = [1, 2, 3, 5, 8, 13, 21]

        for j, i in enumerate(FSeq):
            d = next_dir[j % 4]
            squares.add(Square(i * 0.3).next_to(squares, d, buff=0))

        squares.center()

        direction = [1, -1, -1, 1]
        corner = [[UL, -UL], [UR, -UR]]
        spiral = VGroup()

        for j, i in enumerate(squares):
            c = corner[j % 2]
            d = direction[j % 4]
            arc = ArcBetweenPoints(
                i.get_corner(c[0]),
                i.get_corner(c[1]),
                angle=PI / 2 * d,
                color="#04d9ff",
                stroke_width=6,
            )
            if direction[j % 4] != 1:
                arc = arc.reverse_direction()
            spiral.add(arc)

        self.play(
            LaggedStart(
                FadeIn(squares, lag_ratio=1), Create(spiral, lag_ratio=1), run_time=5
            )
        )
        
        self.wait()
        
        self.play(squares.animate.scale(1.2).set_color(ORANGE) , spiral.animate.scale(1.2).set_color(ORANGE))
        self.play(FadeOut(squares), Uncreate(spiral[::-1]), run_time=1.5)

        # Step 5: Create Golden Ratio Explanation with Rectangles and Expression
        final_explanation = Text("Each square follows the Golden Ratio", font_size=30, color=YELLOW)
        ratio_expression = MathTex(r"\frac{a+b}{a} = \frac{a}{b}", font_size=40, color=BLUE)
        ratio_expression.next_to(final_explanation, DOWN)

        self.play(Write(final_explanation), Write(ratio_expression))
        self.play(final_explanation.animate.scale(1.2), ratio_expression.animate.scale(1.2))
        self.wait(2)
        self.play(FadeOut(final_explanation), FadeOut(ratio_expression))
        


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



