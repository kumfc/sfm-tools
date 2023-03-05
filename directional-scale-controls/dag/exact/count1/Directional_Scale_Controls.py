import traceback
import sys
import sfmUtils
from PySide import *

try:
    sfm
except NameError:
    from sfm_runtime_builtins import *


class Log():
    @staticmethod
    def info(msg):
        sfm.Msg('[Python] [*] ' + str(msg) + '\n')

    @staticmethod
    def debug(msg):
        if debug:
            sfm.Msg('[Python] [DEBUG] ' + str(msg) + '\n')


def MessageBoxInfo(text, window):
    msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, "Info", text, QtGui.QMessageBox.NoButton, window)
    msgBox.addButton("&Continue", QtGui.QMessageBox.RejectRole)
    if msgBox.exec_() == QtGui.QMessageBox.AcceptRole:
        pass


def MessageBoxError(text, window):
    msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Error", text, QtGui.QMessageBox.NoButton, window)
    msgBox.addButton("&Continue", QtGui.QMessageBox.RejectRole)
    if msgBox.exec_() == QtGui.QMessageBox.AcceptRole:
        pass


debug = True
log = Log()
w = QtGui.QMainWindow()


# may cause lag in certain conditions, but more user-friendly
def create_attr_slider(attr_name, dag_name, dag_transform, parent_group, animation_set, shot):
    control_name = dag_name + '_' + attr_name

    dag_transform.AddAttributeAsFloat(attr_name)
    dag_transform.SetValue(attr_name, 1)

    attr_control = sfmUtils.CreateControlAndChannel(control_name, vs.AT_FLOAT, 0.125, animation_set, shot)

    attr_expr = sfmUtils.CreateExpression(control_name + '_expr', 'v*8', animation_set)
    sfmUtils.AddAttributeToElement(attr_expr, 'v', vs.AT_FLOAT, 0.125)
    attr_control.channel.toElement = attr_expr
    attr_control.channel.toAttribute = 'v'

    attr_connection = sfmUtils.CreateConnection(control_name + '_conn', attr_expr, 'result', animation_set)
    attr_connection.AddOutput(dag_transform, attr_name)
    parent_group.AddControl(attr_control)


# for full potential this implementation requires Flex Unlocker
def create_attr_slider_simple(attr_name, dag_name, dag_transform, parent_group, animation_set, shot):
    control_name = dag_name + '_' + attr_name

    dag_transform.AddAttributeAsFloat(attr_name)
    dag_transform.SetValue(attr_name, 1.0)
    attr_control, attr_val = sfmUtils.CreateControlledValue(control_name, "value", vs.AT_FLOAT, 1.0, animation_set, shot)

    attr_connection = sfmUtils.CreateConnection(control_name, attr_val, "value", animation_set)
    attr_connection.AddOutput(dag_transform, attr_name)
    parent_group.AddControl(attr_control)


def main():
    shot = sfm.GetCurrentShot()
    animation_set = sfm.GetCurrentAnimationSet()

    try:
        sfm.scale_patch_applied
    except AttributeError:
        MessageBoxInfo('Don\'t forget to run the "Directional Scale Patch" from Scripts menu!', w)

    target_dag = sfm.FirstSelectedDag()
    log.debug(target_dag.GetName())
    dag_control = animation_set.FindTransformControl(target_dag)
    dag_name = dag_control.GetName()
    dag_transform = target_dag.GetTransform()
    log.debug('selected_dag: ' + str(target_dag))

    if dag_name == 'rootTransform':
        MessageBoxInfo('Can\'t apply this script to rootTransform control. Use real bone root instead (bip_pelvis, static_prop etc.)', w)
        return

    if dag_transform.HasAttribute("scale_x"):
        MessageBoxInfo('This script is already applied to {}!'.format(dag_name), w)
        return

    root_control_group = animation_set.GetRootControlGroup()
    parent_group = root_control_group.FindGroupContainingControl(dag_control)
    log.debug('{} -> {}'.format(parent_group.GetName(), dag_name))

    group_name = dag_name + "_rescale"
    new_group = root_control_group.CreateControlGroup(group_name)
    new_group.SetGroupColor(vs.Color(0, 255, 0, 255), False)
    parent_group.AddChild(new_group)

    if dag_transform.HasAttribute('scale'):
        sfmUtils.MoveControlGroup(dag_name + '_scale', parent_group, new_group)
    else:
        create_attr_slider("scale", dag_name, dag_transform, new_group, animation_set, shot)

    create_attr_slider("scale_x", dag_name, dag_transform, new_group, animation_set, shot)
    create_attr_slider("scale_y", dag_name, dag_transform, new_group, animation_set, shot)
    create_attr_slider("scale_z", dag_name, dag_transform, new_group, animation_set, shot)


try:
    main()
except:
    MessageBoxError('An exception occurred during script execution, check console for detailed information.', w)
    traceback.print_exc(file=sys.stderr)
