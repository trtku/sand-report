import json
from compas.base import Base
from compas.geometry import Frame
from compas.utilities import DataEncoder
from compas.utilities import DataDecoder

LINEAR = 0


class Animation(Base):
    def __init__(self, name, duration, type=None):
        self.name = name
        self.duration = duration
        self.type = type
        self.frames_per_second = 24
        self.interpolation_type = LINEAR

    @classmethod
    def from_json(cls, filepath):
        """Construct a primitive from structured data contained in a json file.

        Parameters
        ----------
        filepath : str
            The path to the json file.

        Returns
        -------
        object
            An object of the type of ``cls``.

        Notes
        -----
        This constructor method is meant to be used in conjunction with the
        corresponding *to_json* method.
        """
        with open(filepath, 'r') as fp:
            data = json.load(fp, cls=DataDecoder)
        return cls.from_data(data)

    def to_data(self):
        """Returns the data dictionary that represents the primitive.

        Returns
        -------
        dict
            The object's data.
        """
        return self.data

    def to_json(self, filepath):
        """Serialise the structured data representing the primitive to json.

        Parameters
        ----------
        filepath : str
            The path to the json file.
        """
        with open(filepath, 'w+') as f:
            json.dump(self.data, f, cls=DataEncoder)

    @property
    def data(self):
        return {'name': self.name,
                'duration': self.duration,
                'type': self.type,
                'frames_per_second': self.frames_per_second}

    @classmethod
    def from_data(cls, data):
        raise NotImplementedError


class TransformAnimation(Animation):
    def __init__(self, name, duration, frames):
        super(TransformAnimation, self).__init__(name, duration, type="Transform")
        self.frames = frames
        if len(frames) > self.frames_per_second * self.duration:
            raise ValueError("The number of frames must be smaller than %d * duration" % self.frames_per_second)

    @classmethod
    def from_data(cls, data):
        frames = [Frame.from_data(d) for d in data['frames']]
        return cls(data['name'], data['duration'], frames)
    
    @property
    def data(self):
        return {'name': self.name,
                'duration': self.duration,
                'type': self.type,
                'frames_per_second': self.frames_per_second,
                'frames': [f.data for f in self.frames]}


if __name__ == "__main__":
    import os
    from compas.geometry import Point, Vector
    frames = [Frame(Point(18.319, -22.464, 16.481), Vector(-0.891, -0.454, 0.000), Vector(-0.227, 0.446, 0.866)),
              Frame(Point(8.255, -13.886, 1.533), Vector(-0.996, -0.093, -0.000), Vector(-0.000, 0.000, 1.000))]
    animation = TransformAnimation("anim1", 8, frames)
    data = animation.data
    print(TransformAnimation.from_data(data))
    filepath = os.path.join(os.path.dirname(__file__), "animations.json")
    print(filepath)
    animation.to_json(filepath)
