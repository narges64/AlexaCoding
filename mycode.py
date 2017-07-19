"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function


A = 0
B = 0
C = 0
D = 0
repeat = 1
check_condition = True
store_condition = False

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response(session_attributes):

    card_title = "Welcome"
    speech_output = "Welcome to the Alexa Coding. " \
                    "You can start saying your program now "

    reprompt_text = "Please Start! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Coding. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def update_program_states(session, new_condition):
    session_attributes = {}
    session_attributes=session['attributes']
    store = session_attributes['store_condition']
    session_attributes['check_condition'] = (not store) and new_condition
    session_attributes['store_condition'] = store or new_condition

def assign_intent(intent, session):
    session_attributes = {}
    session_attributes = session['attributes']
    condition = session_attributes['check_condition']

    card_title = "MyCode"
    if (condition):
        the_var = intent['slots']['Variable']['value']
        the_val = intent['slots']['Value']['value']
        session_attributes[the_var] = the_val
        exec(the_var + " = " + str(the_val))
        speech_output = the_var  + " is now " + str(the_val)
    else:
        speech_output = ""

    reprompt_text = "Please say next statement. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def print_intent(intent, session):
    session_attributes = {}
    session_attributes = session['attributes']
    condition = session_attributes['check_condition']

    card_title = "MyCode"
    if(condition):
        variable = intent['slots']['Variable']['value']
        temp = session_attributes[variable]
        speech_output = variable +  " is " + str(temp)
    else:
        speech_output = ""

    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def add_intent(intent, session):
    session_attributes = {}
    session_attributes = session['attributes']
    condition = session_attributes['check_condition']

    card_title = "MyCode"
    if (condition):
        the_var = intent['slots']['Variable']['value']
        the_val = intent['slots']['Value']['value']
        temp = session_attributes[the_var]
        repeat = session_attributes['repeat']
        temp2 = int(temp)
        for i in range (0, int(repeat)):
            temp2 = temp2 + int(the_val)

        session_attributes['repeat'] = 1
        session_attributes[the_var] = temp2
        speech_output = "Add is done! use print to get the new value"
    else:
        speech_output = ""
    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def addtwo_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']
    condition = session_attributes['check_condition']

    card_title = "MyCode"
    if (condition):
        thefirst_var = intent['slots']['VariableFirst']['value']
        thesecond_var = intent['slots']['VariableSecond']['value']
        thethird_var = intent['slots']['VariableThird']['value']
        thefirst_val = session_attributes[thefirst_var]
        thesecond_val = session_attributes[thesecond_var]
        thethird_val=int(thefirst_val)+int(thesecond_val)
        session_attributes[thethird_var]=thethird_val
        speech_output = "Add is done! use print to get the new value"
    else:
        speech_output = ""
    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def loop_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']
    condition = session_attributes['check_condition']

    card_title = "MyCode"
    if (condition):
        start = intent['slots']['Start']['value']
        end = intent['slots']['End']['value']
        function = intent['slots']['Function']['value']

        for i in range (start, end):
            on_intent(function, session)

        speech_output = "Loop is done"
    else:
        speech_output = ""
    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def repeat_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']
    condition = session_attributes['check_condition']

    card_title = "MyCode"
    if (condition):
        times = intent['slots']['Times']['value']
        session_attributes['repeat'] = times
        speech_output = "OK! what do you want to repeat"
    else:
        speech_output = ""
    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def minusminus_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']
    condition = session_attributes['check_condition']

    card_title = "MyCode"
    if (condition):
        variable = intent['slots']['Variable']['value']
        original_value = session_attributes[variable]
        new_value = int(original_value) -1
        session_attributes[variable]=new_value
        speech_output = "Minus minus is done! "
    else:
        speech_output = ""
    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
def plusplus_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']
    condition = session_attributes['check_condition']

    card_title = "MyCode"
    if (condition):
        variable = intent['slots']['Variable']['value']
        original_value = session_attributes[variable]
        new_value = int(original_value) +1
        session_attributes[variable]=new_value
        speech_output = "Plus Plus is done! "
    else:
        speech_output = ""
    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

#is {Variable} equal to {Value}
def IsEqual_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']

    card_title = "MyCode"

    the_var = intent['slots']['Variable']['value']
    the_val = int(intent['slots']['Value']['value'])

    temp = int(session_attributes[the_var])

    if temp==the_val:
        new_condition = True
        speech_output = "True"
    else:
        new_condition = False
        speech_output = "False"

    update_program_states(session, new_condition)

    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


