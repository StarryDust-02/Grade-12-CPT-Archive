from utils import utility
from utils.settings import *


class Animation(object):
    """Get character pixels and their movement
    
    """

    def __init__(self):
        """The different variables used in control the animation
        Variables:
            sequence_dict: save current animations
            current_sequence: the current sequence of animation
            frame_dict: the frames of the animation
            current_frame: the current frame
            is_playing: bool, determine if the animation is playing
            parent: (if there is) the parent function
            dt: delta time
        
        """
        self.__sequence_dict = {} # A dict to save current animations
        self.__current_sequence = 0
        self.__frame_dict = {}
        self.__current_frame = 0
        self.is_playing = True
        self.image = None
        self.parent = None
        self.play_dt = 1
        self.dt = 1/15*FRAME_PER_SECOND

    def __bool__(self):
        if self.__sequence_dict and self.__frame_dict:
            return True
        else:
            return False

    def set_parent(self, parent: object):
        self.parent = parent
        self.parent.image = self.image


    def update(self):
        """The frame counter
        
        """
        if self.is_playing and self.dt%self.play_dt == 0:
            self.__current_frame += 1
        if self.__current_frame > len(self.__sequence_dict[self.__current_sequence]) - 1:
            self.__current_frame = 0
        self.dt += 1
        self.image = self.__sequence_dict[self.__current_sequence][self.__current_frame]

    def play_animation(self, sequence_id, frame_id=0):
        """Play the animation
        
        """
        self.is_playing = True

        if self.__current_sequence != sequence_id:
            self.__current_sequence = sequence_id
            self.__current_frame = frame_id
    
    def del_animation(self, sequence_id):
        """Delete animation
        
        """
        try:
            del self.__sequence_dict[sequence_id]
        except:
            pass

    def stop_animation(self, sequence_id=None, frame_id=0):
        """Stop the animation
        
        """
        self.is_playing = False

        if sequence_id:
            self.__current_sequence = sequence_id
        
        if frame_id:
            self.__current_frame = frame_id

    def build_animation(self, sequence_id, frames, scale=1, rotation=0, dim_value=255, flip=[False, False]):
        """Build the animation
        
        """
        self.__sequence_dict[sequence_id] = []
        if not self.__current_sequence:
            self.__current_sequence = sequence_id

        # check frames is a list or a single image
        try:
            for frame in frames:
                try: # check if the frame exists
                    self.__sequence_dict[sequence_id].append(self.__frame_dict[frame])
                    
                except:
                    self.__frame_dict[frame] = (utility.load_image(frame, scale, rotation, dim_value, flip))
                    self.__sequence_dict[sequence_id].append(self.__frame_dict[frame])

        except:
            try: # check if the frame exists
                self.__sequence_dict[sequence_id].append(self.__frame_dict[frames])
        
            except:
               self.__frame_dict[frames] = (utility.load_image(frames, scale, rotation, dim_value, flip))
               self.__sequence_dict[sequence_id].append(self.__frame_dict[frames])

        self.image = self.__sequence_dict[self.__current_sequence][self.__current_frame]
