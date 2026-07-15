from pytest_bdd import when, scenarios
from testing.bdd.conftest import legacy_name


scenarios('features/validation/delayTimingType.feature')


@when(**legacy_name(name='ebuttm:authoringDelay attribute has value <authoring_delay>'))
def when_authoring_delay(authoring_delay, template_dict):
    template_dict['authoring_delay'] = authoring_delay
