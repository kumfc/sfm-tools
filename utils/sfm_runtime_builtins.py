import vs

"""
sfmConsole - builtin
sfmUtils - py
sfm - builtin
vp - py
vs - py
gLoadDataModel - py bool
gAppFactory - py vp.GetAppFactory()
StderrCatcher - builtin
SFMStdoutCatcher - builtin
sfmClipEditor - builtin
SFMStderrCatcher - builtin
StdoutCatcher - builtin
sfmApp - builtin
"""

gLoadDataModel = False  # bool checks if valve_pyd import is done
gAppFactory = object()  # vp.GetAppFactory() -> PyCObject


class StderrCatcher:
    def write(self, string):
        # type: (object, str) -> None
        """
        Probably a tweak to redirect stderr to console
        """


class StdoutCatcher:
    def write(self, string):
        # type: (object, str) -> None
        """
        Probably a tweak to redirect stdout to console
        """


class SFMStdoutCatcher(StdoutCatcher):
    pass


class SFMStderrCatcher(StderrCatcher):
    pass


class sfmConsole:
    @staticmethod
    def ClearScriptOutput():
        # type: () -> None
        """
        Clears the output in the Script Editor Console.
        """

    @staticmethod
    def SetEchoScriptOutput():
        # unknown
        """
        Enables echo of executed scripts.
        """

    @staticmethod
    def StderrMsg(steing):
        # type: (str) -> None
        """
        Used to redirect the error output of Python to the Script Editor Console.
        """

    @staticmethod
    def StdoutMsg(string):
        # type: (str) -> None
        """
        Used to redirect the output of Python to the Script Editor Console.
        """


