from compas.geometry import Frame
from compas.geometry import Vector
from compas.geometry import Quaternion


def frame_from_viewport(viewport):
    """
    """
    zaxis = -viewport.CameraDirection
    yaxis = viewport.CameraUp
    xaxis = Vector(*yaxis).cross(zaxis)
    return Frame(viewport.CameraLocation, xaxis, yaxis)


def viewport_by_name(name, scriptcontext):
    """
    """
    for view in scriptcontext.doc.NamedViews:
        if view.Name == name:
            return view.Viewport
    return None


def interpolate_between_quaternions(qA, qB, parameters):
    """Performs a spherical linear interpolation between 2 quaternions.
    """
    from scipy.spatial.transform import Rotation
    from scipy.spatial.transform import Slerp
    R = Rotation.from_quat([q.xyzw for q in [qA, qB]])
    slerp = Slerp([0, 1], R)
    interp_rotations = slerp(parameters)
    return [Quaternion(w, x, y, z) for x, y, z, w in interp_rotations.as_quat()]


def interpolate_between_frames(frameA, frameB, params):
    """
    """
    from scipy.interpolate import BSpline
    quaternions = interpolate_between_quaternions(frameA.quaternion,
                                                  frameB.quaternion,
                                                  params)
    crv = BSpline([0, 0, 1, 1], [frameA.point, frameB.point], 1)
    points = crv(params)
    return [Frame.from_quaternion(q, point=pt) for q, pt in zip(quaternions, points)]

def map_range(value, from_min, from_max, to_min, to_max):
    """
    """
    from_range = from_max - from_min
    to_range = to_max - to_min
    value_scaled = (value - from_min) / float(from_range)
    return to_min + (value_scaled * to_range)


if __name__ == "__main__":
    frameA = Frame((5.405, 12.412, 1.875),
                   (0.995, 0.099, 0.000), (-0.006, 0.057, 0.998))
    frameB = Frame((8.255, -13.886, 1.333),
                   (-0.988, -0.156, 0.000), (0.013, -0.083, 0.996))
    num = 10
    parameters = values = [v/(num - 1) for v in range(int(num))]
    print(interpolate_between_frames(frameA, frameB, parameters))
