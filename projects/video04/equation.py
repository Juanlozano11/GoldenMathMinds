## path : cd Desktop/Math/GoldenMathMinds/projects/video04
## run :  manim -pql equation.py SimpleMathProblem


from manim import *

class SimpleMathProblem(Scene):
    def construct(self):
        # Title text: "Can you solve this?"
        title = Text("Can you solve this?", font_size=48).set_color_by_gradient(PINK, BLUE_B, TEAL_C)
        self.play(Write(title))
        
        self.play(title.animate.shift(UP * 2))
        self.play(title.animate.scale(1.2))

        # Display a simple equation: (2^3) + 3! - Σ (1+2) with gradient color
        problem = MathTex(r"2^3 + 3! - \sum_{n=1}^{2} (1 + n)", font_size=48).set_color_by_gradient(PURPLE, BLUE, YELLOW_C)

         
        
        self.play(Create(problem))
        self.play(problem.animate.scale(1.2))
        self.wait(3)

        # Display the answer with gradient color after a pause
        #answer = MathTex(r"= 8 + 6 - 5 = 9", font_size=48)
        #answer.set_color_by_gradient(GREEN, YELLOW)  # Apply gradient color
        #self.play(Transform(problem, answer))
        #self.wait(2)

        self.play(Uncreate(title), Uncreate(problem))

        # Golden Ratio Spiral (one smooth rotation)
        spiral = ParametricFunction(
            lambda t: np.array([np.cos(t) * (1.618 ** (t / (2 * np.pi))),
                                np.sin(t) * (1.618 ** (t / (2 * np.pi))),
                                0]),
            t_range=[0, 2 * PI],
            color=TEAL_B
        ).scale(0.5).shift(LEFT)
        
        # Dot tracing part of the spiral, stopping midway
        trace_dot = Dot(color=MAROON_C).move_to(spiral.get_start())
        halfway_point = spiral.point_from_proportion(0.5)
        
        # Euler's Identity with elegant text
        euler_identity = MathTex("e^{i\\pi} + 1 = 0", color=LIGHT_GREY).scale(1.3).next_to(trace_dot, 3 * DOWN, buff=0.3)

        # "Golden Math Minds" with gradient effect
        logo_text = Text("Golden Math Minds", font_size=44).set_color_by_gradient(YELLOW, ORANGE, GOLD)
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

# Explanation:
# 2^3 = 8
# 3! = 6
# Σ(1 + n) for n=1 to 2 -> (1+1) + (1+2) = 2 + 3 = 5
# So, 8 + 6 - 5 = 9
