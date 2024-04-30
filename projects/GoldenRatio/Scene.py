from manim import *

class GoldenRatio(Scene):
    def construct(self):
        # Create two squares
        square1 = Square(side_length=2, color=BLUE, fill_opacity=0.5)
        square2 = Square(side_length=1, color=RED, fill_opacity=0.5)

        # Position squares
        square1.shift(LEFT * 3)
        square2.next_to(square1, RIGHT, buff=0)

        # Calculate golden ratio
        golden_ratio = (1 + np.sqrt(5)) / 2

        # Create rectangles inside squares
        rect1 = Rectangle(height=2, width=2/golden_ratio, color=BLUE, fill_opacity=0.5)
        rect2 = Rectangle(height=1, width=1/golden_ratio, color=RED, fill_opacity=0.5)

        # Position rectangles
        rect1.next_to(square1, DOWN, buff=0)
        rect2.next_to(square2, DOWN, buff=0)

        # Create labels
        label1 = MathTex("a").next_to(square1, UP)
        label2 = MathTex("b").next_to(square2, UP)
        label3 = MathTex("a").next_to(rect1, RIGHT)
        label4 = MathTex("b").next_to(rect2, RIGHT)
        label5 = MathTex("a").next_to(rect1, DOWN)
        label6 = MathTex("b").next_to(rect2, DOWN)

        # Show squares, rectangles, and labels
        self.play(Create(square1), Create(square2))
        self.play(Create(rect1), Create(rect2))
        self.play(Write(label1), Write(label2), Write(label3), Write(label4), Write(label5), Write(label6))

        # Add arrows and ratios
        arrow1 = Arrow(label1.get_right(), label3.get_left(), color=YELLOW)
        arrow2 = Arrow(label2.get_right(), label4.get_left(), color=YELLOW)
        ratio1 = MathTex(r"\frac{a}{b}").next_to(arrow1, UP, buff=0.1)
        ratio2 = MathTex(r"\frac{a}{b}").next_to(arrow2, UP, buff=0.1)

        self.play(Create(arrow1), Create(arrow2))
        self.play(Write(ratio1), Write(ratio2))

        # Explain golden ratio
        explanation = MathTex(r"\text{The golden ratio: } \frac{a+b}{a} = \frac{a}{b}", color=GREEN).next_to(rect1, RIGHT)
        explanation.shift(DOWN * 1.3)
        explanation.shift(RIGHT )
        self.play(Write(explanation))

        self.wait(2)
