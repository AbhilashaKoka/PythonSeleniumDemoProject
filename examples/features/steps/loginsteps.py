from behave import given, when,then
@given(u'User is on Landing Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User is on Landing Page')


@when(u'User enter details username, email, current address, permanent address')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enter details username, email, current address, permanent address')


@when(u'Click on Submit')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on Submit')


@then(u'user should able to verify the detail on output area')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user should able to verify the detail on output area')

