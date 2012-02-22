from rawgl import gl as _gl

from GLObject import BindableObject

class TransformFeedback(BindableObject): # TODO
    _generate_id = _gl.glGenTransformFeedbacks
    _delete_id = _gl.glDeleteTransformFeedbacks
    _binding = "transform_feedback_binding"
    _target = _gl.GL_TRANSFORM_FEEDBACK

    # TODO glBeginTransformFeedback, glPauseTransformFeedback, glResumeTransformFeedback, glEndTransformFeedback etc.

