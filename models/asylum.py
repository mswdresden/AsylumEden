tablename = "asylum_person"
db.define_table(tablename,
    Field('first_name', label=T("First Name(s)"), requires=IS_NOT_EMPTY()),
    Field('last_name', label=T("Last Name"), requires=IS_NOT_EMPTY()),
    s3base.s3_date("date_of_birth",
        label = T("Date of Birth"),
        #empty = not settings.get_pr_dob_required(),
        future = 0,
        past = 1320),
    # This adds all the metadata to store
    # information on who created/updated
    # the record & when
    *s3_meta_fields()
)  # Months, so 110 years

# --------------------------
tablename = "asylum_thing"
db.define_table(tablename,
                Field('asylum_person_id', 'reference asylum_person'),
                Field('thing', label=T("Thing"),default="no thing"),
                Field('value', label=T("Value")),
                #Field('children', label=T('Children'), type=[string]),
)

db.asylum_thing.asylum_person_id.requires = IS_IN_DB(db, db.asylum_person.id)

abba999 = "ALL VARIABLES DEFINED IN MODELS IS ALSO THERE IN CONTROLLERS"


# --------------------------
#http://127.0.0.1:7000/book/default/chapter/29/12/components-and-plugins
db.define_table('comment_post',
   Field('body','text',label='Your comment'),
   auth.signature)


# --------------------------
# https://groups.google.com/forum/#!topic/web2py/MQNyLg-CsRM
db.define_table('friend',Field('name'))