#IsLessThanIntent is {Variable} less than {Value}
def IsLessThan_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']

    card_title = "MyCode"

    the_var = intent['slots']['Variable']['value']
    the_val = int(intent['slots']['Value']['value'])

    temp = int(session_attributes[the_var])


    if temp<the_val:
        new_condition = True
        speech_output = "True"
    else:
        new_condition = False
        speech_output = "False"

    update_program_states(session, new_condition)

    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

#IsGreaterThanIntent is {Variable} less than {Value}
def IsGreaterThan_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']

    card_title = "MyCode"

    the_var = intent['slots']['Variable']['value']
    the_val = int(intent['slots']['Value']['value'])

    temp = int(session_attributes[the_var])


    if temp>the_val:
        new_condition = True
        speech_output = "True"
    else:
        new_condition = False
        speech_output = "False"

    update_program_states(session, new_condition)

    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


#IsEqualtwoIntent is {VariableFirst} equal to {VariableSecond}
def IsEqualtwo_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']

    card_title = "MyCode"

    thefirst_var = intent['slots']['VariableFirst']['value']
    thesecond_var = intent['slots']['VariableSecond']['value']

    thefirst_val = int(session_attributes[thefirst_var])
    thesecond_val = int(session_attributes[thesecond_var])


    if thefirst_val==thesecond_val:
        new_condition = True
        speech_output = "True"
    else:
        new_condition = False
        speech_output = "False"

    update_program_states(session, new_condition)

    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

#IsLessThantwoIntent is {VariableFirst} less than {VariableSecond}
def IsLessThantwo_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']

    card_title = "MyCode"

    thefirst_var = intent['slots']['VariableFirst']['value']
    thesecond_var = intent['slots']['VariableSecond']['value']

    thefirst_val = int(session_attributes[thefirst_var])
    thesecond_val = int(session_attributes[thesecond_var])


    if thefirst_val<thesecond_val:
        new_condition = True
        speech_output = "True"
    else:
        new_condition = False
        speech_output = "False"

    update_program_states(session, new_condition)
    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

#IsGreaterThantwoIntent is {VariableFirst} greater than {VariableSecond}
def IsGreaterThantwo_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']

    card_title = "MyCode"

    thefirst_var = intent['slots']['VariableFirst']['value']
    thesecond_var = intent['slots']['VariableSecond']['value']

    thefirst_val = int(session_attributes[thefirst_var])
    thesecond_val = int(session_attributes[thesecond_var])


    if thefirst_val>thesecond_val:
        new_condition = True
        speech_output = "True"
    else:
        new_condition = False
        speech_output = "False"

    update_program_states(session, new_condition)
    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def EndIf_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']

    card_title = "MyCode"
    session_attributes['check_condition'] = True
    session_attributes['store_condition'] = False
    speech_output = "If is done"

    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def Else_intent(intent, session):
    session_attributes = {}
    session_attributes=session['attributes']

    card_title = "MyCode"

    update_program_states(session, True)
    speech_output = ""
    reprompt_text = "Next statement please! "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    session_attributes = {}
    session_attributes = session['attributes']
    session_attributes['repeat'] = 1
    session_attributes['check_condition']=True
    session_attributes['store_condition']=False
    # Dispatch to your skill's launch
    return get_welcome_response(session_attributes)


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "AssignIntent":
        return assign_intent(intent, session)
    elif intent_name == "PrintIntent":
        return print_intent(intent, session)
    elif intent_name == "AddIntent":
        return add_intent(intent, session)
    elif intent_name == "AddtwoIntent":
        return addtwo_intent(intent, session)
    elif intent_name == "LoopIntent":
        return loop_intent(intent, session)
    elif intent_name == "RepeatIntent":
        return repeat_intent(intent, session)
    elif intent_name == "MinusminusIntent":
        return minusminus_intent(intent, session)
    elif intent_name == "PlusplusIntent":
        return plusplus_intent(intent, session)
    elif intent_name == "IsEqualIntent":
        return IsEqual_intent(intent, session)
    elif intent_name == "IsLessThanIntent":
        return IsLessThan_intent(intent, session)
    elif intent_name == "IsGreaterThanIntent":
        return IsGreaterThan_intent(intent, session)
    elif intent_name == "IsEqualtwoIntent":
        return IsEqualtwo_intent(intent, session)
    elif intent_name == "IsLessThantwoIntent":
        return IsLessThantwo_intent(intent, session)
    elif intent_name == "IsGreaterThantwoIntent":
        return IsGreaterThantwo_intent(intent, session)
    elif intent_name == "ElseIntent":
        return Else_intent(intent, session)
    elif intent_name == "ElseIfIntent":
        return ElseIf_intent(intent, session)
    elif intent_name == "EndIfIntent":
        return EndIf_intent(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main  handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
