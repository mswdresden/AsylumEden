tablename = "afropa_client"
db.define_table(tablename,
    # A 'name' field
    Field("name",length=128,label=T("Name"), requires=IS_NOT_EMPTY()),
    Field("firstname",label=T("First Name")),
    s3base.s3_date("date_of_birth",
        label = T("Date of Birth"),
        #empty = not settings.get_pr_dob_required(),
        future = 0,
        past = 1320),  # Months, so 110 years
    s3base.s3_date("date_of_arrival",
        label=T("Date of Arrival"),
        #empty = not settings.get_pr_dob_required(),
        future = 0,
        past = 1320),  # Months, so 110 years
    Field("legal_status", label=T("Legal Status")),
    Field("health_insurance", label=T("Health Insurance")),
    Field("bamf_reference", label=T("BAMF Reference")),
    Field("bank_account", label=T("Bank Account")),
    s3db.pr_person_id(label=T("Assisting Person")),
    s3db.super_link("site_id", "org_site",
                                label = T("Organisation"),
                                # superlink fields are normally invisible
                                readable = True,
                                writable = True,
                                # we want users to see the site name
                                # rather than just the ID
                                represent = s3db.org_site_represent,
                                ),
    # This adds all the metadata to store
    # information on who created/updated
    # the record & when
    *s3_meta_fields())

# set/update CRUD settings
s3.crud_strings[tablename] = Storage(
        label_create = T("Create Client basic info"),
        title_display = T("Client Details"),
        title_list = T("List Client"),
        title_update = T("Edit Client"),
        title_upload = T("Import Client"),
        subtitle_list = T("Clients"),
        label_list_button = T("List Clients"),
        label_delete_button = T("Delete Client"),
        msg_record_created = T("Client added"),
        msg_record_modified = T("Client updated"),
        msg_record_deleted = T("Client deleted"),
        msg_list_empty = T("No Client currently registered")
        )

# ---------------------------------
# table_checklist
tablename = "afropa_checklist"
db.define_table(tablename,
    # A 'name' field
    Field("housing_status",length=128,label=T("Housing OK"), requires=IS_NOT_EMPTY()),
    Field("dezi_housing", label=T("Dezi-Appartment")),
    Field("mailbox_labeled", type="boolean", label=T("Mailbox labeled")),
    Field("key_to_appartment", label=T("Key to Appartment")),
    Field("key_to_mailbox", label=T("Key to Mailbox")),
    Field("heating_ok", label=T("Heating OK")),
    Field("bamf_address", label=T("BAMF Address")),
    Field("waste_separation", label=T("Waste Separation")),
    # This adds all the metadata to store
    # information on who created/updated
    # the record & when
    *s3_meta_fields())

# set/update CRUD settings
s3.crud_strings[tablename] = Storage(
        label_create = T("Create Checklist"),
        title_display = T("Checklist Details"),
        title_list = T("List Checklist"),
        title_update = T("Edit Checklist"),
        title_upload = T("Import Checklist"),
        subtitle_list = T("Checklist"),
        label_list_button = T("List Checklist"),
        label_delete_button = T("Delete Checklist"),
        msg_record_created = T("Checklist added"),
        msg_record_modified = T("Checklist updated"),
        msg_record_deleted = T("Checklist deleted"),
        msg_list_empty = T("No Checklist currently registered")
        )

# ---------------------------------
# table_checklist
tablename = "afropa_mobility"
db.define_table(tablename,
    # A 'name' field
    Field("public_transport",length=128,label=T("Public Transport")),
    Field("dresden_pass" ,label=T("Dresden Pass")),
    Field("monthly_ticket", label=T("Monthly Ticket")),
    # This adds all the metadata to store
    # information on who created/updated
    # the record & when
    *s3_meta_fields())


# set/update CRUD settings
s3.crud_strings[tablename] = Storage(
        label_create = T("Create Mobility"),
        title_display = T("Mobility Details"),
        title_list = T("List Mobility"),
        title_update = T("Edit Mobility"),
        title_upload = T("Import Mobility"),
        subtitle_list = T("Mobility"),
        label_list_button = T("List Mobility"),
        label_delete_button = T("Delete Mobility"),
        msg_record_created = T("Mobility added"),
        msg_record_modified = T("(Mobility updated"),
        msg_record_deleted = T("Mobility deleted"),
        msg_list_empty = T("No Mobility currently registered")
        )
