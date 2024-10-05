from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ProductListTemplateView(TemplateView):
    template_name = "apps/product/product-grid.html"


class ProductListDetailView(TemplateView):
    template_name = "apps/product/product-details.html"


class ProductListView(TemplateView):
    template_name = "apps/product/product-list.html"


class OrderDetailView(TemplateView):
    template_name = "apps/order/order-details.html"


class OrderListView(TemplateView):
    template_name = "apps/order/order-list.html"


class CustomerView(TemplateView):
    template_name = "apps/customer/customers.html"


class CustomerDetailView(TemplateView):
    template_name = "apps/customer/customer-details.html"


class ShoppingCartView(TemplateView):
    template_name = "apps/shopping-cart.html"


class CheckOutView(TemplateView):
    template_name = "apps/checkout.html"


class BillingView(TemplateView):
    template_name = "apps/billing.html"


class InvoiceView(TemplateView):
    template_name = "apps/invoice.html"


class CrmTemplateView(TemplateView):
    template_name = "apps/dashboard/crm.html"


class CalendarView(TemplateView):
    template_name = "apps/calendar.html"


class AnalyticsView(TemplateView):
    template_name = "apps/dashboard/analytics.html"


class ECommerceView(TemplateView):
    template_name = "apps/dashboard/e-commerce.html"


class ManagementView(TemplateView):
    template_name = "apps/dashboard/project-management.html"


class SaasView(TemplateView):
    template_name = "apps/dashboard/saas.html"


class ChatView(TemplateView):
    template_name = "apps/chat/chat.html"


class InboxView(TemplateView):
    template_name = "apps/email/inbox.html"


class EmailDetailView(TemplateView):
    template_name = "apps/email/email-detail.html"


class ComposeView(TemplateView):
    template_name = "apps/email/compose.html"


class CreateEventView(TemplateView):
    template_name = "apps/events/create-an-event.html"


class EventDetailView(TemplateView):
    template_name = "apps/events/event-detail.html"


class EventListView(TemplateView):
    template_name = "apps/events/event-list.html"


class KanbanView(TemplateView):
    template_name = "apps/kanban/kanban.html"


class StarterView(TemplateView):
    template_name = "apps/starter/starter.html"


class LandingView(TemplateView):
    template_name = "apps/landing/landing.html"


class LoginView(TemplateView):
    template_name = "apps/authentication/simple/login.html"


class LogoutView(TemplateView):
    template_name = "apps/authentication/simple/logout.html"


class RegisterView(TemplateView):
    template_name = "apps/authentication/simple/register..html"


class ForgotPasswordView(TemplateView):
    template_name = "apps/authentication/simple/forgot-password..html"


class ConfirmMailView(TemplateView):
    template_name = "apps/authentication/simple/confirm-mail..html"


class ResetPasswordView(TemplateView):
    template_name = "apps/authentication/simple/reset-password.html"


class LockScreenView(TemplateView):
    template_name = "apps/authentication/simple/lock-screen.html"


class WizardView(TemplateView):
    template_name = "apps/authentication/wizard.html"


class ProfileView(TemplateView):
    template_name = "apps/user/profile.html"


class SettingsUserView(TemplateView):
    template_name = "apps/user/settings.html"


class PricingAltView(TemplateView):
    template_name = "apps/pricing/pricing-alt.html"


class PricingDefaultView(TemplateView):
    template_name = "apps/pricing/pricing-default.html"


class FaqBasicView(TemplateView):
    template_name = "apps/faq/faq-basic.html"


class FaqAltView(TemplateView):
    template_name = "apps/faq/faq-alt.html"


class FaqAccordionView(TemplateView):
    template_name = "apps/faq/fac-accordion.html"


class Error404View(TemplateView):
    template_name = "apps/errors/404.html"


class Error500View(TemplateView):
    template_name = "apps/errors/500.html"


class AssociationsView(TemplateView):
    template_name = "apps/miscellaneous/associations.html"


class InvitePeopleView(TemplateView):
    template_name = "apps/miscellaneous/invite-people.html"


class PrivacyPolicyView(TemplateView):
    template_name = "apps/miscellaneous/privacy-policy.html"


class FormControlView(TemplateView):
    template_name = "apps/forms/basic/form-control.html"


