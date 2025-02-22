from django.urls import path

from apps.views import ProductListTemplateView, ProductListDetailView, ProductListView, OrderDetailView, OrderListView, \
    CustomerView, CustomerDetailView, ShoppingCartView, CheckOutView, BillingView, InvoiceView, CrmTemplateView, \
    CalendarView, AnalyticsView, ManagementView, ECommerceView, SaasView, ChatView, InboxView, EmailDetailView, \
    ComposeView, CreateEventView, EventDetailView, EventListView, KanbanView, StarterView, LandingView, LoginView, \
    LogoutView, RegisterView, ForgotPasswordView, ConfirmMailView, ResetPasswordView, LockScreenView, WizardView, \
    ProfileView, SettingsUserView, PricingAltView, PricingDefaultView, FaqBasicView, FaqAltView, FaqAccordionView, \
    Error404View, Error500View, AssociationsView, InvitePeopleView, PrivacyPolicyView, FormControlView, InputGroupView, \
    SelectView, CheckView, RangeView, LayoutView, AdvanceSelectView, DatePickerView, EditorAdvanceView, EmojiButtonView, \
    FileUploaderView, RatingView, FloatingLabelView, WizardFormView, ValidationFormView, BasicTableView, \
    AdvanceTableView, BulkSelectView, ChartjsView, LineChartsView, BarChartsView, CandlestickView, GeoMapView, \
    ScatterView, PieChartView, RadarChartView, HeatMapView, HowToUseView, SocialsFeedView, ActivityLogView, \
    NotificationsView, FollowerView, FontAwesomeView, BootStrapIconView, FeatherIconView, MaterialIconView, \
    GoogleMapView, LeafletMapView, WidgetView, ChangelogView, DesignFileView, GulpView, GettingStartView, \
    ConfigurationView, StylingView, DarkModeView, PluginView

