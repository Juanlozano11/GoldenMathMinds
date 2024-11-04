## Path: cd Desktop/Math/GoldenMathMinds/projects/video01
## run: manim -pql euler_identity_simple.py EulerIdentityExplanation

from manim import *

class CreativeEulerExplanation(Scene):
    def construct(self):
        # Initial title and introduction
        title = Text("Exploring Euler's Identity", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction text and first function
        intro_text = Text("Consider this function: ", font_size=24).next_to(title, DOWN)
        self.play(Write(intro_text))
        self.wait(1)

        formula1 = MathTex(r"f(x) = \left(1 + \frac{1}{x}\right)^x", font_size=48).set_color(TEAL).to_edge(UP).shift(RIGHT * 2)
        self.play(FadeOut(intro_text), Write(formula1))
        self.wait(1)

        # Set up axes with labels and numerical ticks
        axes = Axes(
            x_range=[1, 50, 5], y_range=[0, 3, 0.5],
            x_length=7, y_length=5,
            axis_config={"color": GREY}
        ).shift(DOWN)

        # Numerical labels for x and y axes
        x_label = axes.get_x_axis_label(r"x", direction=DOWN)
        y_label = axes.get_y_axis_label(r"f(x)", direction=LEFT)
        axes_labels = VGroup(x_label, y_label)
        
        graph1 = axes.plot(lambda x: (1 + 1/x)**x, x_range=[1, 50], color=BLUE)

        # Display first graph with explanation text
        expl_text1 = Text("As x grows, f(x) approaches a special constant.", font_size=24).next_to(formula1, DOWN)
        
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph1), Write(expl_text1))
        self.wait(2)

        # Transition to (1 + pi/x)^x
        self.play(FadeOut(graph1), FadeOut(expl_text1))
        formula2 = MathTex(r"f(x) = \left(1 + \frac{\pi}{x}\right)^x", font_size=48).set_color(GREEN).to_edge(UP).shift(RIGHT * 2)
        expl_text2 = Text("Now, let's use π instead of 1.", font_size=24).next_to(formula2, DOWN)
        self.play(Transform(formula1, formula2), Write(expl_text2))
        self.wait(1)

        # Plot (1 + pi/x)^x
        graph2 = axes.plot(lambda x: (1 + np.pi / x)**x, x_range=[1, 50], color=GREEN)
        pi_approx_label = MathTex(r"\left(1 + \frac{\pi}{x}\right)^x", font_size=36, color=GREEN).next_to(graph2, UP)

        self.play(Create(graph2), Write(pi_approx_label))
        self.wait(2)

        # Transition to complex (1 + i*pi/x)^x
        self.play(FadeOut(graph2), FadeOut(pi_approx_label), FadeOut(expl_text2))
        formula3 = MathTex(r"f(x) = \left(1 + \frac{i \pi}{x}\right)^x", font_size=48).set_color(PURPLE).to_edge(UP).shift(RIGHT * 2)
        expl_text3 = Text("What happens when we add an imaginary component?", font_size=24).next_to(formula3, DOWN)
        self.play(Transform(formula1, formula3), Write(expl_text3))
        self.wait(1)

        # Plot (1 + i*pi/x)^x for different values of x
        complex_graphs = VGroup()
        for x_val in [1, 5, 10, 20, 50]:
            complex_point = Dot(axes.c2p(x_val, np.abs((1 + 1j * np.pi / x_val)**x_val)), color=PURPLE)
            complex_graphs.add(complex_point)
            self.play(FadeIn(complex_point), run_time=0.5)
        
        # Display all points for the complex function at various values of x
        self.play(ShowIncreasingSubsets(complex_graphs), run_time=2)
        self.wait(1)

        # Clear elements and introduce Euler's Identity
        self.play(FadeOut(title), FadeOut(axes), FadeOut(complex_graphs), FadeOut(formula1), FadeOut(expl_text3))
        euler_identity = MathTex("e^{i\\pi} + 1 = 0", font_size=72).set_color(WHITE).move_to(ORIGIN).shift(UP * 1.5 + RIGHT * 1.5)
        outro = Text("The beauty of Euler's Identity!", font_size=36, color=YELLOW)
        outro.next_to(euler_identity, DOWN)

        self.play(Write(euler_identity))
        self.play(Write(outro))
        self.wait(2)

        self.play(FadeOut(euler_identity), FadeOut(outro))
