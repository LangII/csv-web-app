# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainItem(models.Model):
    text = models.CharField(max_length=300)
    complete = models.IntegerField()
    to_do_list = models.ForeignKey('MainTodolist', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_item'


class MainTodolist(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'main_todolist'


class tblCompany(models.Model):
    companyid = models.AutoField(db_column='CompanyID', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=50)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=50)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=50)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=5)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10)  # Field name made lowercase.
    salespersonid = models.PositiveIntegerField(db_column='SalesPersonID')  # Field name made lowercase.
    imageloc = models.CharField(db_column='ImageLoc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    responseemail = models.CharField(db_column='ResponseEmail', max_length=1, blank=True, null=True)  # Field name made lowercase.
    responsepost = models.CharField(db_column='ResponsePost', max_length=1, blank=True, null=True)  # Field name made lowercase.
    responseemailcompany = models.CharField(db_column='ResponseEmailCompany', max_length=1, blank=True, null=True)  # Field name made lowercase.
    poststring = models.CharField(db_column='PostString', max_length=255)  # Field name made lowercase.
    reorderwarning = models.CharField(db_column='ReOrderWarning', max_length=1, blank=True, null=True)  # Field name made lowercase.
    packingimageloc = models.CharField(db_column='PackingImageLoc', max_length=50)  # Field name made lowercase.
    userdef1 = models.CharField(max_length=255, blank=True, null=True)
    userdef2 = models.CharField(max_length=255, blank=True, null=True)
    userdef3 = models.CharField(max_length=255, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    macola = models.CharField(max_length=12, blank=True, null=True)
    nextreviewdate = models.DateTimeField(db_column='NextReviewDate', blank=True, null=True)  # Field name made lowercase.
    classification = models.CharField(db_column='Classification', max_length=3, blank=True, null=True)  # Field name made lowercase.
    distro = models.CharField(max_length=1, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    firstshipdate = models.DateTimeField(db_column='FirstShipDate', blank=True, null=True)  # Field name made lowercase.
    m2mid = models.CharField(max_length=12, blank=True, null=True)
    clickbank = models.CharField(db_column='Clickbank', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clickbankkey = models.CharField(db_column='ClickbankKEY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    domconsolidator = models.CharField(db_column='DomConsolidator', max_length=1, blank=True, null=True)  # Field name made lowercase.
    intlconsolidator = models.CharField(db_column='IntlConsolidator', max_length=1, blank=True, null=True)  # Field name made lowercase.
    surepost = models.CharField(db_column='SurePost', max_length=1)  # Field name made lowercase.
    nosingleitem = models.CharField(db_column='NoSingleItem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    priorityship = models.CharField(db_column='PriorityShip', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clickbankkey2 = models.CharField(db_column='ClickbankKEY2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    returngroup = models.IntegerField(db_column='ReturnGroup')  # Field name made lowercase.
    volusion = models.CharField(db_column='Volusion', max_length=1, blank=True, null=True)  # Field name made lowercase.
    volusionlogin = models.CharField(db_column='VolusionLogin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    volusionpwd = models.CharField(db_column='VolusionPWD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contactemail = models.CharField(db_column='ContactEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    volusionurl = models.CharField(db_column='VolusionURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    infusion = models.CharField(db_column='Infusion', max_length=1, blank=True, null=True)  # Field name made lowercase.
    accesstoken = models.CharField(db_column='AccessToken', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refreshtoken = models.CharField(db_column='RefreshToken', max_length=100, blank=True, null=True)  # Field name made lowercase.
    inactivedate = models.DateTimeField(db_column='InactiveDate', blank=True, null=True)  # Field name made lowercase.
    clickbankkey3 = models.CharField(db_column='ClickbankKEY3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    oauth = models.CharField(db_column='Oauth', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clickbankkey4 = models.CharField(db_column='ClickbankKEY4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    clickbankkey5 = models.CharField(db_column='ClickbankKEY5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    xmlpost = models.CharField(db_column='XmlPost', max_length=1, blank=True, null=True)  # Field name made lowercase.
    httppost = models.CharField(db_column='HTTPPost', max_length=1, blank=True, null=True)  # Field name made lowercase.
    number_1shoppingcart = models.CharField(db_column='1shoppingcart', max_length=1, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    shopify = models.CharField(db_column='Shopify', max_length=1, blank=True, null=True)  # Field name made lowercase.
    limelight = models.CharField(db_column='Limelight', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ultracart = models.CharField(db_column='UltraCart', max_length=1, blank=True, null=True)  # Field name made lowercase.
    paypal = models.CharField(db_column='PayPal', max_length=1, blank=True, null=True)  # Field name made lowercase.
    infusionsoft = models.CharField(db_column='InfusionSoft', max_length=1, blank=True, null=True)  # Field name made lowercase.
    woocommerce = models.CharField(db_column='WooCommerce', max_length=1, blank=True, null=True)  # Field name made lowercase.
    shipstation = models.CharField(db_column='ShipStation', max_length=1, blank=True, null=True)  # Field name made lowercase.
    stripe = models.CharField(db_column='Stripe', max_length=1, blank=True, null=True)  # Field name made lowercase.
    jet = models.CharField(db_column='Jet', max_length=1, blank=True, null=True)  # Field name made lowercase.
    flickrocket = models.CharField(db_column='FlickRocket', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ecwid = models.CharField(db_column='Ecwid', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ontraport = models.CharField(db_column='Ontraport', max_length=1, blank=True, null=True)  # Field name made lowercase.
    thrivecart = models.CharField(db_column='ThriveCart', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clickfunnel = models.CharField(db_column='ClickFunnel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clickbankcart = models.CharField(db_column='ClickBankCart', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ejunkie = models.CharField(db_column='EJunkie', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mailchimp = models.CharField(db_column='MailChimp', max_length=1, blank=True, null=True)  # Field name made lowercase.
    generalcontactemail = models.CharField(db_column='GeneralContactEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    itcontactemail = models.CharField(db_column='ITContactEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    clickbankkey6 = models.CharField(db_column='ClickbankKEY6', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCompany'


class tblPackageShipments(models.Model):
    packageshipmentid = models.AutoField(db_column='PackageShipmentID', primary_key=True)  # Field name made lowercase.
    companyid = models.PositiveIntegerField(db_column='CompanyID')  # Field name made lowercase.
    requesteddatetime = models.DateTimeField(db_column='RequestedDateTime')  # Field name made lowercase.
    requesteduserfullname = models.CharField(db_column='RequestedUserFullName', max_length=41)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=50)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=41)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=70, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=70, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=35, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=25, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=60, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=35, blank=True, null=True)  # Field name made lowercase.
    faxnumber = models.CharField(db_column='FaxNumber', max_length=25)  # Field name made lowercase.
    shippingmethod = models.CharField(db_column='ShippingMethod', max_length=50)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    freightcost = models.FloatField(db_column='FreightCost')  # Field name made lowercase.
    trackingnumber = models.CharField(db_column='TrackingNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=13, blank=True, null=True)  # Field name made lowercase.
    shippingnumber = models.CharField(db_column='ShippingNumber', max_length=128, blank=True, null=True)  # Field name made lowercase.
    shippingnotes = models.CharField(db_column='ShippingNotes', max_length=256, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fulfillmentcost = models.FloatField(db_column='FulfillmentCost')  # Field name made lowercase.
    billtocompanyname = models.CharField(db_column='BillToCompanyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billtoattention = models.CharField(db_column='BillToAttention', max_length=41, blank=True, null=True)  # Field name made lowercase.
    billtoaddress1 = models.CharField(db_column='BillToAddress1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billtoaddress2 = models.CharField(db_column='BillToAddress2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    billtocity = models.CharField(db_column='BillToCity', max_length=30, blank=True, null=True)  # Field name made lowercase.
    billtostate = models.CharField(db_column='BillToState', max_length=5, blank=True, null=True)  # Field name made lowercase.
    billtozipcode = models.CharField(db_column='BillToZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    billtocountry = models.CharField(db_column='BillToCountry', max_length=25, blank=True, null=True)  # Field name made lowercase.
    billtophonenumber = models.CharField(db_column='BillToPhoneNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    billtofaxnumber = models.CharField(db_column='BillToFaxNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    billtonotes = models.CharField(db_column='BillToNotes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billtoemail = models.CharField(db_column='BillToEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userdefval1 = models.TextField(blank=True, null=True)
    userdefval2 = models.TextField(blank=True, null=True)
    userdefval3 = models.TextField(blank=True, null=True)
    residential = models.CharField(db_column='Residential', max_length=1, blank=True, null=True)  # Field name made lowercase.
    completiondate = models.DateTimeField(db_column='CompletionDate', blank=True, null=True)  # Field name made lowercase.
    shippeddate = models.DateTimeField(db_column='ShippedDate', blank=True, null=True)  # Field name made lowercase.
    shippingaccount = models.CharField(db_column='ShippingAccount', max_length=75, blank=True, null=True)  # Field name made lowercase.
    postage = models.FloatField(db_column='Postage', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    declaredvalue = models.CharField(db_column='DeclaredValue', max_length=8, blank=True, null=True)  # Field name made lowercase.
    shippingcost = models.FloatField(db_column='ShippingCost', blank=True, null=True)  # Field name made lowercase.
    publishedrate = models.FloatField(db_column='PublishedRate', blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=70, blank=True, null=True)  # Field name made lowercase.
    nocharge = models.CharField(db_column='NoCharge', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nochargereqby = models.CharField(db_column='NoChargeReqBy', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nochargedesc = models.CharField(db_column='NoChargeDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    distro = models.SmallIntegerField(db_column='Distro', blank=True, null=True)  # Field name made lowercase.
    shippedmethod = models.CharField(db_column='ShippedMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    zone = models.CharField(db_column='Zone', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dimensions = models.CharField(db_column='Dimensions', max_length=20, blank=True, null=True)  # Field name made lowercase.
    multiboxshipment = models.SmallIntegerField(db_column='MultiBoxShipment', blank=True, null=True)  # Field name made lowercase.
    nocombine = models.IntegerField(db_column='NoCombine', blank=True, null=True)  # Field name made lowercase.
    numpicklocs = models.IntegerField(db_column='NumPickLocs', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    costpicks = models.FloatField(db_column='CostPicks', blank=True, null=True)  # Field name made lowercase.
    costpkg = models.FloatField(db_column='CostPkg', blank=True, null=True)  # Field name made lowercase.
    readytoship = models.DateTimeField(db_column='ReadyToShip', blank=True, null=True)  # Field name made lowercase.
    delivereddate = models.DateTimeField(db_column='DeliveredDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPackageShipments'


class tblPackageShipmentLines(models.Model):
    packageshipmentlineid = models.AutoField(db_column='PackageShipmentLineID', primary_key=True)  # Field name made lowercase.
    packageshipmentid = models.PositiveIntegerField(db_column='PackageShipmentID')  # Field name made lowercase.
    packageid = models.PositiveIntegerField(db_column='PackageID')  # Field name made lowercase.
    quantity = models.PositiveIntegerField(db_column='Quantity')  # Field name made lowercase.
    quantityshipped = models.PositiveIntegerField(db_column='QuantityShipped')  # Field name made lowercase.
    lotinfo = models.CharField(db_column='LotInfo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    lot = models.CharField(db_column='LOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userdefval1 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblPackageShipmentLines'


class tblPackages(models.Model):
    packageid = models.AutoField(db_column='PackageID', primary_key=True)  # Field name made lowercase.
    companyid = models.PositiveIntegerField(db_column='CompanyID')  # Field name made lowercase.
    partnumber = models.CharField(db_column='PartNumber', max_length=40, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=90, blank=True, null=True)  # Field name made lowercase.
    detaileddescription = models.CharField(db_column='DetailedDescription', max_length=100)  # Field name made lowercase.
    onhand = models.IntegerField(db_column='OnHand')  # Field name made lowercase.
    allocated = models.IntegerField(db_column='Allocated')  # Field name made lowercase.
    available = models.IntegerField(db_column='Available')  # Field name made lowercase.
    onorder = models.IntegerField(db_column='OnOrder')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=50)  # Field name made lowercase.
    reorderthreshold = models.PositiveIntegerField(db_column='ReorderThreshold')  # Field name made lowercase.
    reorderamount = models.PositiveIntegerField(db_column='ReorderAmount')  # Field name made lowercase.
    leadtime = models.PositiveIntegerField(db_column='LeadTime')  # Field name made lowercase.
    averagecost = models.FloatField(db_column='AverageCost')  # Field name made lowercase.
    status = models.CharField(max_length=9, blank=True, null=True)
    customfield01 = models.CharField(db_column='CustomField01', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reorderwarningamt = models.IntegerField(db_column='ReOrderWarningAmt')  # Field name made lowercase.
    reorderwarningemail = models.CharField(db_column='ReOrderWarningEmail', max_length=1)  # Field name made lowercase.
    pvalue = models.FloatField(db_column='PVALUE', blank=True, null=True)  # Field name made lowercase.
    bin = models.CharField(max_length=50, blank=True, null=True)
    declaredvalue = models.CharField(db_column='DeclaredValue', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allocatedtoship = models.IntegerField(db_column='AllocatedToShip', blank=True, null=True)  # Field name made lowercase.
    harmonizedcode = models.CharField(db_column='HarmonizedCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customsdescription = models.CharField(db_column='CustomsDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
    countryoforigin = models.CharField(db_column='CountryOfOrigin', max_length=2, blank=True, null=True)  # Field name made lowercase.
    orderseq = models.PositiveIntegerField(db_column='OrderSeq', blank=True, null=True)  # Field name made lowercase.
    replaceval = models.FloatField(db_column='ReplaceVal', blank=True, null=True)  # Field name made lowercase.
    lastonhand = models.IntegerField(db_column='LastOnHand', blank=True, null=True)  # Field name made lowercase.
    priorlastonhand = models.IntegerField(db_column='PriorLastOnHand', blank=True, null=True)  # Field name made lowercase.
    altbin = models.CharField(max_length=50, blank=True, null=True)
    oldpno = models.CharField(db_column='oldPno', max_length=25, blank=True, null=True)  # Field name made lowercase.
    serialnumreq = models.CharField(db_column='SerialNumReq', max_length=1, blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    dem = models.SmallIntegerField(db_column='Dem', blank=True, null=True)  # Field name made lowercase.
    sortnumber = models.IntegerField(db_column='SortNumber')  # Field name made lowercase.
    alternatepartname = models.CharField(db_column='AlternatePartName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lotinfo = models.CharField(db_column='LotInfo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    lot = models.CharField(db_column='LOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    listonpackingslip = models.PositiveSmallIntegerField(db_column='ListOnPackingSlip')  # Field name made lowercase.
    lastonhandweekly = models.IntegerField(db_column='LastOnHandWeekly', blank=True, null=True)  # Field name made lowercase.
    cyclecountthreshold = models.IntegerField(db_column='cycleCountThreshold', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPackages'


# class Tblcountries(models.Model):
#     id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=60)  # Field name made lowercase.
#     code = models.CharField(db_column='Code', max_length=2)  # Field name made lowercase.
#     cs_symbol = models.CharField(db_column='CS_Symbol', max_length=60, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'tblCountries'


# class Tblfreightfin(models.Model):
#     packageshipmentid = models.PositiveIntegerField(db_column='PackageShipmentID')  # Field name made lowercase.
#     companyid = models.PositiveIntegerField(db_column='CompanyID')  # Field name made lowercase.
#     shippedmethod = models.CharField(db_column='ShippedMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
#     dimensions = models.CharField(db_column='Dimensions', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     zone = models.CharField(db_column='Zone', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     zipcode = models.CharField(db_column='ZipCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=60, blank=True, null=True)  # Field name made lowercase.
#     truecost = models.FloatField(db_column='TrueCost', blank=True, null=True)  # Field name made lowercase.
#     cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
#     published = models.FloatField(db_column='Published', blank=True, null=True)  # Field name made lowercase.
#     billed = models.FloatField(db_column='Billed', blank=True, null=True)  # Field name made lowercase.
#     shippeddate = models.DateTimeField(db_column='ShippedDate', blank=True, null=True)  # Field name made lowercase.
#     tblfreightfinid = models.AutoField(db_column='tblFreightFinID', primary_key=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'tblFreightFin'


# class Tbllivescripts(models.Model):
#     livescriptid = models.AutoField(db_column='LiveScriptID', primary_key=True)  # Field name made lowercase.
#     starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
#     endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
#     running = models.CharField(db_column='Running', max_length=1)  # Field name made lowercase.
#     scriptname = models.CharField(db_column='ScriptName', unique=True, max_length=45)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'tblLiveScripts'


# class Tblpackagesbs(models.Model):
#     packageid = models.AutoField(db_column='PackageID', primary_key=True)  # Field name made lowercase.
#     companyid = models.PositiveIntegerField(db_column='CompanyID')  # Field name made lowercase.
#     partnumber = models.CharField(db_column='PartNumber', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     title = models.CharField(db_column='Title', max_length=90, blank=True, null=True)  # Field name made lowercase.
#     detaileddescription = models.CharField(db_column='DetailedDescription', max_length=100)  # Field name made lowercase.
#     onhand = models.IntegerField(db_column='OnHand')  # Field name made lowercase.
#     allocated = models.IntegerField(db_column='Allocated')  # Field name made lowercase.
#     available = models.IntegerField(db_column='Available')  # Field name made lowercase.
#     onorder = models.IntegerField(db_column='OnOrder')  # Field name made lowercase.
#     category = models.CharField(db_column='Category', max_length=50)  # Field name made lowercase.
#     reorderthreshold = models.PositiveIntegerField(db_column='ReorderThreshold')  # Field name made lowercase.
#     reorderamount = models.PositiveIntegerField(db_column='ReorderAmount')  # Field name made lowercase.
#     leadtime = models.PositiveIntegerField(db_column='LeadTime')  # Field name made lowercase.
#     averagecost = models.FloatField(db_column='AverageCost')  # Field name made lowercase.
#     status = models.CharField(max_length=9, blank=True, null=True)
#     customfield01 = models.CharField(db_column='CustomField01', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     reorderwarningamt = models.IntegerField(db_column='ReOrderWarningAmt')  # Field name made lowercase.
#     reorderwarningemail = models.CharField(db_column='ReOrderWarningEmail', max_length=1)  # Field name made lowercase.
#     pvalue = models.FloatField(db_column='PVALUE', blank=True, null=True)  # Field name made lowercase.
#     bin = models.CharField(max_length=50, blank=True, null=True)
#     declaredvalue = models.CharField(db_column='DeclaredValue', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     allocatedtoship = models.IntegerField(db_column='AllocatedToShip', blank=True, null=True)  # Field name made lowercase.
#     harmonizedcode = models.CharField(db_column='HarmonizedCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     customsdescription = models.CharField(db_column='CustomsDescription', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     countryoforigin = models.CharField(db_column='CountryOfOrigin', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     orderseq = models.PositiveIntegerField(db_column='OrderSeq', blank=True, null=True)  # Field name made lowercase.
#     replaceval = models.FloatField(db_column='ReplaceVal', blank=True, null=True)  # Field name made lowercase.
#     lastonhand = models.IntegerField(db_column='LastOnHand', blank=True, null=True)  # Field name made lowercase.
#     priorlastonhand = models.IntegerField(db_column='PriorLastOnHand', blank=True, null=True)  # Field name made lowercase.
#     altbin = models.CharField(max_length=50, blank=True, null=True)
#     oldpno = models.CharField(db_column='oldPno', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     serialnumreq = models.CharField(db_column='SerialNumReq', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
#     dem = models.SmallIntegerField(db_column='Dem', blank=True, null=True)  # Field name made lowercase.
#     sortnumber = models.IntegerField(db_column='SortNumber')  # Field name made lowercase.
#     alternatepartname = models.CharField(db_column='AlternatePartName', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     lotinfo = models.CharField(db_column='LotInfo', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     lot = models.CharField(db_column='LOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     listonpackingslip = models.PositiveSmallIntegerField(db_column='ListOnPackingSlip')  # Field name made lowercase.
#     lastonhandweekly = models.IntegerField(db_column='LastOnHandWeekly', blank=True, null=True)  # Field name made lowercase.
#     cyclecountthreshold = models.IntegerField(db_column='cycleCountThreshold', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'tblPackagesBS'


# class Tblreadytoshipdates(models.Model):
#     id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     packageshipmentid = models.IntegerField(db_column='PackageShipmentID')  # Field name made lowercase.
#     readytoship = models.DateTimeField(db_column='ReadyToShip', blank=True, null=True)  # Field name made lowercase.
#     reason = models.CharField(db_column='Reason', max_length=19, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'tblReadyToShipDates'


# class Tblshippingmethods(models.Model):
#     shippingmethodid = models.AutoField(db_column='ShippingMethodID', primary_key=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
#     display = models.CharField(db_column='Display', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     cs_symbol = models.CharField(db_column='CS_Symbol', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     delcon = models.CharField(db_column='DelCon', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     sigreq = models.CharField(db_column='SigReq', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     packagetype = models.CharField(db_column='PackageType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     level0 = models.DecimalField(db_column='Level0', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     level1 = models.DecimalField(db_column='Level1', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     level2 = models.DecimalField(db_column='Level2', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     level3 = models.DecimalField(db_column='Level3', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     handlingcharge = models.FloatField(db_column='HandlingCharge', blank=True, null=True)  # Field name made lowercase.
#     carriergroup = models.IntegerField(db_column='CarrierGroup', blank=True, null=True)  # Field name made lowercase.
#     prioritycarrier = models.CharField(db_column='PriorityCarrier', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     non_machinable = models.CharField(db_column='Non_Machinable', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     flats = models.CharField(db_column='Flats', max_length=5, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'tblShippingMethods'


# class Tblspecialshipdis(models.Model):
#     shippingmethodid = models.SmallIntegerField(db_column='ShippingMethodID')  # Field name made lowercase.
#     discount = models.FloatField(db_column='Discount')  # Field name made lowercase.
#     distype = models.CharField(db_column='DisType', max_length=16)  # Field name made lowercase.
#     handlingfee = models.FloatField(db_column='HandlingFee')  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='CompanyID')  # Field name made lowercase.
#     specialshipdisid = models.AutoField(db_column='SpecialShipDisID', primary_key=True)  # Field name made lowercase.
#     startweight = models.FloatField(db_column='StartWeight', blank=True, null=True)  # Field name made lowercase.
#     stopweight = models.FloatField(db_column='StopWeight', blank=True, null=True)  # Field name made lowercase.
#     fromservice = models.SmallIntegerField(db_column='FromService', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'tblSpecialShipDis'


# class Tblthirdpartyshipping(models.Model):
#     companyid = models.IntegerField(db_column='CompanyID', blank=True, null=True)  # Field name made lowercase.
#     carrier = models.CharField(db_column='Carrier', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     accountnumber = models.CharField(db_column='AccountNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     companyname = models.CharField(db_column='CompanyName', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     b2baccount = models.CharField(db_column='B2BAccount', max_length=1, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'tblThirdPartyShipping'


# class Tblupc(models.Model):
#     id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     upcnumber = models.CharField(db_column='UPCNumber', unique=True, max_length=50)  # Field name made lowercase.
#     packageid = models.IntegerField(db_column='PackageID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'tblUPC'