class sfm:
    @staticmethod
    def AimConstraint():
        """
        Create an aim constraint

        name: 'Constraint Name'
        group: 'Animation Set Group Name'
        mo: 'Maintain Offset'
        w: 'Weight'
        wu: 'World up vector'
        wuSpace: 'World up space'
        refObject: 'Dag node to specify the space world up vector'
        controls: 'Create weight controls and channels'
        """

    @staticmethod
    def BeginRig():
        """
        Start a rig and make it the active rig

        append: 'Flag specifying if appending elements to an existing rig is allowed'
        """

    @staticmethod
    def ClearSelection():
        """
        Clear the current selection, removing all currently selected dag nodes
        """

    @staticmethod
    def CreateAnimationSet():
        """
        Create an animation set for the specified element

        target: 'Element for which animation set is to be created'
        """

    @staticmethod
    def CreateAttachmentHandle():
        """
        Create a dag node for an attachment point
        """

    @staticmethod
    def CreateDag():
        """
        Create a dag node and transform controls in the specified animation set

        pos: 'Dag position'
        rot: 'Rag rotation (pitch, yaw, roll)'
        animSet: 'Animation set to which the dag is to be added.'
        """

    @staticmethod
    def CreateModel():
        """
        Create a CDmeGameModel referencing the specified mdl
        """

    @staticmethod
    def CreateRigHandle():
        """
        Create a rig handle

        pos: 'Rig handle position'
        rot: 'Rig handle rotation (pitch, yaw, roll)'
        group: 'Animation Set Group Name'
        posControl: 'Create a position control and channel for the handle'
        rotControl: 'Create a rotation control and channel for the handle'
        """

    @staticmethod
    def EndRig():
        """
        End the currently active rig
        """

    @staticmethod
    def ErrMsg():
        """
        Redirects stderr
        """

    @staticmethod
    def FindDag():
        """
        Find the dag within the current or specified animation set with the specified name
        """

    @staticmethod
    def FirstSelectedDag():
        """
        Get the first dag node in the current selection.
        """

    @staticmethod
    def GenerateSamples():
        """
        Resample the position and orientation of the selected dag nodes and store in the logs for each node

        parent: 'Generate samples using the specified node as the parent'
        pos: 'Generate position values'
        rot: 'Generate rotation values'
        world: 'Generate samples in world space, ignoring the any parent'
        """

    @staticmethod
    def GetCurrentAnimationSet():
        # type: () -> vs.movieobjects.CDmeAnimationSet
        """
        Get the currently active selected animation set.
        """

    @staticmethod
    def GetCurrentFrame():
        """
        Return the shot relative frame number corresponding to the current time
        """

    @staticmethod
    def GetCurrentRig():
        """
        End the currently active rig
        """

    @staticmethod
    def GetCurrentShot():
        # type: () -> vs.movieobjects.CDmeFilmClip
        """
        Get the currently selected shot.
        """

    @staticmethod
    def GetPosition():
        """
        Get dag node position
        
        space: 'Space in which the move is to occur'
        refObject: 'Dag node to be used for reference space mode'
        """

    @staticmethod
    def GetRotation():
        """
        Get dag node position

        space: Space in which the move is to occur'
        refObject: 'Dag node to be used for reference space mode'
        """

    @staticmethod
    def IKConstraint():
        """
        Create 2-bone IK Constraint

        poleVector: 'World space pole vector'
        pvTarget: 'Pole vector target vector'
        name: 'Constraint Name'
        group: 'Animation Set Group Name'
        mo: 'Maintain Offset'
        w: 'Weight'
        controls: 'Create weight controls and channels'
        """

    @staticmethod
    def Move():
        """
        Move the currently selected dag nodes

        x: 'Amount to move along X'
        y: 'Amount to move along Y'
        z: 'Amount to move along Z'
        relative: 'Move the nodes relative to their current position'
        offsetMode: 'Apply the move as an offset over the time selection instead of an absolute value'
        space: 'Space in which the move is to occur'
        refObject: 'Dag node to be used for reference space mode'
        """

    @staticmethod
    def Msg(string):
        # type: (str) -> None
        """
        Redirects stdout
        """

    @staticmethod
    def NextSelectedDag():
        """
        Get the next selected control in the current selection.
        """

    @staticmethod
    def OrientConstraint():
        """
        Create orientation constraint

        name: 'Constraint Name'
        group: 'Animation Set Group Name'
        mo: 'Maintain Offset'
        w: 'Weight'
        controls: 'Create weight controls and channels'
        """

    @staticmethod
    def Parent():
        """
        Make primary selection the parent of all other selected dag nodes

        world: 'Parent the selected nodes to the world (unparent).'
        maintainWorldPos: 'Maintain the world space positions of the children.'
        logMode: 'Specification of how logs on the child dag are to be updated.'
        """

    @staticmethod
    def ParentConstraint():
        """
        Create parent constraint

        name: 'Constraint Name'
        group: 'Animation Set Group Name'
        mo: 'Maintain Offset'
        w: 'Weight'
        controls: 'Create weight controls and channels'
        """

    @staticmethod
    def PointConstraint():
        """
        Create point constraint

        name: 'Constraint Name'
        group: 'Animation Set Group Name'
        mo: 'Maintain Offset'
        w: 'Weight'
        controls: 'Create weight controls and channels'
        """

    @staticmethod
    def PopSelection():
        """
        Pop the current selection off of the stack and restore the previously pushed selection.
        """

    @staticmethod
    def PrintDagOperators():
        """
        Print an ordered list of operators for the selected dag node

        local: 'local only'
        """

    @staticmethod
    def PushSelection():
        """
        Push the current selection on to the stack, so that it may be restored later.
        """

    @staticmethod
    def RemoveConstraints():
        """
        Remove all constraints from the selected dag nodes
        """

    @staticmethod
    def Rotate():
        """
        Rotate the currently selected dag nodes

        x: 'Amount to move rotate around X'
        y: 'Amount to move rotate around Y'
        z: 'Amount to move rotate around Z'
        relative: 'Move the nodes relative to their current position'
        offsetMode: 'Apply the move as an offset over the time selection instead of an absolute value'
        space: 'Space in which the move is to occur'
        refObject: 'Dag node to be used for reference space mode'
        """

    @staticmethod
    def Select():
        """
        Select one or more dag nodes

        r: 'Remove the dag from the selection'
        tgl: 'Toggle selection, remove if in selection, add if not in selection'
        error: 'Error if the specified selection does not exist'
        """

    @staticmethod
    def SelectAll():
        """
        Select all of the dag nodes in the animation set
        """

    @staticmethod
    def SelectDag():
        """
        Add a dag node to the selection
        """

    @staticmethod
    def SetCurrentFrame(n):
        # type: (int) -> None
        """
        Set the current time for script operation to the specified frame relative to the start of the shot
        
        n: 'Frame number'
        """

    @staticmethod
    def SetDefault(pos, rot):
        # type: (bool, bool) -> None
        """
        Set the default position and orientation of the currently selected nodes

        pos: 'Flag indicating if the position default should be set'
        rot: 'Flag indicating if the rotation default should be set'
        """

    @staticmethod
    def SetOperationMode():
        """
        Set the current channel operation mode
        """

    @staticmethod
    def SetReferencePose():
        """
        Move the currently selected dag nodes to their reference pose position
        """

    @staticmethod
    def UsingAnimationSet():
        """
        Specify an animation set to be assumed for commands in which an animation set is not explicitly specified.
        """

    @staticmethod
    def console(string):
        # type: (str) -> None
        """
        Dispatch string to command console
        """


class sfmClipEditor:
    @staticmethod
    def GetSelectedClips():
        # type: () -> list
        """
        Returns list of currently selected clips.
        """

    @staticmethod
    def GetSelectedShots():
        # type: () -> list
        """
        Returns list of current selected shots in the Timeline.
        """