class InputGroupView(TemplateView):
    template_name = "apps/forms/basic/input-group.html"


class SelectView(TemplateView):
    template_name = "apps/forms/basic/select.html"


class CheckView(TemplateView):
    template_name = "apps/forms/basic/check.html"


class RangeView(TemplateView):
    template_name = "apps/forms/basic/range.html"


class LayoutView(TemplateView):
    template_name = "apps/forms/basic/layout.html"


class AdvanceSelectView(TemplateView):
    template_name = "apps/forms/advance/advance-select.html"


class DatePickerView(TemplateView):
    template_name = "apps/forms/advance/date-picker.html"


class EditorAdvanceView(TemplateView):
    template_name = "apps/forms/advance/editor.html"


class EmojiButtonView(TemplateView):
    template_name = "apps/forms/advance/emoji-button.html"


class FileUploaderView(TemplateView):
    template_name = "apps/forms/advance/file-uploader.html"


class RatingView(TemplateView):
    template_name = "apps/forms/advance/rating.html"


class FloatingLabelView(TemplateView):
    template_name = "apps/forms/floating-labels.html"


class WizardFormView(TemplateView):
    template_name = "apps/forms/wizard.html"


class ValidationFormView(TemplateView):
    template_name = "apps/forms/validation.html"


class BasicTableView(TemplateView):
    template_name = "apps/tables/basic-tables.html"


class AdvanceTableView(TemplateView):
    template_name = "apps/tables/advance-tables.html"


class BulkSelectView(TemplateView):
    template_name = "apps/tables/bulk-select.html"


class ChartjsView(TemplateView):
    template_name = "apps/charts/chartjs.html"


class LineChartsView(TemplateView):
    template_name = "apps/charts/echarts/line-charts.html"


class BarChartsView(TemplateView):
    template_name = "apps/charts/echarts/bar-charts.html"


class CandlestickView(TemplateView):
    template_name = "apps/charts/echarts/candlestick-charts.html"


class GeoMapView(TemplateView):
    template_name = "apps/charts/echarts/geo-map.html"


class ScatterView(TemplateView):
    template_name = "apps/charts/echarts/scatter-charts.html"


class PieChartView(TemplateView):
    template_name = "apps/charts/echarts/pie-charts.html"


class RadarChartView(TemplateView):
    template_name = "apps/charts/echarts/radar.html"


class HeatMapView(TemplateView):
    template_name = "apps/charts/echarts/heatmap-charts.html"


class HowToUseView(TemplateView):
    template_name = "apps/charts/echarts/how-to-use.html"


class SocialsFeedView(TemplateView):
    template_name = "apps/socials/feed.html"


class ActivityLogView(TemplateView):
    template_name = "apps/socials/activity-log.html"


class NotificationsView(TemplateView):
    template_name = "apps/socials/notifications.html"


class FollowerView(TemplateView):
    template_name = "apps/socials/follower.html"


class FontAwesomeView(TemplateView):
    template_name = "apps/icons/font-awesome.html"


class BootStrapIconView(TemplateView):
    template_name = "apps/icons/bootstrapicon.html"


class FeatherIconView(TemplateView):
    template_name = "apps/icons/feather.html"


class MaterialIconView(TemplateView):
    template_name = "apps/icons/material-icons.html"


class GoogleMapView(TemplateView):
    template_name = "apps/maps/google-map.html"


class LeafletMapView(TemplateView):
    template_name = "apps/maps/leaflet-map.html"


class WidgetView(TemplateView):
    template_name = "apps/widgets/widgets.html"


class ChangelogView(TemplateView):
    template_name = "apps/changelog/changelog.html"


class DesignFileView(TemplateView):
    template_name = "apps/design_file/design-file.html"


class GulpView(TemplateView):
    template_name = "apps/gulp/gulp.html"


class GettingStartView(TemplateView):
    template_name = "apps/getting_started/getting-started.html"


class ConfigurationView(TemplateView):
    template_name = "apps/customization/configuration.html"


class StylingView(TemplateView):
    template_name = "apps/customization/styling.html"


class DarkModeView(TemplateView):
    template_name = "apps/customization/dark-mode.html"


class PluginView(TemplateView):
    template_name = "apps/customization/plugin.html"
