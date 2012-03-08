"""Transform feedback class.

@bug: Transform feedback is currently unimplemented.
@todo: Implement this using C{glBeginTransformFeedback},
C{glPauseTransformFeedback}, C{glResumeTransformFeedback},
C{glEndTransformFeedback}, C{glDrawTransformFeedback},
C{glDrawTransformFeedbackInstanced}, C{glDrawTransformFeedbackStream}, and
C{glDrawTransformFeedbackStreamInstanced}.

@author: Stephan Wenger
@date: 2012-02-29
"""

from rawgl import gl as _gl

from glitter.utils import ManagedObject, BindableObject

class TransformFeedback(ManagedObject, BindableObject):
    _generate_id = _gl.glGenTransformFeedbacks
    _delete_id = _gl.glDeleteTransformFeedbacks
    _db = "transform_feedbacks"
    _binding = "transform_feedback_binding"
    _target = _gl.GL_TRANSFORM_FEEDBACK

__all__ = ["TransformFeedback"]