class sfmApp:
    @staticmethod
    def CloseDocument():
        """
        Closes current document. qApp will emit DocumentClosed when done.

        forceSilent: 'no dialog is shown in case of an error (True)'
        """

    @staticmethod
    def ExecuteGameCommand():
        """
        Executes the command in the game console.
        """

    @staticmethod
    def GetClipsOfTrack():
        """
        Returns a list of the clips of a track.
        """

    @staticmethod
    def GetDocumentRoot():
        """
        Returns the root of the current document or None.
        """

    @staticmethod
    def GetElementForHandle():
        """
        Returns the element for the handle, or None.
        """

    @staticmethod
    def GetFramesPerSecond():
        """
        Returns frames per second.
        """

    @staticmethod
    def GetHeadTimeInFrames():
        """
        Returns the current time in frames.
        """

    @staticmethod
    def GetHeadTimeInSeconds():
        """
        Returns the current time in seconds.
        """

    @staticmethod
    def GetMainWindow():
        """
        Returns the current QMainWindow.
        """

    @staticmethod
    def GetMovie():
        """
        Returns current active movie as CDmeFilmClip.
        """

    @staticmethod
    def GetNameForTimelineMode():
        """
        Returns current recording state.
        """

    @staticmethod
    def GetParentClip():
        """
        Returns the parent clip of a track group.
        """

    @staticmethod
    def GetParentTrack():
        """
        Returns the parent track of a clip.
        """

    @staticmethod
    def GetParentTrackGroup():
        """
        Returns the parent track group of a track.
        """

    @staticmethod
    def GetScriptController():
        """
        Returns the instance of the script controller.
        """

    @staticmethod
    def GetScriptsMenu():
        """
        Returns the script menu.
        """

    @staticmethod
    def GetShotAtCurrentTime():
        """
        Returns the clip at the current time or None.
        """

    @staticmethod
    def GetShots():
        """
        Returns list of current shots in the Timeline.
        """

    @staticmethod
    def GetTimelineMode():
        """
        Returns current recording state.
        """

    @staticmethod
    def GetTrackGroupsOfClip():
        """
        Returns a list of the track groups of a clip.
        """

    @staticmethod
    def GetTracksOfTrackGroup():
        """
        Returns a list of the tracks of a track groups.
        """

    @staticmethod
    def HasDocument():
        """
        Returns a boolean whether a document is available.
        """

    @staticmethod
    def LoadMap():
        """
        Loads a new map. qApp will emit LevelLoadingStarted when started and LevelLoadingFinished when done.

        name: 'name of the map'
        forceSilent: 'no dialog is shown in case of an error (True)'
        """

    @staticmethod
    def NewDocument():
        """
        Creates a new document. Closes the current document, if applicable

        filename: 'absolute filename of the document (last used directory with filename)'
        name: 'name of the document (last used name with a number appended)'
        framerate: 'framerate as float. (24.0)'
        defaultContent: 'create default content for the document (True)'
        forceSilent: 'no dialog is shown in case of an error (True)'
        """

    @staticmethod
    def OpenDocument():
        """
        Opens an existing document. Returns True on success. qApp will emit DocumentLoaded when done.

        filename: 'absolute filename of the document'
        forceSilent: 'no dialog is shown in case of an error (True)'
        """

    @staticmethod
    def ProcessEvents():
        """
        Calls qApp->processEvents and renders one frame. qApp will emit InteractiveRenderFinished when done with all requested rendering.
        """

    @staticmethod
    def RegisterTabWindow():
        """
        Registers a widget in the SFM Tabbed Environment.

        Pretty Name
        Internal Name
        Pointer to Widget (shiboken::getCppPointer( widget )[0] )
        """

    @staticmethod
    def RescanScriptMenus():
        """
        Rescans all menus and deletes existing content. qApp emits RescanMenuFinished when done.
        """

    @staticmethod
    def SaveDocument():
        """
        Saves the current document. Returns True on success. qApp will emit DocumentSaved when done.

        filename: 'absolute filename of the document. If missing, than uses existing path'
        forceSilent: 'no dialog is shown in case of an error (True)'
        """

    @staticmethod
    def SetHeadTimeInFrames(current_frame):
        # type: (int) -> None
        """
        Sets the current time in frames.
        """

    @staticmethod
    def SetHeadTimeInSeconds(current_time):
        # type: (int) -> None
        """
        Sets the current time in seconds.
        """

    @staticmethod
    def SetTimelineMode(state):
        # type: (int) -> None
        """
        Sets the new recording state.
        """

    @staticmethod
    def ShowTabWindow(internal_name):
        # type: (str) -> None
        """
        Show a widget in the SFM Tabbed Environment with the name Internal Name

        internal_name: 'Internal Name'
        """

    @staticmethod
    def Version():
        # type: () -> str
        """
        Version of the SFM as string in the form x.x.x.x
        """
