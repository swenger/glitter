from rawgl import gl as _gl

from util import BindableObject

class TransformFeedback(BindableObject): # TODO
    _generate_id = _gl.glGenTransformFeedbacks
    _delete_id = _gl.glDeleteTransformFeedbacks
    _bind = _gl.glBindTransformFeedback
    _binding = _gl.GL_TRANSFORM_FEEDBACK_BINDING
    _target = _gl.GL_TRANSFORM_FEEDBACK

    # TODO glBeginTransformFeedback, glPauseTransformFeedback, glResumeTransformFeedback, glEndTransformFeedback etc.

