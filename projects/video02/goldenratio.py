## Path: cd Desktop/Math/GoldenMathMinds/projects/video02
## run: manim -pql goldenratio.py GoldenRatio


from manim import *

class GoldenRatioIntroduction(Scene):
    def construct(self):
        # Step 1: Display the golden ratio symbol and its value
        golden_ratio_text = MathTex(r"\phi \approx 1.618", font_size=72)
        golden_ratio_text.set_color(YELLOW)
        title = Text("The Golden Ratio", font_size=48).next_to(golden_ratio_text, UP)
        
        self.play(Write(title))
        self.play(Write(golden_ratio_text))
        self.wait(2)
        
        # Step 2: Introduce it as a special number like pi
        comparison_text = Text("Just like π, this is a very special number.", font_size=36)
        comparison_text.next_to(golden_ratio_text, DOWN)
        
        self.play(Write(comparison_text))
        self.wait(2)
        
        # Step 3: Ask where the number comes from
        question_text = Text("Where does this number come from?", font_size=36)
        self.play(FadeOut(comparison_text), FadeOut(title), golden_ratio_text.animate.shift(UP))
        self.play(Write(question_text))
        self.wait(2)
        
        # Step 4: Show Fibonacci sequence leading to the Golden Ratio
        fibonacci_text = Text("It appears in the Fibonacci Sequence...", font_size=36)
        fibonacci_text.shift(DOWN * 1.5)
        
        self.play(FadeOut(question_text))
        self.play(Write(fibonacci_text))
        
        # Show a quick representation of the Fibonacci sequence
        fibonacci_sequence = VGroup(
            MathTex("1,", "1,", "2,", "3,", "5,", "8,", "13,", "21,", "34,", "55..."),
        )
        fibonacci_sequence.arrange(RIGHT, buff=0.3).next_to(fibonacci_text, DOWN)
        
        self.play(Write(fibonacci_sequence))
        self.wait(3)
        
        # Step 5: Display examples of Golden Ratio in nature and art
        nature_text = Text("...in nature,", font_size=36, color=GREEN).shift(UP * 1.5)
        art_text = Text("...and in art & architecture.", font_size=36, color=BLUE).next_to(nature_text, DOWN)
        
        self.play(FadeOut(fibonacci_sequence), FadeOut(fibonacci_text))
        self.play(Write(nature_text))
        self.wait(2)
        self.play(Write(art_text))
        self.wait(2)
        
        # Step 6: Conclude with its importance
        importance_text = Text("The Golden Ratio reveals patterns and beauty everywhere.", font_size=32).shift(DOWN * 1.5)
        
        self.play(FadeOut(nature_text), FadeOut(art_text))
        self.play(Write(importance_text))
        self.wait(3)
        
        # End scene
        self.play(FadeOut(importance_text), FadeOut(golden_ratio_text))
