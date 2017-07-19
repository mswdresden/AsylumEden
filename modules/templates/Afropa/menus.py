# -*- coding: utf-8 -*-

from gluon import *
from s3 import *
from s3layouts import *
try:
    from .layouts import *
except ImportError:
    pass
import s3menus as default



# Below is an example which you can base your own template's menus.py on
# - there are also other examples in the other templates folders

# =============================================================================
class S3MainMenu(default.S3MainMenu):
    """
        #Custom Application Main Menu:

        #The main menu consists of several sub-menus, each of which can
        #be customised separately as a method of this class. The overall
        #composition of the menu is defined in the menu() method, which can
        #be customised as well:

        #Function        Sub-Menu                Access to (standard)

        #menu_modules()  the modules menu        the Eden modules
        #menu_gis()      the GIS menu            GIS configurations
        #menu_admin()    the Admin menu          System/User Administration
        #menu_lang()     the Language menu       Selection of the GUI locale
        #menu_auth()     the User menu           Login, Logout, User Profile
        #menu_help()     the Help menu           Contact page, About page

        #The standard uses the MM layout class for main menu items - but you
        #can of course use a custom layout class which you define in layouts.py.

        #Additional sub-menus can simply be defined as additional functions in
        #this class, and then be included in the menu() method.

        #Each sub-menu function returns a list of menu items, only the menu()
        #function must return a layout class instance.
    """



    # -------------------------------------------------------------------------
    @classmethod
    def menu(cls):
        """ Compose Menu """

        main_menu = MM()(

            # Modules-menu, align-left
            cls.menu_modules(),

            # Service menus, align-right
            # Note: always define right-hand items in reverse order!

            cls.menu_help(right=True), # msw: altered (see below)
            cls.menu_auth(right=True),
            cls.menu_lang(right=True),
            cls.menu_admin(right=True),
            #cls.menu_gis(right=True), # msw: does not show up?! hmmm

            # msw's custom menus (tests)
            # you can define a menu function and call it here:
            #   - 'right=True' does NOT work for some reason
            #   - you must wirte cls. in front of your function
            #cls.menu_msw(right=True),
            #cls.menu_msw2(right=True),
        )
        return main_menu

    # -------------------------------------------------------------------------
    # you can override the main menu functions here
    #   - probably good idea: first copy the original code from s3menus.py - the edit
    #   - you need the @classmethod
    #   - you need the (cls, **attr)
    #   - MM: MainMenue; c=controller; f=function (more options explained in s3navigation.py)
    #   - IMPORTANT: you only see the menu-item if the controller and the function exist. in addition,
    #     it seems only to work for the system controllers (like org, default, ...)
    #     for the time beeing, msw uses the end of the org.py controller file for personal code
    @classmethod
    def menu_help(cls, **attr):
        """ Custom Modules Menu for help """
        menu_help = MM("Help", c="default", f="help", **attr)(
            MM("Contact us", f="contact"),
            MM("About", f="about"),
            MM(current.T("Ask MSW"), c="org", f="ask_msw"),
            MM("spiegel.de", c="org", f="spiegel"),
        )
        return menu_help

    # -------------------------------------------------------------------------
    @classmethod
    def menu_msw(cls, right=True):
        """ Custom Modules Menu msw """

        return [
            MM("SimpleMSW", link=False)(
                MM("msw1"),
                MM("msw2"),
            )
        ]

    # -------------------------------------------------------------------------
    @classmethod
    def menu_msw2(cls, **attr):
        """ Custom Modules Menu """

        return [
            MM("Helpi", link=False)(
                MM("Ask MSW", c="afropa", f="askmsw"),
                MM("BBB"),
                MM("Ask MSW2",c="org",f="ask_msw"),
                MM("CCC"),
                MM("DDD")
            )
        ]

    # -------------------------------------------------------------------------
    #@classmethod
    #def menu_modules(cls):
        #""" Custom Modules Menu """

        #return [
            #homepage(),
            #homepage("gis"),
            #homepage("pr")(
                #MM("Persons", f="person"),
                #MM("Groups", f="group")
            #),
            #MM("more", link=False)(
                #homepage("dvi"),
                #homepage("irs")
            #),
        #]






# =============================================================================
class S3OptionsMenu(default.S3OptionsMenu):
    """
        #Custom Controller Menus

        #The options menu (left-hand options menu) is individual for each
        #controller, so each controller has its own options menu function
        #in this class.

        #Each of these option menu functions can be customised separately,
        #by simply overriding (re-defining) the default function. The
        #options menu function must return an instance of the item layout.

        #The standard menu uses the M item layout class, but you can of
        #course also use any other layout class which you define in
        #layouts.py (can also be mixed).

        #Make sure additional helper functions in this class don't match
        #any current or future controller prefix (e.g. by using an
        #underscore prefix).
    """

    #def cr(self):
        #""" CR / Shelter Registry """

        #return M(c="cr")(
                    #M("Camp", f="shelter")(
                        #M("New", m="create"),
                        #M("List All"),
                        #M("Map", m="map"),
                        #M("Import", m="import"),
                    #)
                #)

    # -------------------------------------------------------------------------
    # msw

    # org as an example (just copied form modules/s3menue.py)
    @staticmethod
    def org():
        """ ORG / Organization Registry """

        settings = current.deployment_settings
        ADMIN = current.session.s3.system_roles.ADMIN
        SECTORS = "Clusters" if settings.get_ui_label_cluster() \
                             else "Sectors"
        stats = lambda i: settings.has_module("stats")

        return M(c="org")(
                    M("Organizations MSW", f="organisation")(
                        M("Create", m="create"),
                        M("Import", m="import"),
                        M("TestSpiegel", c="org",f="spiegel")
                    ),
                    M("Offices", f="office")(
                        M("Create", m="create"),
                        M("Map", m="map"),
                        M("Import", m="import")
                    ),
                    M("Facilities", f="facility")(
                        M("Create", m="create"),
                        M("Import", m="import"),
                    ),
                    M("Resources", f="resource", m="summary",
                      check=stats)(
                        M("Create", m="create"),
                        M("Import", m="import")
                    ),
                    M("Organization Types", f="organisation_type",
                      restrict=[ADMIN])(
                        M("Create", m="create"),
                    ),
                    M("Office Types", f="office_type",
                      restrict=[ADMIN])(
                        M("Create", m="create"),
                    ),
                    M("Facility Types", f="facility_type",
                      restrict=[ADMIN])(
                        M("Create", m="create"),
                    ),
                    M(SECTORS, f="sector", restrict=[ADMIN])(
                        M("Create", m="create"),
                    ),
                )
    # Afropa menue
    @staticmethod
    def afropa():
        """ Afropa Registry """

        return M(c="afropa")(
                    M("Clients", f="client")(
                        M("Create", m="create"),
                        M("Import", m="import"),
                        M("Report", m="report"),
                      ),
                    M("Checklists", f="checklist")(
                        M("Create", m="create"),
                        M("Import", m="import"),
                        M("Report", m="report"),
                    ),
                    M("Mobility", f="mobility")(
                        M("Create", m="create"),
                        M("Import", m="import"),
                        M("Report", m="report"),
                    ),
            )

    # Asylum menue
    @staticmethod
    def asylum():
        """ Asylum Registry """

        return M(c="asylum")(
                    M("Asylum Person", f="person")(
                        M("Create", m="create"),
                        M("Import", m="import"),
                        M("Report", m="report"),
                      ),
                    M("Asylum Thing", f="thing")(
                        M("Create", m="create"),
                        M("Import", m="import"),
                        M("Report", m="report"),
                    ),
        )


# END =========================================================================
