# GradientDescentDemo
Visuals for an explanation of gradient descent for a calculus class project


## Notes
To get rid of a warning about `Unsupported element type: <class 'svgelements.svgelements.Use'>`, line 153 of `mobject/svg/svg_mobject.py` was changed to `if isinstance(shape, (se.Group, se.Use)):
`. See https://github.com/3b1b/manim/issues/1904 for more details.

To run an animation and save it as an MP4:
`source venv/bin/activate`
`manimgl ClassName.py ClassName -w --hd --file_name out.mp4 --frame_rate 60`

Assume all animations have an FPS of 60 unless specified otherwise in the file name.

Saving as a GIF creates files that are easily hundreds of MB, so MP4 is preferred.
