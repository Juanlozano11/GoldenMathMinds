## path : cd Desktop/Math/GoldenMathMinds/projects/video04
## run :  manim -pql equation.py SimpleMathProblem


from manim import *

class SimpleMathProblem(Scene):
    def construct(self):
        # Title with gradient and gentle scaling
        title = Text("Can you solve this?", font_size=48).set_color_by_gradient(PINK, BLUE_B, TEAL_C)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.shift(UP * 2).scale(1.2))
        self.wait(0.5)

        # Displaying the problem with a smooth appearance and wave effect
        problem = MathTex(r"2^3 + 3! - \sum_{n=1}^{2} (1 + n)", font_size=48)
        problem.set_color_by_gradient(PURPLE, BLUE, YELLOW_C)
        problem.shift(DOWN * 0.5)

        # Wave animation effect on each character
        for i, char in enumerate(problem):
            char.generate_target()
            char.target.shift(UP * 0.2 if i % 2 == 0 else DOWN * 0.2)
        self.play(Write(problem), *[MoveToTarget(char, rate_func=there_and_back) for char in problem], run_time=2)

        self.wait(1)

        # Display answer with typewriter effect
        answer = MathTex(r"= 8 + 6 - 5 = 9", font_size=48, color=GREEN_C).next_to(problem, DOWN, buff=0.5)
        for i, char in enumerate(answer):
            self.play(Write(char), run_time=0.2)

        # Hold answer briefly
        self.wait(1)

        # Clean up problem and answer
        self.play(FadeOut(title), FadeOut(problem), FadeOut(answer), run_time=1.5)

        # Golden Ratio Spiral for an aesthetic transition
        spiral = ParametricFunction(
            lambda t: np.array([np.cos(t) * (1.618 ** (t / (2 * np.pi))),
                                np.sin(t) * (1.618 ** (t / (2 * np.pi))),
                                0]),
            t_range=[0, 4 * PI],
            color=TEAL_B
        ).scale(0.5).shift(LEFT)
        self.play(Create(spiral), run_time=3)
        
        # Glowing dot tracing part of the spiral
        trace_dot = Dot(color=MAROON_C, radius=0.1).move_to(spiral.get_start())
        glow = Dot(color=YELLOW, radius=0.2, fill_opacity=0.3).move_to(trace_dot.get_center())
        
        # Moving dot and glow effect along spiral
        self.add(glow)
        self.play(MoveAlongPath(trace_dot, spiral, rate_func=linear), run_time=3)
        self.play(FadeOut(glow), FadeOut(trace_dot), FadeOut(spiral))

        # Final logo with shadow effect
        logo_text_shadow = Text("Golden Math Minds", font_size=44, color=GREY_B).shift(DOWN * 0.05 + RIGHT * 0.05)
        logo_text = Text("Golden Math Minds", font_size=44, color=WHITE)
        
        self.add(logo_text_shadow)  # Shadow effect behind main text
        self.play(Write(logo_text), run_time=2)
        self.wait(1.5)

        # Fade out for a smooth ending
        self.play(FadeOut(logo_text), FadeOut(logo_text_shadow), run_time=2)
