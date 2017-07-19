# -*- coding: utf-8 -*-

"""
    Guided Tour, Controllers
"""
module = request.controller
resourcename = request.function

if not settings.has_module(module):
    raise HTTP(404, body="Module disabled: %s" % module)

# ------------------------------------------
def index():
    #import datetime
    datetimenow = datetime.datetime.utcnow()
    date        = datetime.datetime.now()

    response.flash = T(str(abba999))

    return locals()

# ------------------------------------------
def person():
    return s3_rest_controller()

    ## return the person
    #persons = db().select(db.asylum_person.ALL, orderby=db.asylum_person.first_name)
    #return dict(persons=persons)

    #db.t_dog_dog.f_dog_owner_id.default = 2
    #form =  SQLFORM(db.asylum_person)
    #return dict(form=form)

# ------------------------------------------
def show():
    person = db.asylum_person(request.args(0, cast=int)) or redirect(URL('index'))
    #db.asylum_person.asylum_person_id.default = person.id
    form = SQLFORM(db.asylum_person)
    if form.process().accepted:
        response.flash = 'your asylum person is posted (or what)'
    return dict(person=person, form=form)

# ------------------------------------------
def manage():
    #grid = SQLFORM.smartgrid(db.asylum_person, linked_tables=['post'])
    grid = SQLFORM.smartgrid(db.asylum_person, linked_tables=[None])
    return dict(grid=grid)

# ------------------------------------------
def thing():
    return s3_rest_controller()

# ------------------------------------------
def thing2():
    #return s3_rest_controller()
    response.flash = "Ich bin thing2"
    return dict()

# ------------------------------------------
def testwithargs(a=9):
    response.flash = 'this should never be seen, as this function has an argument'

# ------------------------------------------
def __testwithunderscore():
    response.flash = 'this should never be seen, as this function starts with two underscores'

# ------------------------------------------
def tester():
    path_info   = request.env.path_info
    request_cid = request.cid

    response.title="hallo du kleies schaf"   # overrides the title in the browser
    response.subtitle = "... geh schlafen!!" # has no effect on my chromium
    response.write("response.write(text): a method to write text into the output page body.")

    localstring=str("hallo, ich bin ein string")
    return locals()

# ------------------------------------------
def manualrows():
    #table = db.asylum_thing
    rows = db().select(db.asylum_thing.ALL)
    #print rows
    return dict(rows=rows)
# ------------------------------------------
def export_test():
    db.export_to_csv_file(open('somefile.csv', 'wb'))
    response.flash = "exported somefile.csv"
    return dict()


# ------------------------------------------
if __name__ == '__main__':
    def import_test():
        db.import_from_csv_file(open('somefile.csv', 'rb'))
        return dict()


# chapter 7 forms and stuff ..

# ------------------------------------------
def input_form():
    #form = FORM('your name', INPUT(_name='name', requires=IS_NOT_EMPTY()),
    #INPUT(_type='submit'))
    #form.add_button('go to spiegel', 'http://www.spiegel.de')


    form = SQLFORM(db.asylum_person,col3 = {'name':A('what is this?',
      _href='http://www.google.com/search?q=define:name')},comments=True)

    #if form.accepts(request, session):
    if form.process().accepted:
        response.flash = "cool"
    elif form.errors:
        response.flash = "form has errors"
    else:
        response.flash = "please give an input"

    vars = request.vars
    args = request.args
    print "\n -------"
    print "vars: ", vars
    print "args: ", args


    return dict(form=form)

# ------------------------------------------
@auth.requires_login()
def post():

    print "the request.cid is: ", request.cid
    return dict(form=SQLFORM(db.comment_post).process(),
                comments=db(db.comment_post).select())

# ------------------------------------------
def form_communication():
    form = SQLFORM.factory(
                           Field('name',requires=IS_NOT_EMPTY()),
                           Field('phone'),
                           )


    if form.process().accepted:
        response.flash = "Your name:", form.vars.name
        response.flash = "Your phone:", form.vars.phone

    return dict(form=form)

# ------------------------------------------
def form_manip():
    form = SQLFORM(db.asylum_thing,
                   #record=asylum_thing_index,
                   deletable=True,
                   submit_button=T('Update'))

    form[0][-1][1].append(TAG.BUTTON('Cancel', _onclick="document.location='%s';"%URL('index')))
    form.element('input[type=submit]')['_onclick'] = "return confirm('Are you sure?');"

    if form.process().accepted:
        response.flash = 'form ok'
    else:
        response.flash = 'there is an error'

    return dict(form=form)

# ------------------------------------------
def catch_info():
    #try:
    #    t
    #except:
    #    response.flash = "mist"
    #else:
    #    response.flash = str("cool, t is:", t)

    return "alert('hello')"


# ------------------------------------------
def show_friend():
    form = SQLFORM(db.friend)
    friends = db(db.friend).select()
    return dict(form=form,friends=friends)

# ------------------------------------------
def delete_friend(): # executes callback
    # should check permissions but ok for now...
    del db.friend[request.port_vars.id]
    return 'done'