import sfmUtils


# no remap, lightweight
def create_attr_slider(attr_name, dag_name, dag_transform, parent_group, animation_set, shot):
    control_name = dag_name + '_' + attr_name

    dag_transform.AddAttributeAsFloat(attr_name)
    dag_transform.SetValue(attr_name, 1.0)
    attr_control, attr_val = sfmUtils.CreateControlledValue(control_name, "value", vs.AT_FLOAT, 1.0, animation_set, shot)

    attr_connection = sfmUtils.CreateConnection(control_name, attr_val, "value", animation_set)
    attr_connection.AddOutput(dag_transform, attr_name)
    parent_group.AddControl(attr_control)


# remapable
def create_attr_slider_with_remap(attr_name, dag_name, dag_transform, parent_group, animation_set, shot):
    control_name = dag_name + '_' + attr_name

    dag_transform.AddAttributeAsFloat(attr_name)
    dag_transform.SetValue(attr_name, 1)

    attr_control = sfmUtils.CreateControlAndChannel(control_name, vs.AT_FLOAT, 0.5, animation_set, shot)

    attr_expr = sfmUtils.CreateExpression(control_name + '_expr', 'lerp(value, lo, hi)', animation_set)
    sfmUtils.AddAttributeToElement(attr_expr, "hi", vs.AT_FLOAT, 2)
    sfmUtils.AddAttributeToElement(attr_expr, "lo", vs.AT_FLOAT, 0)
    sfmUtils.AddAttributeToElement(attr_expr, "value", vs.AT_FLOAT, 0.5)
    attr_control.channel.toElement = attr_expr
    attr_control.channel.toAttribute = "value"

    attr_connection = sfmUtils.CreateConnection(control_name + '_conn', attr_expr, "result", animation_set)
    attr_connection.AddOutput(dag_transform, attr_name)
    parent_group.AddControl(attr_control)


# fixed size remap with the use of simplified expression
def create_attr_slider_fixed_size(attr_name, dag_name, dag_transform, parent_group, animation_set, shot):
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