urlpatterns = [
    path('', ProductListTemplateView.as_view(), name='product-grid'),
    path('product-detail', ProductListDetailView.as_view(), name='product_detail'),
    path('product-list', ProductListView.as_view(), name='product-list'),
    path('order-detail', OrderDetailView.as_view(), name='order-detail'),
    path('order-list', OrderListView.as_view(), name='order-list'),
    path('customers', CustomerView.as_view(), name='customers'),
    path('customer-detail', CustomerDetailView.as_view(), name='customer-detail'),
    path('shopping-cart', ShoppingCartView.as_view(), name='shopping-cart'),
    path('checkout', CheckOutView.as_view(), name='checkout'),
    path('billing', BillingView.as_view(), name='billing'),
    path('invoice', InvoiceView.as_view(), name='invoice'),
    path('crm', CrmTemplateView.as_view(), name='crm'),
    path('calendar', CalendarView.as_view(), name='calendar'),
    path('analytics', AnalyticsView.as_view(), name='analytics'),
    path('ecommerce', ECommerceView.as_view(), name='ecommerce'),
    path('management', ManagementView.as_view(), name='management'),
    path('saas', SaasView.as_view(), name='saas'),
    path('chat', ChatView.as_view(), name='chat'),
    path('inbox', InboxView.as_view(), name='inbox'),
    path('email-detail', EmailDetailView.as_view(), name='email-detail'),
    path('compose', ComposeView.as_view(), name='compose'),
    path('create-an-event', CreateEventView.as_view(), name='create-an-event'),
    path('event-detail', EventDetailView.as_view(), name='event-detail'),
    path('event-list', EventListView.as_view(), name='event-list'),
    path('kanban', KanbanView.as_view(), name='kanban'),
    path('starter', StarterView.as_view(), name='starter'),
    path('landing', LandingView.as_view(), name='landing'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forgot-password', ForgotPasswordView.as_view(), name='forgot-password'),
    path('confirm-mail', ConfirmMailView.as_view(), name='confirm-mail'),
    path('reset-password', ResetPasswordView.as_view(), name='reset-password'),
    path('lock-screen', LockScreenView.as_view(), name='lock-screen'),
    path('wizard', WizardView.as_view(), name='wizard'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('settings', SettingsUserView.as_view(), name='settings'),
    path('pricing', PricingAltView.as_view(), name='pricing'),
    path('pricing-default', PricingDefaultView.as_view(), name='pricing-default'),
    path('faq-basic', FaqBasicView.as_view(), name='faq-basic'),
    path('faq-alt', FaqAltView.as_view(), name='faq-alt'),
    path('faq-accordion', FaqAccordionView.as_view(), name='faq-accordion'),
    path('error404', Error404View.as_view(), name='error404'),
    path('error500', Error500View.as_view(), name='error500'),
    path('associations', AssociationsView.as_view(), name='associations'),
    path('invite-people', InvitePeopleView.as_view(), name='invite-people'),
    path('privacy-policy', PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('form-control', FormControlView.as_view(), name='form-control'),
    path('input-group', InputGroupView.as_view(), name='input-group'),
    path('select', SelectView.as_view(), name='select'),
    path('check', CheckView.as_view(), name='check'),
    path('range', RangeView.as_view(), name='range'),
    path('layout', LayoutView.as_view(), name='layout'),
    path('advance-select', AdvanceSelectView.as_view(), name='advance-select'),
    path('date-picker', DatePickerView.as_view(), name='date-picker'),
    path('advance-editor', EditorAdvanceView.as_view(), name='advance-editor'),
    path('emoji-button', EmojiButtonView.as_view(), name='emoji-button'),
    path('file-uploader', FileUploaderView.as_view(), name='file-uploader'),
    path('rating', RatingView.as_view(), name='rating'),
    path('floating-label', FloatingLabelView.as_view(), name='floating-label'),
    path('wizard-form', WizardFormView.as_view(), name='wizard-form'),
    path('validation-form', ValidationFormView.as_view(), name='validation-form'),
    path('basic-table', BasicTableView.as_view(), name='basic-table'),
    path('advance-table', AdvanceTableView.as_view(), name='advance-table'),
    path('bulk-select', BulkSelectView.as_view(), name='bulk-select' ),
    path('chartjs', ChartjsView.as_view(), name='chartjs'),
    path('line-charts', LineChartsView.as_view(), name='line-charts'),
    path('bar-charts', BarChartsView.as_view(), name='bar-charts'),
    path('candlestick-charts', CandlestickView.as_view(), name='candlestick-charts'),
    path('geo-map', GeoMapView.as_view(), name='geo-map'),
    path('scatter', ScatterView.as_view(), name='scatter'),
    path('pie-charts', PieChartView.as_view(), name='pie-charts'),
    path('radar-charts', RadarChartView.as_view(), name='radar-charts'),
    path('heatmap', HeatMapView.as_view(), name='heatmap'),
    path('how-to-use', HowToUseView.as_view(), name='how-to-use'),
    path('feed', SocialsFeedView.as_view(), name='feed'),
    path('activity-log', ActivityLogView.as_view(), name='activity-log'),
    path('notification', NotificationsView.as_view(), name='notification'),
    path('follower', FollowerView.as_view(), name='follower'),
    path('font-awesome', FontAwesomeView.as_view(), name='font-awesome'),
    path('bootstrap-icons', BootStrapIconView.as_view(), name='bootstrap-icons'),
    path('feather', FeatherIconView.as_view(), name='feather'),
    path('material-icon', MaterialIconView.as_view(), name='material-icon'),
    path('google-map', GoogleMapView.as_view(), name='google-map'),
    path('leaflet', LeafletMapView.as_view(), name='leaflet-map'),
    path('widget', WidgetView.as_view(), name='widget'),
    path('changelog', ChangelogView.as_view(), name='changelog'),
    path('design-file', DesignFileView.as_view(), name='design-file'),
    path('gulp', GulpView.as_view(), name='gulp'),
    path('getting-started', GettingStartView.as_view(), name='getting-started'),
    path('configuration', ConfigurationView.as_view(), name='configuration'),
    path('styling', StylingView.as_view(), name='styling'),
    path('dark-mode', DarkModeView.as_view(), name='dark-mode'),
    path('plugin', PluginView.as_view(), name='plugin'),
]