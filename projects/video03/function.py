## path: cd Desktop/Math/GoldenMathMinds/projects/video03
## ## run: manim -pql function.py function

from manim import *

class SineAndCosineWithTangentTrace(Scene):
    def construct(self):
        # Set up axes without automatic coordinates
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI / 2],  # x-axis from -2π to 2π with π/2 intervals
            y_range=[-4, 4, 1],  # y-axis from -4 to 4 with intervals of 1
            x_length=10,  # Adjust length for better visibility
            y_length=6,
            axis_config={"color": WHITE},
            tips=False
        )

        # Manually adding labels for -2π, -π, 0, π, 2π
        labels = {
            -2 * PI: MathTex(r"-2\pi"),
            -PI: MathTex(r"-\pi"),
            0: MathTex(r"0"),
            PI: MathTex(r"\pi"),
            2 * PI: MathTex(r"2\pi")
        }

        for x_val, label in labels.items():
            label.next_to(axes.c2p(x_val, 0), DOWN)
            self.add(label)

        # Labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("sin(x)")

        # Define the sine wave
        sine_curve = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[-2 * PI, 2 * PI])
        
        # Create a ValueTracker to move the dot along the sine curve
        x_tracker = ValueTracker(-2 * PI)
        
        # Create a dot that will follow the sine curve
        moving_dot = Dot(color=YELLOW).move_to(axes.i2gp(x_tracker.get_value(), sine_curve))
        
        # Update the dot's position along the sine curve based on x_tracker
        moving_dot.add_updater(lambda d: d.move_to(axes.i2gp(x_tracker.get_value(), sine_curve)))

        # Create a longer tangent line to represent the slope at each point on the sine curve
        tangent_line = always_redraw(
            lambda: axes.get_secant_slope_group(
                x_tracker.get_value(),
                sine_curve,
                dx=0.01,
                secant_line_length=4  # Increase length of the tangent line
            ).set_color(GREEN)
        )

        # Create a ValueTracker for the phase shift of the cosine function
        phase_tracker = ValueTracker(0)

        # Cosine curve that traces the derivative, with a dynamic phase shift
        cosine_trace = always_redraw(
            lambda: axes.plot(
                lambda x: np.cos(x + phase_tracker.get_value()),  # Apply phase shift from phase_tracker
                color=RED,
                x_range=[-2 * PI, x_tracker.get_value()]  # Extend x_range as x_tracker increases
            )
        )

        # Display the value of x in the format "x = " followed by the current value, positioned at the dot
        x_value_display = always_redraw(
            lambda: MathTex(f"x = {round(x_tracker.get_value(), 2)}", color=BLUE).scale(0.5)
            .next_to(moving_dot, UP, buff=0.3)
        )

        # Display the value of cos(x) near the cosine trace in red
        cos_value_display = always_redraw(
            lambda: MathTex(f"f'(x) = {round(np.cos(x_tracker.get_value() + phase_tracker.get_value()), 2)}", color=RED).scale(0.5)
            .next_to(axes.c2p(x_tracker.get_value(), np.cos(x_tracker.get_value() + phase_tracker.get_value())), UP, buff=0.3)
        )

        # Animation
        self.play(Write(axes), Write(x_label), Write(y_label))
        self.play(Create(sine_curve), run_time=2)
        self.wait(0.3)

        # Add the dot, tangent line, cosine trace, x value display, and cos(x) value display
        self.add(moving_dot, tangent_line, cosine_trace, x_value_display, cos_value_display)
        
        # Position t1 below the axes
        t1 = Text("Notice that this new function differs slightly from sin(x), only by a phase shift")
        
        t1.to_edge(DOWN)
        
        
        # Animate the sine wave with color shift and move the dot across the curve
        self.play(
            x_tracker.animate.set_value(2 * PI),  # Move the dot from -2π to 2π
            sine_curve.animate.set_color_by_gradient(BLUE, GREEN, YELLOW),  # Color gradient
            run_time=6,  # Extended duration for a smoother, longer animation
            rate_func=linear
        )

        self.play(Write(t1.scale(0.5)))  # Adjust scale and animate
        self.wait(2) 

        # Shift the cosine trace by -π/2 smoothly
        self.play(phase_tracker.animate.set_value(-PI / 2), run_time=2)
        self.wait(1)

        # Replace t1 with a new explanatory text
        self.play(FadeOut(t1))  # Fade out the previous text smoothly

        # Position t2 below the axes, same as t1
        t2 = Text("This shows that this path is just the derivative of sin(x), shifted by -π/2, making it cos(x).")
        t2.to_edge(DOWN)  # Position t2 at the bottom of the screen
        self.play(Write(t2.scale(0.5)))
        self.wait(2)  # Pause for readability

        # Shift the cosine trace back to its original position
        self.play(phase_tracker.animate.set_value(0), run_time=2)
        self.wait(1)

        # Fade out the explanatory text before the final clean-up
        self.play(FadeOut(t2))

        # Clean up the scene smoothly by fading out remaining elements
        self.play(Uncreate(moving_dot), Uncreate(tangent_line), Uncreate(sine_curve), Uncreate(cosine_trace))
        self.play(FadeOut(axes), FadeOut(x_label), FadeOut(y_label), *[FadeOut(label) for label in labels.values()])
        self.play(Uncreate(cos_value_display), Uncreate(x_value_display))

        # Position t3 at the top for the concluding statement
        t3 = MathTex(r"\text{Thus, we have found that the derivative of } \sin(x) \text{ is } \cos(x):")
        t4 = MathTex(r"f'(x) = \frac{d}{dx} \sin(x) = \cos(x)")
        t3.to_edge(UP)  # Position t3 at the top of the screen
        

        self.play(Write(t3))
         # Short pause to allow reading
        
        self.play(Write(t4), Write(t3))
        self.play(Uncreate(t3), Uncreate(t4))
        






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

