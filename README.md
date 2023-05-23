# GradientDescentDemo
Visuals for an explanation of gradient descent for a calculus class project


## Notes
To get rid of a warning about `Unsupported element type: <class 'svgelements.svgelements.Use'>`, line 153 of `mobject/svg/svg_mobject.py` was changed to `if isinstance(shape, (se.Group, se.Use)):
`. See https://github.com/3b1b/manim/issues/1904 for more details.

To run an animation and save it as a GIF:
`source venv/bin/activate`
`manimgl ClassName.py ClassName -w -i -l --file_name out.gif --frame_rate 15`

Assume all GIFs have an FPS of 15 unless specified otherwise in the file name.
